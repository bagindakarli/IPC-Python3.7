# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
TCP_IP = '127.0.0.1'

# definisikan port dari server yang akan terhubung
TCP_PORT = 5005

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024

# definisikan pesan yang akan disampaikan
PESAN = "Hello World!"

# buat socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((TCP_IP, TCP_PORT))

# kirim pesan ke server
s.send(PESAN.encode())

# terima pesan dari server
data = s.recv(BUFFER_SIZE)

# tampilkan pesan/reply dari server
print ("pesan diterima:", data.decode())

# tutup koneksi
s.close()

