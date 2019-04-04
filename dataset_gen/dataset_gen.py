from server_class import Server 
from _thread import *
import threading
import sys

print_lock = threading.Lock()

def send_msg(server, file_name):
    while True:
        file_server = open(file_name + "_server.txt", "a")
        msg = input("\n")
        server.send_msg(msg)
        file_server.write(msg + "\n")
        file_server.close()
        
def recieve_msg(server, file_name):
    while True:
        file_client = open(file_name + "_client.txt", "a")
        msg = server.recieve_msg()
        if msg == "Nan":
            print_lock.release()
            file_client.close()
            sys.exit()
        print("Client: " + msg)
        file_client.write(msg)
        file_client.close()
    

def chat(server, file_name):
    while True:
        print_lock.acquire()

        start_new_thread(send_msg,(server,file_name))
        start_new_thread(recieve_msg,(server, file_name))

def main():
    host = '10.145.234.243'
    port = 2003

    file_name = "Siddhant_Rajat_Happy" #<Server>_<Client>_<Emotion of the client>
    server = Server(host, port)
    server.initialise_connection()
    chat(server, file_name)


if __name__ =='__main__':
    main()
        




