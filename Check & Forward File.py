import glob
import os
import bluetooth
import sys
import time
from bluetooth import *
from PyOBEX.client import Client
from bt_proximity import BluetoothRSSI

log_file=open("BToothServer.log","a+")
sys.stdout=log_file
distance=0
direct=glob.glob('./Bluetooth/*.txt')
if len(direct)!=0:
    for f in direct:
        file=open(f,"r")
        source=file.readline(17)
        file.readline(1)
        print("New file received from source %s " % (source))
        print os.path.split(f)[1]
        BT_ADDR = source
        num=8
        btrssi = BluetoothRSSI(addr=BT_ADDR)
        print("Estimating source proximity using RSSI...")
        rssival=0
        for i in range(0, num):
            rssival+=btrssi.get_rssi()
            time.sleep(1)
        distance+=rssival/8
        print ("The source was approximately %d feet from the server" % abs(rssival/8))
        destination=file.readline(17)
        file.readline(1)
        print("File intended for destination %s " % (destination))
        contents=file.read()
        print ("Initiating search for destination device...")
        nearby_devices=bluetooth.discover_devices(flush_cache=True,lookup_names=True)
        print("Number of devices found: %d " % len(nearby_devices))
        for addr, name in nearby_devices:
            print("%s - %s " % (addr, name))
        flag=0
        for addr, name in nearby_devices:
            if destination==addr:
                device_name=bluetooth.lookup_name(addr)
                print("Device with destination ID found")
                print("Searching for OBEX service on %s - %s" % (addr, device_name))
                service_matches = find_service(name="OBEX Object Push", address=addr)
                if len(service_matches)==0:
                        print("Couldn't find the service. Device doesn't support file transfer. File will be deleted to avoid security risks.")
                        file.close()
                        os.remove(f)
                        break
                first_match=service_matches[0]
                port=first_match["port"]
                name=first_match["name"]
                host=first_match["host"]
                print("Connecting to \"%s\" on %s" % (name, device_name))
                client=Client(host,port)
                client.connect()
                client.put(os.path.split(f)[1], contents)
                client.disconnect()
                print("File successfully sent to destination and has been deleted from server.")
                file.close()
                os.remove(f)
                BT_ADDR = destination
                num=8
                btrssi = BluetoothRSSI(addr=BT_ADDR)
                print("Estimating destination proximity using RSSI...")
                rssival=0
                for i in range(0, num):
                    rssival+=btrssi.get_rssi()
                    time.sleep(1)
                distance+=rssival/8
                print ("The destination was approximately %d feet from the server" % abs(rssival/8))
                print ("Estimated distance between source and destination is %d feet +/-%f" % (abs(distance), abs(distance*0.25)))
                flag=0
                break
            else:
                flag=1
        if flag!=0:
            if len(nearby_devices)!=0:
                print("None of the found devices match specified destination ID")
        if len(nearby_devices)==0:
            print("Device with destination ID not found")

print("\n\n\n\n\n")
log_file.close()
sys.stdout=sys.__stdout__

