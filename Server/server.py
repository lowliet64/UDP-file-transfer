import socket
import threading
import time
import udp_server
import json
from datetime import datetime

class serverUDP(udp_server.UDPServer):
    def __init__(self,host,port):
        super().__init__(host,port)
        self.socket_lock = threading.Lock()

    def handle_request(self, data, endereco):
        posicao = json.loads(data)

        

        if posicao['comand'] == 'up':
            posicao['y'] += 1
        elif posicao['comand'] == 'down':
            posicao['y'] -= 1
        elif posicao['comand'] == 'right':
            posicao['x'] += 1
        elif posicao['comand'] == 'left':
            posicao['x'] -= 1
        x = posicao['x']
        y = posicao['y']
        self.printwt(f'[ O cliente {endereco} está na posição X:{x} Y:{y}]')
        
        with self.socket_lock:
            self.sock.sendto(json.dumps(posicao).encode("utf-8"), endereco)

    def receberClientes(self):
        try:
            while True:
                try:
                    cliente, endereco = self.sock.recvfrom(1024)
                    c_thread = threading.Thread(target= self.handle_request, args=(cliente,endereco))
                    c_thread.daemon = True
                    c_thread.start()
                except OSError as err:
                    self.printwt(err)
        except KeyboardInterrupt:
            self.shutdown_server()

def main():
    IPlocal = "127.0.0.1"
    Porta = 8081

    serverGPS = serverUDP(IPlocal, Porta)
    serverGPS.configure_server()
    serverGPS.receberClientes()

if __name__ == '__main__':
    main()