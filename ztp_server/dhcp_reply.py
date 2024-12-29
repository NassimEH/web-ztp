import socket
from scapy.all import packet
from scapy.all import BOOTP, DHCP, get_if_addr


def get_dhcp_packet(data: bytes) -> packet:
    return BOOTP(data)


def get_ip_in_pool(packet: packet) -> str:
    for option in packet["DHCP"].options:
        if option[0] == "requested_addr":
            return option[1]

    return "10.0.0.1"


def create_dhcp_reply(packet: packet, ip_address: str) -> bytes:
    ip_client = get_ip_in_pool(packet)

    new_options = [
        ("server_id", ip_address),
        ("lease_time", 3600),
        ("subnet_mask", "255.255.255.0"),
        # ("router", "0.0.0.0"),
        ("name_server", "8.8.8.8"),
    ]

    message_type = "offer"
    for option in packet["DHCP"].options:
        if option[0] == "message-type":
            if option[1] == 3:
                message_type = "ack"
            new_options.append(("message-type", message_type))
        elif option[0] == "requested_addr":
            pass
        else:
            new_options.append(option)

    bootp = BOOTP(
        op=2,
        yiaddr=ip_client,
        siaddr=ip_address,
        chaddr=packet["BOOTP"].chaddr,
        xid=packet["BOOTP"].xid,
    )
    dhcp = DHCP(options=new_options)
    reply = bootp / dhcp

    reply.show()

    return bytes(reply)


def dhcp_receive_message(interface: str, bind_port=67, buffer_size=1024) -> None:
    ip_address = get_if_addr(interface)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind((ip_address, bind_port))
        print(f"Serveur en écoute sur {ip_address}:{bind_port}...")

        while True:
            data, addr = s.recvfrom(buffer_size)
            print(f"Paquet reçu de {addr[0]} :")

            packet = get_dhcp_packet(data)
            packet.show()

            offer = create_dhcp_reply(packet, ip_address)
            s.sendto(offer, ("255.255.255.255", 68))

            print("Paquet envoyé.\n")


if __name__ == "__main__":
    dhcp_receive_message("enp0s3")
