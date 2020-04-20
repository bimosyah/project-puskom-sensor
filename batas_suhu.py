from api import API_BATAS_SUHU
import requests

response = requests.get(API_BATAS_SUHU)
suhu = response.json()
suhu_atas = suhu['suhu_atas']
suhu_bawah = suhu['suhu_bawah']
#print(suhu_atas +" " +suhu_bawah)

