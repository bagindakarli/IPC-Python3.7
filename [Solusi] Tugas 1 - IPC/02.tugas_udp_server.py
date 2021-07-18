# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP bind dari server
UDP_IP = "127.0.0.1"

# definisikan port number untuk bind dari server
UDP_PORT = 5005

# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# lakukan bind
sock.bind((UDP_IP, UDP_PORT))

# loop forever
while True:
    # terima pesan dari client
    data, addr = sock.recvfrom(1024)
    
    # menampilkan hasil pesan dari client
    #print (addr)
    pesan = "pesan diterima dari " + str(addr) + " berisi pesan: " + data.decode()
    print (pesan)
