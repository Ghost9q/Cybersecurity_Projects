Simple network scanner

This program is a simple network scanner that uses Scapy to scan your network and retrieve some information about the hosts. 
We are able to locate hosts on the network using ARP, after that we find the vendor of the host by looking at its MAC address. 
At the end we are able to guess the type of device according to its vendor and the TTL number of the packet that we received 
from the host. Please note that the program is not perfect and might have problems, so make sure to give feedback on my linkedin:
www.linkedin.com/in/shokran-ataii-48326b312.

Dependencies
To be able to run the program you need have python 3.13.3 or above. After installing python install these libraries using pip:
scapy 2.6.1 and requests 2.32.5.

You can run the following commands in your terminal after installing python:
pip install scapy==2.6.1
pip install requests==2.32.5
