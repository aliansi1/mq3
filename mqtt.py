import paho.mqtt.client as mqtt
import streamlit as st

#import context  # Ensures paho is in PYTHONPATH



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("gammvert/pithiviers/AAA")
    client.subscribe("gammvert/pithiviers/BBB")
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   st.write(msg.topic+" التوبك وصل ياشباب"+str(msg.payload))
   
 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.mqtt-dashboard.com", 1883, 60)
client.loop_forever()

 
