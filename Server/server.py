import socket
import threading
import time
import udp_server
from datetime import datetime

class serverUDP(udp_server.UDPServer):
    def __init__(self,host,port):
        super().__init__(host,port)
        self.socket_lock = threading.Lock()

    def handle_request(self, data, endereco):
        posicao = data

        self.printwt(f'[ O cliente {endereco} está na posição {posicao}]')

        resposta = '{"comando":"comando_","x":0,"y":0}'
        with self.socket_lock:
            self.sock.sendto(resposta.encode('utf-8'), endereco)

    def receberClientes(self):
        try:
            while True:
                try:
                    cliente, endereco = self.sock.recvfrom(1024)
                    c_thread = threading.Thread(target= self.handle_requests, args=(cliente,endereco))
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