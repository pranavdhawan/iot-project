import serial.tools.list_ports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
cred = credentials.Certificate('sourceJSONFILE.json')
 
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://arduino-cb30c-default-rtdb.firebaseio.com/'
})
 
ref = db.reference('py/')
users_ref = ref.child('users/')
users_ref.set({
    'Arduino Reading': {}
})
 
 
 
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
 
serialInst.baudrate = 9600
serialInst.port = "/dev/cu.usbmodem101"
serialInst.open()
 
f = 0
 
while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        f = f + 1
        hopper_ref = users_ref.child('Arduino Reading')
        hopper_ref.update({
            'Arduino Reading': packet.decode('utf')
        })
        # print("Sensor reading: ", packet.decode('utf'))
 
