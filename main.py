from RfidReaderClass import RfidReader
import time

a =  RfidReader()

while True:
    try:
        a.read_tag()
        a.get_tag_id()
    except KeyboardInterrupt:
        a.disconnect_device()
        break
