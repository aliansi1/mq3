import simplejson
import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import streamlit as st 
import requests

def do_something(sc): 
    #print("Doing stuff...")
    msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': "aaaaaaaa"}, ("gammvert/pithiviers/BBB", "bbbbbb", 0, False)]
    publish.multiple(msgs, hostname="broker.mqtt-dashboard.com")  
    # do your stuff
    st.write( simplejson.loads(request.POST.get('data')) )

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
 


 
