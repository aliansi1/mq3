import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import streamlit as st 
import requests as rq

@py.route('/do_something', methods=['GET', 'POST'])
def do_something(sc): 
    #print("Doing stuff...")
    msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': "aaaaaaaa"}, ("gammvert/pithiviers/BBB", "bbbbbb", 0, False)]
    publish.multiple(msgs, hostname="broker.mqtt-dashboard.com")  
    #if rq.method == 'POST':  #this block is only entered when the form is submitted
    st.write("xxx")
 

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
 


 
