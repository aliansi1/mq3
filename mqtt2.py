import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import sched, time
import requests
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
     url = 'https://api.jsonbin.io/b/6137cac49548541c29add347/latest'
     headers = {
    'X-Master-Key': '$2b$10$5WeMJUgq7AAwROqsNxc68.TdR8UNsxB8VWxBZ6Fs3siF0LF0we8tm'
    }
    req = requests.get(url, json=None, headers=headers)
    print(req.text)
    #print("Doing stuff...")
    #msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': req.text}, ("gammvert/pithiviers/BBB", "bbbbbbNEW HANID", 0, False)]
    client.publish("gammvert/pithiviers/AAA", req.text)  
    # do your stuff
    s.enter(1, 1, do_something, (sc,))

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
s.enter(3, 1, do_something, (s,))
s.run()




 
