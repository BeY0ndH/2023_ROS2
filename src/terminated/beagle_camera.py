'''

import roboidai as ai
import roboidai.lab.ko as lab
cam = ai.Camera('ip0', flip='h', square=True)
#lab.collect_image(cam, '/home/k/DICE1')
#lab.collect_image(cam, '/home/k/DICE2')
lab.collect_image(cam, '/home/k/DICE5')
#lab.collect_image(cam, '/home/k/DICE4')
#lab.collect_image(cam, '/home/k/DICE5')
#lab.collect_image(cam, '/home/k/DICE6')

#ai.test_camera()   

'''
'''
import roboidai as ai

tmi = ai.TmImage()
tmi.load_model('/home/k/DICE/converted_keras')

cam = ai.Camera('ip0', flip='h', square=True)
cam.count_down(3)

while True :

    image = cam.read()
    if tmi.predict(image) :
        label = tmi.get_label()
        conf = tmi.get_conf()
        if conf > 0.85 :
            print(label,type(label),conf)

    cam.show(image)
    if cam.check_key() == 'esc' : break

'''

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import roboidai as ai

tmi = ai.TmImage()
tmi.load_model('/home/k/DICE/converted_keras')

cam = ai.Camera('ip0',square=True)

print("countdown on")
cam.count_down(5)
print("countdown off =")


 
image = cam.read()
if tmi.predict(image):
    label = tmi.get_label()
    conf = tmi.get_conf()
    if conf > 0.8   :
        print(label, conf)
    

    cam.show(image)
   
    


