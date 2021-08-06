import simplejson
import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import streamlit as st 
import requests as request
import sys

def do_something(sc): 
    #print("Doing stuff...")
    msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': "aaaaaaaa"}, ("gammvert/pithiviers/BBB", "bbbbbb", 0, False)]
    publish.multiple(msgs, hostname="broker.mqtt-dashboard.com")  
    # do your stuff
    POST={}
    args=sys.stdin.read().split('&')
    for arg in args:
    st.write(arg.split('=') )
 

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
 


 
