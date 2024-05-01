import certifi
import paho.mqtt.client as mqtt
import ssl
import serial
import time

#Callback on connection
def on_connect(client, userdata, flags, rc, properties):
    print(f'Connected (Result: {rc})')
    client.subscribe('arduino')
    client.publish('arduino',payload=userdata['ultrasonic_val'])

# Callback when message is received
def on_message(client, userdata, msg):
    print(f'Message received on topic: {msg.topic}. Message: {msg.payload}')

def write_read():
    data = arduino.readline()
    #print(f"{data} - {type(data.decode('utf-8'))}")
    return data

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)

# Enter your password here
client.username_pw_set('solace-cloud-client', 'vhfvoutofgngdva5q7da4q5o72')
# Use the host and port from Solace Cloud without the protocol
# ex. "ssl://yoururl.messaging.solace.cloud:8883" becomes "yoururl.messaging.solace.cloud"
client.connect('mr-connection-vhne8njdq44.messaging.solace.cloud',8883,60)

while True:
    ultrasonic_val = write_read().decode('utf-8')
    if len(str(ultrasonic_val))>0:
        #print(ultrasonic_val)
        client.user_data_set({'ultrasonic_val':ultrasonic_val})
        client.on_connect = on_connect
        client.on_message = on_message
        client.loop_start()

com.unity.nuget.newtonsoft-json


