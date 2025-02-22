import socket
from scapy.all import packet, BOOTP, DHCP

from dhcp_server.dhcp_db import DHCPData
from app.utils import device_utils

class DHCPServer:
    def __init__(self, ip_address: str, bind_port=67, buffer_size=1024):
        self.ip_address = ip_address
        self.bind_port = bind_port
        self.buffer_size = buffer_size

        self.dhcp_data = DHCPData()
        self.get_ip = self.dhcp_data.get_ip_in_pool()

    def get_dhcp_packet(self, data: bytes):
        return BOOTP(data)

    def get_dhcp_option(self, packet: packet, option: str):
        for dhcp_option in packet["DHCP"].options:
            if dhcp_option[0] == option:
                return dhcp_option[1]

    def get_reply_message_type(self, message_type):
        if message_type == "discover" or message_type == 1:
            return "offer"
        elif message_type == "request" or message_type == 3:
            return "ack"

    def get_serial_number(self, packet):
        client_id = self.get_dhcp_option(packet, "client_id")

        if client_id:
            serial_number = client_id.decode("utf-8")
            return serial_number

    def get_ip_in_pool(self, requested_addr, serial_number):
        if requested_addr:
            return requested_addr

        if serial_number:
            return self.dhcp_data.get_ip(serial_number)

    def get_bootfile(self, serial_number):
        if serial_number:
            serial_number = ''.join(c for c in serial_number if c.isprintable()).strip()
            return self.dhcp_data.get_bootfile(serial_number)

    def create_dhcp_options(self, message_type: str):
        new_options = [
            ("message-type", message_type),
            ("server_id", self.dhcp_data.server_ip),
            ("lease_time", 3600),
            ("subnet_mask", self.dhcp_data.subnet),
            ("domain", "local"),  # 15
            # ("router", self.dhcp_data.router),
            # ("name_server", "8.8.8.8"),
            # ("static-routes", self.dhcp_data.router+":"+self.dhcp_data.subnet), # 33
            # ("tftp_server", "10.30.31.30"),  # Option 66
            # ("option-67", b"http://10.30.31.30:80/config.txt"),  # Option 67 brute
            ("end"),
        ]

        # for option in packet["DHCP"].options:
        #     if option[0] in ["message-type", "requested_addr", "server_id"]:
        #         pass  # Ne pas dupliquer ces options
        #     else:
        #         new_options.append(option)

        return new_options

    def create_bootp(self, client_ip: str, chaddr, xid, bootfile):
        return BOOTP(
            op=2,
            yiaddr=client_ip,
            siaddr=self.ip_address,
            chaddr=chaddr,
            xid=xid,
            file=bootfile,
        )

    # def dhcp_offer(self, packet: packet):
    #     client_ip = self.get_ip_in_pool(packet)

    #     options = self.create_dhcp_options(packet, "offer")

    #     bootp = self.create_bootp(packet, client_ip)

    #     dhcp = DHCP(options=options)
    #     reply = bootp / dhcp

    #     return bytes(reply)

    # def dhcp_ack(self, packet: packet):
    #     client_ip = self.get_ip_in_pool(packet)

    #     options = self.create_dhcp_options(packet, "ack")

    #     bootp = self.create_bootp(packet, client_ip)

    #     dhcp = DHCP(options=options)
    #     reply = bootp / dhcp

    #     return bytes(reply)

    def create_dhcp_reply(self, packet: packet):
        requested_addr = self.get_dhcp_option(packet, "requested_addr")
        serial_number = self.get_serial_number(packet)
        client_ip = self.get_ip_in_pool(requested_addr, serial_number)

        message_type = self.get_dhcp_option(packet, "message-type")
        reply_message_type = self.get_reply_message_type(message_type)

        if reply_message_type:
            options = self.create_dhcp_options(reply_message_type)

            chaddr = packet["BOOTP"].chaddr
            xid = packet["BOOTP"].xid
            bootfile = self.get_bootfile(serial_number)
            bootp = self.create_bootp(client_ip, chaddr, xid, bootfile)
            dhcp = DHCP(options=options)

            reply = bootp / dhcp

            return bytes(reply)

        # if message_type == 1:
        #     return self.dhcp_offer(packet)
        # elif message_type == 3:
        #     return self.dhcp_ack(packet)

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
                if offer:
                    print("Packet envoyé :")
                    self.get_dhcp_packet(offer).show()
                    # add_device(packet)

                    s.sendto(offer, ("255.255.255.255", 68))
                else:
                    print("rien a renvoyer")

    # def run(self):
    #     """Main server loop using socket"""
    #     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    #         s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #         s.bind((self.ip_address, self.bind_port))
    #         print(f"Serveur en écoute sur {self.ip_address}:{self.bind_port}...")

    #         while True:
    #             data, addr = s.recvfrom(self.buffer_size)
    #             print(f"Paquet reçu de {addr[0]} :")

    #             # Extract DHCP packet
    #             packet = self.get_dhcp_packet(data)
    #             print("Packet reçu :")
    #             packet.show()

    #             # Extract client MAC from the DHCP request
    #             client_mac = self.get_mac_from_packet(packet)
    #             print(f"Client MAC: {client_mac}")

    #             # Create the DHCP offer response
    #             offer = self.create_dhcp_reply(packet)
    #             if offer:
    #                 print("Packet envoyé :")
    #                 self.get_dhcp_packet(offer).show()

    #                 # Send the response **directly to the requesting MAC address**
    #                 with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as raw_sock:
    #                     raw_sock.bind((self.interface, 0))  # Bind to network interface
    #                     raw_sock.send(offer)  # Send raw Ethernet frame

    #             else:
    #                 print("Rien à renvoyer")


if __name__ == "__main__":
    server = DHCPServer("0.0.0.0")
    server.run()
