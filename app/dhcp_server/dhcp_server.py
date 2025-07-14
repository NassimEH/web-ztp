import socket
from scapy.all import packet, BOOTP, DHCP, get_if_list, get_if_addr

from dhcp_server.dhcp_db import DHCPData

import env.config as cfg


class DHCPServer:
    def __init__(self, server_ip: str, bind_port=67, buffer_size=1024):
        self.server_ip = server_ip
        self.bind_port = bind_port
        self.buffer_size = buffer_size

        self.dhcp_data = DHCPData()
        self.get_ip = self.dhcp_data.get_ip_in_pool()

        for iface in get_if_list():
            try:
                if get_if_addr(iface) == self.server_ip:
                    self.interface = iface
                    break
            except Exception:
                self.interface = None
                continue

    def get_dhcp_packet(self, data: bytes):
        return BOOTP(data)

    def get_dhcp_option(self, packet: packet, option: str):
        if "DHCP" not in packet:
            return None
        for dhcp_option in packet["DHCP"].options:
            if isinstance(dhcp_option, tuple) and len(dhcp_option) >= 2:
                if dhcp_option[0] == option:
                    return dhcp_option[1]
            elif dhcp_option == "end":
                break
        return None

    def get_reply_message_type(self, message_type):
        if message_type == "discover" or message_type == 1:
            return "offer"
        elif message_type == "request" or message_type == 3:
            return "ack"
        else:
            return None

    def get_serial_number(self, packet):
        client_id = self.get_dhcp_option(packet, "client_id")
        if client_id:
            if isinstance(client_id, bytes):
                serial_number = client_id.decode("utf-8", errors="ignore")
            else:
                serial_number = str(client_id)

            serial_number = "".join(c for c in serial_number if c.isprintable()).strip()

            if (
                serial_number
                and not serial_number.startswith("\x01")
                and len(serial_number) > 3
            ):
                return serial_number

        hostname = self.get_dhcp_option(packet, "hostname")
        if hostname:
            if isinstance(hostname, bytes):
                hostname = hostname.decode("utf-8", errors="ignore")
            else:
                hostname = str(hostname).strip()

            return hostname

        chaddr = packet["BOOTP"].chaddr
        mac_addr = ":".join(f"{b:02x}" for b in chaddr[:6])
        return f"MAC-{mac_addr}"

    def get_ip_in_pool(self, requested_addr, serial_number):
        if requested_addr:
            return requested_addr

        if serial_number:
            assigned_ip = self.dhcp_data.get_ip(serial_number)
            if assigned_ip:
                return assigned_ip
            else:
                return next(self.get_ip)

        return None

    def get_bootfile(self, serial_number):
        if not serial_number:
            return None

        bootfile = self.dhcp_data.get_bootfile(serial_number)
        if bootfile:
            return bootfile

        return None

    def create_dhcp_options(self, message_type: str, bootfile: str):
        new_options = [
            ("message-type", message_type),
            ("server_id", self.server_ip),
            ("lease_time", 3600),
            ("subnet_mask", self.dhcp_data.subnet),
            ("domain", "local"),
            ("router", self.server_ip),
        ]

        if bootfile:
            new_options.append((67, bootfile.encode("utf-8")))  # Bootfile option

        new_options.append("end")

        return new_options

    def create_bootp(self, client_ip: str, chaddr, xid, bootfile):
        bootp_packet = BOOTP(
            op=2,
            yiaddr=client_ip,
            siaddr=self.server_ip,
            chaddr=chaddr,
            xid=xid,
        )

        if bootfile:
            bootp_packet.file = bootfile

        return bootp_packet

    def create_dhcp_reply(self, packet: packet):
        requested_addr = self.get_dhcp_option(packet, "requested_addr")
        serial_number = self.get_serial_number(packet)

        client_ip = self.get_ip_in_pool(requested_addr, serial_number)

        if not client_ip:
            return None

        message_type = self.get_dhcp_option(packet, "message-type")
        reply_message_type = self.get_reply_message_type(message_type)

        if reply_message_type == "ack":
            hostname = getattr(packet["BOOTP"], "hostname", None)
            self.dhcp_data.create_or_update_device(
                serial_number, client_ip, hostname, True
            )

        if reply_message_type:
            bootfile = self.get_bootfile(serial_number)

            options = self.create_dhcp_options(reply_message_type, bootfile)

            chaddr = packet["BOOTP"].chaddr
            xid = packet["BOOTP"].xid
            bootp = self.create_bootp(client_ip, chaddr, xid, bootfile)
            dhcp = DHCP(options=options)

            reply = bootp / dhcp

            return bytes(reply)

        return None

    def send_dhcp_reply(self, offer, ip_address: bytes):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(offer, (ip_address, 68))

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            if self.interface:
                s.setsockopt(
                    socket.SOL_SOCKET, socket.SO_BINDTODEVICE, self.interface.encode()
                )

            s.bind(("0.0.0.0", self.bind_port))
            print(f"Serveur DHCP en écoute sur 0.0.0.0:{self.bind_port}")
            print(f"IP du serveur DHCP: {self.server_ip}")

            while True:
                data, addr = s.recvfrom(self.buffer_size)
                packet = self.get_dhcp_packet(data)

                reply = self.create_dhcp_reply(packet)
                if reply:
                    s.sendto(reply, ("255.255.255.255", 68))


if __name__ == "__main__":
    server_ip = "0.0.0.0"
    server = DHCPServer(server_ip)
    server.run()
