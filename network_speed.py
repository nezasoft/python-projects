import psutil
import speedtest
from tabulate import tabulate

class Network_Details(object):
    def __init__(self):
        self.tester = psutil.if_addrs(c)
        self.speed = speedtest.Speed()
        self.interface = self.interfaces()[0]
        self.download_speed = self.speeds()["download"]
        self.upload_speed = self.speeds()["upload"]


   def __str__(self):
       data = {"Interface:" :[self.interface],
               "Download:":[str(self.download_speed)+"Mbps"],
               "Upload:":[str(self.upload_speed)+"Mbps"]}

       table = tabulate(data, headers="keys",tablefmt="pretty")

       return str(table)