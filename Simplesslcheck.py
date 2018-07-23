import OpenSSL
import ssl
import socket
from datetime import date
import datetime
import sys

class Simplesslcheck:
        with open("C:/tmp/items.txt", "r") as f:
            for line in f:
                server = line.split(",")[0]
                port = line.split(",")[1]
                list_adr = (server, port.strip())
                try:
                    cert = ssl.get_server_certificate(list_adr)
                    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
                    data = x509.get_notAfter()
                    index = 0
                    year = day = ""
                    month = ""
                    # Get year
                    while index <= 3:
                        year += data[index]
                        index += 1
                    # Get month
                    counter = index + 1
                    while index <= counter:
                        month += data[index]
                        index += 1
                    # Get day
                    counter += 2
                    while index <= counter:
                        day += data[index]
                        index += 1
                    # print year, month, day

                    now = datetime.datetime.now()
                    date_now = date(now.year, now.month, now.day)
                    date_cer = date(int(year), int(month), int(day))
                    print "Days left:",(date_cer - date_now).days
                    cnt += 1
                except socket.gaierror:
                    print sys.exc_info()
                    pass