#!/usr/bin/env python3
"""
Test simple et rapide du serveur DHCP
"""

import socket
from scapy.all import BOOTP, DHCP
import random


def quick_test(serial_number=None):
    if not serial_number:
        serial_number = f"TESTDEV{random.randint(100, 999)}"

    print(f"🧪 Test DHCP avec numéro de série: {serial_number}")
    print("=" * 50)
    # Création d'un packet DHCP simple
    xid = random.randint(1, 0xFFFFFFFF)
    mac = bytes([0x00, 0x0C, 0x29, 0x12, 0x34, 0x56])

    # Numéro de série de test (comme dans votre serveur DHCP)
    serial_number = "TESTSERIAL123456"

    dhcp_options = [
        ("message-type", "discover"),
        ("client_id", serial_number.encode()),  # 🎯 Numéro de série ajouté !
        ("hostname", b"test-device"),
        ("end"),
    ]

    bootp = BOOTP(op=1, xid=xid, chaddr=mac + b"\x00" * 10, flags=0x8000)

    dhcp = DHCP(options=dhcp_options)
    packet = bootp / dhcp

    # Envoi
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", 68))
    sock.settimeout(3)

    try:
        print("📤 Envoi DHCP DISCOVER...")
        sock.sendto(bytes(packet), ("127.0.0.1", 67))

        print("⏳ Attente réponse...")
        data, addr = sock.recvfrom(1024)

        response = BOOTP(data)
        print("✅ Réponse OFFER reçue !")
        response.show()

        # 🎯 Test du REQUEST après l'OFFER
        print("\n📤 Envoi DHCP REQUEST...")

        # Récupération de l'IP offerte
        offered_ip = response.yiaddr
        print(f"💡 IP offerte: {offered_ip}")

        # Création du packet REQUEST
        dhcp_request_options = [
            ("message-type", "request"),
            ("client_id", serial_number.encode()),
            ("requested_addr", offered_ip),
            ("server_id", "127.0.0.1"),  # Votre serveur
            ("hostname", b"test-device"),
            ("end"),
        ]

        bootp_request = BOOTP(op=1, xid=xid, chaddr=mac + b"\x00" * 10, flags=0x8000)
        dhcp_request = DHCP(options=dhcp_request_options)
        request_packet = bootp_request / dhcp_request

        # Envoi du REQUEST
        sock.sendto(bytes(request_packet), ("127.0.0.1", 67))

        print("⏳ Attente réponse ACK...")
        ack_data, ack_addr = sock.recvfrom(1024)

        ack_response = BOOTP(ack_data)
        print("🎉 Réponse ACK reçue !")
        ack_response.show()

        print(
            f"\n✅ Test complet réussi ! Device '{serial_number}' devrait être enregistré avec IP {offered_ip}"
        )

    except socket.timeout:
        print("❌ Pas de réponse")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    finally:
        sock.close()


if __name__ == "__main__":
    import sys

    # Permet de passer un numéro de série en argument
    if len(sys.argv) > 1:
        serial = sys.argv[1]
        quick_test(serial)
    else:
        quick_test()
