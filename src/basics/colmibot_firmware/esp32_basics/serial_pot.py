import serial

PORT = '/dev/ttyUSB0'
BAUDRATE = 115200

esp32 = serial.Serial(PORT, BAUDRATE, timeout=1)
#bucle infinito para leer lineas completas y convertirlas a texto verifica que haya algo es una prueba manual sin Ros2
while True:
    linea = esp32.readline().decode().strip()

    if linea:
        print(f'ADC = {linea}')
