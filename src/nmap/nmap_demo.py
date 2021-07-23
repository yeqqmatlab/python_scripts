import nmap

nm = nmap.PortScanner()

nm.scan('192.168.10.240-249', '22,21', '-sv')
a = nm.command_line()
print(a)