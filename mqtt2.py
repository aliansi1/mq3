import paho.mqtt.client as mqtt
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    #print("Doing stuff...")
    msgs = [{'topic': "gammvert/pithiviers/AAA", 'payload': "aaaaaaaa"}, ("gammvert/pithiviers/BBB", "bbbbbb", 0, False)]
    publish.multiple(msgs, hostname="broker.mqtt-dashboard.com")  
    # do your stuff
    s.enter(1, 1, do_something, (sc,))

client = mqtt.Client()
client.connect("broker.mqtt-dashboard.com", 1883, 60)    
s.enter(3, 1, do_something, (s,))
s.run()




 