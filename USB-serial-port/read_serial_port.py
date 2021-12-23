import serial

serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
serial_port.flush()

while True:
    try:
        data = serial_port.readline().decode('utf-8').rstrip()
        print(data)
    except Exception as e:
        print(str(e))
        exit()
