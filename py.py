import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import streamlit as st 
from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def refresh():
    st.write("okk")
    params = {
        'thing1': request.values.get('ee'),
        'thing2': request.get_json().get('55')
    }
    st.write(params)
    return json.dumps(params)



   
 

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
app.run() 


 
