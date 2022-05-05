import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import sched, time
import requests
import json 

s = sched.scheduler(time.time, time.sleep)
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
  
def do_something(): 
  #try:
 
  
   url = "https://mikmon2.000webhostapp.com/getregmikdata.php?hs=39703D78AE9C788C483B30B4D7EE47F7"
   payload={}
   headers = {}
   response = requests.request("GET", url, headers=headers, data=payload)
 
   data = json.loads("{\"data\":"+response.text+"}")

   entry1List = []
   print(response.text)
   client = mqtt.Client()
   client.connect("broker.mqtt-dashboard.com", 1883, 30) 
   for i in data['data']:
      client.subscribe("shadmik/reg/mikmon/v1/"+str(i["dvc"]))
      print("shadmik/reg/mikmon/v1/"+str(i["dvc"]))
      entry1List.append({'topic': "shadmik/reg/mikmon/v1/"+str(i["dvc"]), 'payload':  str(i)})
      
  
   publish.multiple(entry1List, hostname="broker.mqtt-dashboard.com")  
 # except:
  # x=1

   
do_something()
#s.enter(2, 1, do_something, (s,))
#s.run()
