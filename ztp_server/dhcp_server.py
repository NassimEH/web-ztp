import socket
from scapy.all import packet, BOOTP, DHCP

from dhcp_db import DHCPData


class DHCPServer:
    def __init__(self, ip_address: str, bind_port=67, buffer_size=1024):
        self.ip_address = ip_address
        self.bind_port = bind_port
        self.buffer_size = buffer_size

        self.dhcp_data = DHCPData()

    def get_dhcp_packet(self, data: bytes):
        return BOOTP(data)

    def get_ip_in_pool(self, packet: packet):
        for option in packet["DHCP"].options:
            if option[0] == "requested_addr":
                return option[1]

        return "10.0.0.120"

    def create_dhcp_options(self, packet: packet, message_type: str):
        new_options = [
            ("subnet_mask", self.dhcp_data.subnet),
            ("router", self.dhcp_data.router),
            ("name_server", "8.8.8.8"),
            ("domain", "local"), #15
            ("static-routes", self.dhcp_data.router+":"+self.dhcp_data.subnet), #33
            ("boot-file-name", "http:"+self.dhcp_data.url+"/ztp.py"), #67
            ("message-type", message_type),
            ("lease_time", 3600),
            ("server_id", self.ip_address),
        ]

        for option in packet["DHCP"].options:
            if option[0] == "message-type":
                pass
            elif option[0] == "requested_addr":
                pass
            else:
                new_options.append(option)

        return new_options

    def create_bootp(self, packet: packet, client_ip: str):
        return BOOTP(
            op=2,
            yiaddr=client_ip,
            siaddr=self.ip_address,
            chaddr=packet["BOOTP"].chaddr,
            xid=packet["BOOTP"].xid,
        )

    def dhcp_offer(self, packet: packet):
        client_ip = self.get_ip_in_pool(packet)

        options = self.create_dhcp_options(packet, "offer")

        bootp = self.create_bootp(packet, client_ip)

        dhcp = DHCP(options=options)
        reply = bootp / dhcp

        return bytes(reply)

    def dhcp_ack(self, packet: packet):
        client_ip = self.get_ip_in_pool(packet)

        options = self.create_dhcp_options(packet, "ack")

        bootp = self.create_bootp(packet, client_ip)

        dhcp = DHCP(options=options)
        reply = bootp / dhcp

        return bytes(reply)

    def create_dhcp_reply(self, packet: packet):
        for option in packet["DHCP"].options:
            if option[0] == "message-type":
                message_type = option[1]
                break

        if message_type == 1:
            return self.dhcp_offer(packet)
        elif message_type == 3:
            return self.dhcp_ack(packet)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.bind((self.ip_address, self.bind_port))
            print(f"Serveur en écoute sur {self.ip_address}:{self.bind_port}...")

            while True:
                data, addr = s.recvfrom(self.buffer_size)
                print(f"Paquet reçu de {addr[0]} :")

                packet = self.get_dhcp_packet(data)
                print("Packet reçu :")
                packet.show()

                offer = self.create_dhcp_reply(packet)
                print("Packet envoyé :")
                self.get_dhcp_packet(offer).show()
                # add_device(packet)

                s.sendto(offer, ("255.255.255.255", 68))


if __name__ == "__main__":
    server = DHCPServer("0.0.0.0")
    server.run()
