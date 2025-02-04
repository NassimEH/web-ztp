import os

import requests

BACKEND_URL = os.getenv("BACKEND_URL")


class IPaddress:
    def __init__(self, ip_address: str):
        self.ip_address = ip_address
        self.octets = [int(octet) for octet in self.ip_address.split(".")]
        # self.bin_octets = [bin((octet)) for octet in self.octets]

    def next(self):
        new_ip = (
            f"{self.octets[0]}.{self.octets[1]}.{self.octets[2]}.{self.octets[3] + 1}"
        )
        return IPaddress(new_ip)

    def __lt__(self, other):
        if self.octets[0] != other.octets[0]:
            return self.octets[0] < other.octets[0]
        if self.octets[1] != other.octets[1]:
            return self.octets[1] < other.octets[1]
        if self.octets[2] != other.octets[2]:
            return self.octets[2] < other.octets[2]

        return self.octets[3] <= other.octets[3]

    def __str__(self):
        return self.ip_address


class DHCPData:
    def __init__(self):
        self.url = BACKEND_URL
        self.subnet = self.get_subnet()
        self.router = self.get_router()
        self.min_ip_pool = self.get_min_ip_pool()
        self.max_ip_pool = self.get_max_ip_pool()

    def get_subnet(self) -> str:
        try:
            # response = requests.get(self.url + "/subnet")
            # response.raise_for_status()
            return "255.255.255.0"
        except:
            pass

    def get_router(self) -> str:
        try:
            # response = requests.get(self.url + "/router")
            # response.raise_for_status()
            return "0.0.0.0"
        except:
            pass

    def get_min_ip_pool(self) -> str:
        try:
            # response = requests.get(self.url + "/min_ip_pool")
            # response.raise_for_status()
            return "10.0.0.10"
        except:
            pass

    def get_max_ip_pool(self) -> str:
        try:
            # response = requests.get(self.url + "/max_ip_pool")
            # response.raise_for_status()
            return "10.0.0.254"
        except:
            pass

    def get_use_ip(self) -> set:
        try:
            response = requests.get(self.url + "/ips")
            response.raise_for_status()
            return set(response)
        except:
            return set()

    def get_ip_in_pool(self) -> str:
        ip_address = IPaddress(self.min_ip_pool)
        max_ip_address = IPaddress(self.max_ip_pool)
        while ip_address < max_ip_address:
            ip_address = ip_address.next()
            yield str(ip_address)

    def add_device(
        self, serial_number: str, ip: str, hostname=None, interface=None
    ) -> dict:
        try:
            device = {
                "serial_number": serial_number,
                "ip": ip,
                **({"hostname": hostname} if hostname else {}),
                **({"interface": interface} if interface else {}),
            }

            response = requests.post(self.url + "/device", json=device)
            response.raise_for_status()
            return response.json()
        except:
            pass

    def get_ip(self, serial_number: str) -> dict:
        try:
            response = requests.get(self.url + "/ip/" + serial_number)
            response.raise_for_status()
            return response.json()
        except:
            return {}
