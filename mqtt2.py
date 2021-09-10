import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import sched, time
import http.client

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
   #  conn = http.client.HTTPSConnection("firestore.googleapis.com")
    # payload = ''
    # headers = {}
    # conn.request("GET", "/v1/projects/inlaid-particle-296016/databases/(default)/documents/c/doc1?key=AIzaSyCCIHwUPFBFve6bjRrkclHmGpoNfsvy2sM", payload, headers)
    # res = conn.getresponse()
    # data = res.read()
     #print(data.decode("utf-8"))
    #print("Doing stuff...")
    #msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': data.decode("utf-8")}, ("gammvert/pithiviers/BBB", "bbbbbbNEW HANID", 0, False)]
  conn = http.client.HTTPSConnection("mikmon2.000webhostapp.com")
  payload = ''
  headers = {}
  conn.request("GET", "/LGLS7752a1d2e62.php", payload, headers)
  res = conn.getresponse()
  data = res.read()
  #print(data.decode("utf-8"))
  ini_string = "{
  'LGLS7752a1d2e6':{ 
  'active':'"+data.decode("utf-8")+"',  'brgtotal':'9999'
  }
  }"
  client.publish("send/to/LGLS7752a1d2e6palm", ini_string)  
  print(data.decode("utf-8"))
  s.enter(1, 1, do_something, (sc,))

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
s.enter(7, 1, do_something, (s,))
s.run()




 


 
