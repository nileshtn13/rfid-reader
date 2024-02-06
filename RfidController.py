import serial
from serial.tools import list_ports



class RfidReader():
    def __init__(self):
        self.rfid_device = None
        self.device_status = False
        self.device_connection = False
        self.read_time = 1
        self.single_polling_inc = "BB00220000227E"
        self.tag_id = None
        self.connect_device()

    def connect_device(self):
        ports = list(list_ports.comports())
        for port in ports:
            if "CP2102" in port.description:
                self.device_status = True
                try:
                    self.rfid_device = serial.Serial(port=port.device, baudrate=115200, timeout=1)
                except serial.SerialException:
                    print("device already open by some other program")
                if self.rfid_device.isOpen():
                    self.device_connection = True
                    print("device has connected successfully")
                    return True
                else:
                    self.device_status = False
                    print("found device but not able to connect please retry")
                    return False
            else:
                print("serial device with name \"CP2102\" device not found")

    def disconnect_device(self):
        self.rfid_device.close()
        self.device_status = False
        if not self.rfid_device.isOpen():
            self.device_connection = False
            print("device has disconnected successfully")
            return True
        else:
            self.device_connection = True
            print("could not able to close the device")
            return False
        
    def check_device_serial_conection(self):
        self.device_connection = self.rfid_device.isOpen()
        return self.device_connection
    
    def check_device_connection(self):
        ports = list(list_ports.comports())
        for port in ports:
            if "CP2102" in port.description:
                self.device_status = True
            else:
                self.device_status = True
        return self.device_status


    def __send_request(self):
        bytecode = bytes.fromhex(self.single_polling_inc)
        self.rfid_device.write(bytecode)

    def __get_tag_id(self):
        data = self.rfid_device.read(40)
        if data.hex() == "bb01ff000115167e":
            self.tag_id = None
        else:
            if data.hex()[:2] == "bb" and data.hex()[-2:] == "7e":
                self.tag_id = data.hex()[16:-8]
            else:
                self.tag_id = None
        return True

    def read_tag(self):
        self.__send_request()
        self.__get_tag_id
        return self.tag_id