from scapy.all import ARP, Ether, srp, IP, ICMP, sr1 #type:ignore
import requests

# ---------- MAC Vendor Lookup ----------
def get_vendor(mac):
    try:
        oui = mac.upper()[0:8].replace(":", "-")
        url = f"https://api.macvendors.com/{oui}"
        resp = requests.get(url, timeout=2)
        return resp.text if resp.status_code == 200 else "Unknown"
    except:
        return "Unknown"

# ---------- Ping to check TTL ----------
def get_ttl(ip):
    try:
        pkt = IP(dst=ip)/ICMP()
        reply = sr1(pkt, timeout=1, verbose=0)
        if reply:
            return reply.ttl
    except:
        pass
    return None

def guess_device_type(mac, ttl, vendor):
    # Guess from vendor
    vendor_lower = vendor.lower()
    if any(x in vendor_lower for x in ["cisco", "tp-link", "ubiquiti", "netgear", "ruijie networks"]):
        return "Networking Device"
    if any(x in vendor_lower for x in ["apple", "samsung", "huawei", "xiaomi"]):
        return "Smartphone/Tablet"
    if any(x in vendor_lower for x in ["vmware", "virtualbox"]):
        return "Virtual Machine"
    if any(x in vendor_lower for x in ["dell", "hp", "lenovo", "asus", "acer"]):
        return "PC/Laptop"

    # Guess from TTL
    if ttl:
        if ttl > 200:
            return "Router/Firewall"
        elif 100 < ttl < 150:
            return "Windows Host"
        elif 50 < ttl < 70:
            return "Linux/Unix Host"

    return "Unknown"

# ---------- Network Scanner ----------
def net_scanner(net):
    arp_pkt = ARP(pdst=net)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    pkt = ether / arp_pkt
    result = srp(pkt, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        vendor = get_vendor(mac)
        ttl = get_ttl(ip)
        dtype = guess_device_type(mac, ttl, vendor)
        devices.append({"ip": ip, "mac": mac, "vendor": vendor, "ttl": ttl, "type": dtype})
    return devices

# ----------main Program-----------
def main():
    while True:
        try:
            network = input("Enter your network/target address here (enter q to quit): ").lower().strip()
            target_type = 'unknown'
            if '/' in network:
                target_type = 'network'
            else:
                target_type = 'single-target'
    
            if network == 'q':
                break

            
            devices = net_scanner(network)
            print(f"Found {len(devices)} devices:\n")
            for d in devices:
                print(f"IP: {d['ip']}, MAC: {d['mac']}, Vendor: {d['vendor']}, TTL: {d['ttl']}, Type: {d['type']}\n")

                
            if len(devices) == 0 and target_type == 'single-target':
                print('target not reachable\n')
            elif len(devices) == 0 and target_type == 'network':
                print('''Something went wrong! Please make sure: 
the network address is correct.
you are connected to the network.\n''')

        except Exception:
            print('''Something went wrong! Please make sure: 
the network address is correct.
you are connected to the network.
you have all the dependencies installed. (if not use pip to install them (requests, scapy))\n''')

# ---------- Run ----------
if __name__ == '__main__':
    print('''
Note that the device type is not 100% accurate
it's just the most relevant guess according to 
the vendor and TTL of the device.\n''')
    main()
