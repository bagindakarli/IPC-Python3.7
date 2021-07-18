# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
UDP_IP = "127.0.0.1"

# definisikan target port number server yang akan dituju
UDP_PORT = 5005

# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

print ("target IP:", UDP_IP)
print ("target port:", UDP_PORT)

# lakukan loop 10 kali
for x in range (10):
    # definisikan pesan yang akan dikirim
    PESAN = "Hello world "+ str(x)
    print ("pesan:", PESAN)
    
    # kirim pesan    
    sock.sendto(PESAN.encode(), (UDP_IP, UDP_PORT))





