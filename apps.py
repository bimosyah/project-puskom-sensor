import Adafruit_DHT
import requests 
import time
from twilio.rest import Client
from nomer import nomer_hp
from api import API_ENDPOINT
from batas_suhu import suhu_atas,suhu_bawah
# Inisialisasi sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 14

# TWILIO
account_sid = "AC33c4222305503c7e736fb7a42e6b08be"
auth_token  = "0e278cc19e9b9c89ca3139048119e1c5"
client = Client(account_sid, auth_token)
nomer_tujuan = nomer_hp
nomer_pengirim ="+12029294009"

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))        
        #post suhu ke server

        data = {'suhu':"{0:0.1f}".format(temperature),'keterangan':""}
        r = requests.post(url = API_ENDPOINT, data = data)

	if float(temperature) < float(suhu_bawah):	
	    message = client.messages.create(to= nomer_tujuan,from_= nomer_pengirim,body="Suhu server {0:0.1f} perlu segera dicek.".format(temperature))
            print("suhu rendah")
	    #print(temperature)
            #print(float(suhu_bawah))
	if float(temperature) > float(suhu_atas):	
	    message = client.messages.create(to= nomer_tujuan,from_= nomer_pengirim,body="Suhu server {0:0.1f} perlu segera dicek.".format(temperature))
            print("suhu naik")
	    #print(temperature)
            #print(float(suhu_atas))

    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(3600)

