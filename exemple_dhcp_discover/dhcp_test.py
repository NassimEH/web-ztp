#!/usr/bin/env python3
"""
Quick and easy DHCP server test
"""

import socket
from scapy.all import BOOTP, DHCP
import random


def quick_test(serial_number=None):
    if not serial_number:
        serial_number = f"TESTDEV{random.randint(100, 999)}"

    print(f"🧪 DHCP test with serial number: {serial_number}")
    print("=" * 50)
    # Creating a simple DHCP packet
    xid = random.randint(1, 0xFFFFFFFF)
    mac = bytes([0x00, 0x0C, 0x29, 0x12, 0x34, 0x56])

    serial_number = "TESTSERIAL123456"

    dhcp_options = [
        ("message-type", "discover"),
        ("client_id", serial_number.encode()),
        ("hostname", b"test-device"),
        ("end"),
    ]

    bootp = BOOTP(op=1, xid=xid, chaddr=mac + b"\x00" * 10, flags=0x8000)

    dhcp = DHCP(options=dhcp_options)
    packet = bootp / dhcp

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", 68))
    sock.settimeout(3)

    try:
        print("📤 Sending DHCP DISCOVER...")
        sock.sendto(bytes(packet), ("127.0.0.1", 67))

        print("⏳ Waiting for response...")
        data, addr = sock.recvfrom(1024)

        response = BOOTP(data)
        print("✅ OFFER response received!")
        response.show()

        print("\n📤 Sending DHCP REQUEST...")

        offered_ip = response.yiaddr
        print(f"💡 Offered IP: {offered_ip}")

        dhcp_request_options = [
            ("message-type", "request"),
            ("client_id", serial_number.encode()),
            ("requested_addr", offered_ip),
            ("server_id", "127.0.0.1"),
            ("hostname", b"test-device"),
            ("end"),
        ]

        bootp_request = BOOTP(op=1, xid=xid, chaddr=mac + b"\x00" * 10, flags=0x8000)
        dhcp_request = DHCP(options=dhcp_request_options)
        request_packet = bootp_request / dhcp_request

        sock.sendto(bytes(request_packet), ("127.0.0.1", 67))

        print("⏳ Waiting for ACK response...")
        ack_data, ack_addr = sock.recvfrom(1024)

        ack_response = BOOTP(ack_data)
        print("🎉 ACK response received!")
        ack_response.show()

        print(
            f"\n✅ Test complet réussi ! Device '{serial_number}' devrait être enregistré avec IP {offered_ip}"
        )

    except socket.timeout:
        print("❌ Pas de réponse")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        sock.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        serial = sys.argv[1]
        quick_test(serial)
    else:
        quick_test()
