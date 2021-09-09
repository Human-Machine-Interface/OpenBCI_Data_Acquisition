import serial
ser = serial.Serial('COM11', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'J')     # write a string
ser.write(b'A')     # write a string
#ser.close()             # close port

while True:
    if ser.inWaiting():
        packet=ser.readline()
        print(packet.decode('utf'))
        break
    else:
        print("nada")