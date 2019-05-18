import RPi.GPIO

GPIO.setmode(GPIO.BCM)
PTM = 40
GPIO.setup(PTM,GPIO.IN)

while True:
    k = GPIO.input(PTM)
    print("OKUDUGUM DEGER = ",end="")
    print(k)

