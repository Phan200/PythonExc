import nmap

nm=nmap.PortScanner()
print(nm.nmap_version())
nm.scan('192.168.1.14', '22-1024', '-v --version-all')
print(nm.scanstats())
print(nm.all_hosts())
print(nm.scaninfo())
print(nm.csv())
