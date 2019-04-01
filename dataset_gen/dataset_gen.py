from server_class import Server 
from _thread import *
import threading
import sys

print_lock = threading.Lock()

def send_msg(server, file_name):
    while True:
        file_server = open("data/" + file_name + "_server.txt", "a")
        file_data = open("data/" + file_name + "_data.txt","a")
        msg = input("\n")
        server.send_msg(msg)
        file_server.write(msg + "\n")
        file_data.write(msg + "\n")
        file_server.close()
        file_data.close()
        
def recieve_msg(server, file_name):
    while True:
        file_client = open("data/" + file_name + "_client.txt", "a")
        file_data = open("data/" + file_name + "_data.txt", "a")
        msg = server.recieve_msg()
        if msg == "Nan":
            print_lock.release()
            file_client.close()
            file_data.close()
            sys.exit()
        print("Client: " + msg)
        file_client.write(msg)
        file_data.write("> " + msg)
        file_data.close()
        file_client.close()
    

def chat(server, file_name):
    while True:
        print_lock.acquire()

        start_new_thread(send_msg,(server,file_name))
        start_new_thread(recieve_msg,(server, file_name))

def main():
    host = 'localhost'
    port = 2003

    file_name = "Siddhant_Rajat_Happy" #<Server>_<Client>_<Emotion of the client>
    server = Server(host, port)
    server.initialise_connection()
    chat(server, file_name)


if __name__ =='__main__':
    main()
        




