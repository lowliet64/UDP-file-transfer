import socket 
import sys
from pynput.keyboard import Key,Listener
import json
from threading import Thread
import os


    
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
HOST ='127.0.0.1'
PORT = 8081
BUFFER_SIZE = 1024
ADDR = (HOST,PORT)

# dados de posição e comando que serão enviados para o servidor
data = {'comand':'center', 'x':0 ,'y':0}

def on_press(key):
   
    if(key==Key.down):
        os.system('cls')
        print("voce pressionou :", key)
        data['comand']='down'
        client_socket.sendto(json.dumps(data).encode("utf-8"),ADDR)
        msg ,address = client_socket.recvfrom(2048)
        if msg:
            try:
                msg = json.loads(msg.decode("utf-8"))
                data['x'] =msg['x']
                data['y'] =msg['y']
                print(type(msg), msg)
            except:
                print("pacote corrompido") 
                    
    if(key==Key.up):
        os.system('cls')
        print("voce pressionou :",key)
        data['comand']='up'
        client_socket.sendto(json.dumps(data).encode("utf-8"),ADDR)
        msg ,address = client_socket.recvfrom(2048)
        if msg:
            try:
                msg= json.loads(msg.decode("utf-8"))
                data['x'] =msg['x']
                data['y'] =msg['y']
                print(type(msg), msg)
            except:
                print("pacote corrompido") 
        
    elif(key==Key.left):
        os.system('cls')
        print("voce pressionou :", key)
        data['comand']='left'
        client_socket.sendto(json.dumps(data).encode("utf-8"),ADDR)
        msg ,address = client_socket.recvfrom(2048)
        if msg:
            try:
                msg = json.loads(msg.decode("utf-8"))
                data['x'] =msg['x']
                data['y'] =msg['y']
                print(type(msg), msg)
            except:
                print("pacote corrompido") 
    elif(key==Key.right):
        os.system('cls')
        print("voce pressionou :",key)
        data['comand']='right'
        client_socket.sendto(json.dumps(data).encode("utf-8"),ADDR)
        msg ,address = client_socket.recvfrom(2048)
        if msg:
            try:
                msg= json.loads(msg.decode("utf-8"))
                data['x'] = msg['x']
                data['y'] = msg['y']
                print(type(msg), msg)
            except:
                print("pacote corrompido") 

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
 
 


    

            
