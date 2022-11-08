from importlib.metadata import files
import os
import requests


os.system("clear")

print("Wellcome IP-FORWARDER SCRIPT from Moein\n")

iran_vps_ip = input("Please enter your iran vps ip : ")
foreign_vps_ip = input("Please enter your foriegn vps ip for forwrding traffic : ")

def ip_forwarding_linux():
    commands = f"sudo sysctl net.ipv4.ip_forward=1 && iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination {iran_vps_ip} && sudo iptables -t nat -A PREROUTING -j DNAT --to-destination {foreign_vps_ip} && sudo iptables -t nat -A POSTROUTING -j MASQUERADE"
    print("\nIp forwarding finished...\n")

ip_forwarding_linux()