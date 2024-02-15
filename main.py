from RfidController import RfidReader
import time

a =  RfidReader()
a.connect_device()

device_status_memory = True
while True:
    device_status = a.check_device_connection()
    if device_status:
        if device_status_memory:
            id = a.read_tag()
            print(id)
        else:
            a.connect_device()
            device_status_memory = True
            id = a.read_tag()
            print(id)
    else:
        device_status_memory = False
        print("device not connected")
        
    time.sleep(1)
