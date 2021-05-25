import nmap
import csv
import json
import argparse

def mapeo(target, begin, end):
    nmap_path = r"C:\Program Files (x86)\Nmap\nmap.exe"
    scanner = nmap.PortScanner()

    for i in range(int(begin),int(end)+1):

        res = scanner.scan(target, str(i))
        res = res["scan"][target]["tcp"][i]["state"]
        print(f"port {i} is {res}. ")
        puertos = [res]
        with open(r'scan.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(puertos)

