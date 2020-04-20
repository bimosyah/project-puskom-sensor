import time, sys
import RPi.GPIO as GPIO
from twilio.rest import Client
from nomer import nomer_hp
from api import API_ENDPOINT

# TWILIO
account_sid = "AC33c4222305503c7e736fb7a42e6b08be"
auth_token  = "0e278cc19e9b9c89ca3139048119e1c5"
client = Client(account_sid, auth_token)
nomor_pengirim ="+12029294009"
nomor_tujuan = nomer_hp
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
    print('Sensor detected action!')
    message = client.messages.create(to= nomor_tujuan,from_= nomor_pengirim,body="Gas terdeksi, perlu segera dicek.")
   
    return
 
GPIO.add_event_detect(11, GPIO.RISING)
GPIO.add_event_callback(11, action)
 
try:
    while True:
        print('alive')
        time.sleep(3600)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()

