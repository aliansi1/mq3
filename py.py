import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import streamlit as st 
import sys

def do_something(sc): 
    #print("Doing stuff...")
    msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': "aaaaaaaa"}, ("gammvert/pithiviers/BBB", "bbbbbb", 0, False)]
    publish.multiple(msgs, hostname="broker.mqtt-dashboard.com")  
    # do your stuff
    
@view_config(route_name='newusers', renderer='json')
def newusers(self):
    name =  str(self.request.POST.get('ee'))
    st.write(name)
    return name 
 

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
 


 
