import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import sched, time
import requests
import http.client

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
     conn = http.client.HTTPSConnection("firestore.googleapis.com")
     payload = ''
     headers = {}
     conn.request("GET", "/v1/projects/inlaid-particle-296016/databases/(default)/documents/c/doc1?key=AIzaSyCCIHwUPFBFve6bjRrkclHmGpoNfsvy2sM", payload, headers)
     res = conn.getresponse()
     data = res.read()
     #print(data.decode("utf-8"))
    #print("Doing stuff...")
    #msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': data.decode("utf-8")}, ("gammvert/pithiviers/BBB", "bbbbbbNEW HANID", 0, False)]
     client.publish("gammvert/pithiviers/AAA", data.decode("utf-8"))  
    # do your stuff
     s.enter(1, 1, do_something, (sc,))

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
s.enter(5, 1, do_something, (s,))
s.run()




 


 
