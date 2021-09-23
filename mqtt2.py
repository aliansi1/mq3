import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import sched, time
import requests
 

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
  try:
   #  conn = http.client.HTTPSConnection("firestore.googleapis.com")
    # payload = ''
    # headers = {}
    # conn.request("GET", "/v1/projects/inlaid-particle-296016/databases/(default)/documents/c/doc1?key=AIzaSyCCIHwUPFBFve6bjRrkclHmGpoNfsvy2sM", payload, headers)
    # res = conn.getresponse()
    # data = res.read()
     #print(data.decode("utf-8"))
    #print("Doing stuff...")
    #msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': data.decode("utf-8")}, ("gammvert/pithiviers/BBB", "bbbbbbNEW HANID", 0, False)]
  
   url = "https://mikmon2.000webhostapp.com/getmikdata.php"
   payload={}
   headers = {}
   response = requests.request("GET", url, headers=headers, data=payload)
   #data = json.loads("{data:"+response.text.decode("utf-8")+"}")
   #print(response.text)
   #for i in data['data']:
   msgs =response.text.decode("utf-8") #[{'topic': str(i["hs"]), 'payload': i},{'topic': "gammvert/pithiviers/BBB", 'payload': "{data:{  'active':"+str(i["active"])+"',  'brgtotal':'9999'  }  }"} ]
    #[{"hs":"2B22ECF8A532234696DB27E3768B72FA","topc":"FED472E99D2C9773501BB58CBF2FDD2BC3CF228100D494AB4A70C4367B808B28","str":";all;queue2;","active":"19","LAN":"0","WAN":"0","WAN1":"0","WAN2":"0","WAN3":"0","WAN4":"0","WAN5":"0","WAN6":"0","WAN7":"0","WAN8":"0","WAN9":"0","WAN10":"0","WAN11":"0","WAN12":"0","lines":"0","regidtred":"0","bound1":"0","bound2":"0","rate":"0","speedauto":"0"},{"hs":"2B22ECF8A532234696DB27E3768B72FA","topc":"2B22ECF8A532234696DB27E3768B72FA","str":"0","active":"19","LAN":"0","WAN":"0","WAN1":"0","WAN2":"0","WAN3":"0","WAN4":"0","WAN5":"0","WAN6":"0","WAN7":"0","WAN8":"0","WAN9":"0","WAN10":"0","WAN11":"0","WAN12":"0","lines":"0","regidtred":"0","bound1":"0","bound2":"0","rate":"0","speedauto":"0"}]
        
   ini_string = "{ 'LGLS7752a1d2e6':{  'active':'"+response.text+"',  'brgtotal':'9999'  }  }"
   publish.multiple(msgs, hostname="broker.mqtt-dashboard.com", 1883)  
   client.publish("send/to/LGLS7752a1d2e6palm", ini_string)  
   client.publish("send/to/FED472E99D2C9773501BB58CBF2FDD2BC3CF228100D494AB4A70C4367B808B28", ini_string)  
   #print(data.decode("utf-8"))
   s.enter(30, 1, do_something, (sc,))
  except:
   x=1

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
s.enter(2, 1, do_something, (s,))
s.run()
