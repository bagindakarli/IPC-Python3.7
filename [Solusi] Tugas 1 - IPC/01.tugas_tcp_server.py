# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP binding  yang akan digunakan 
TCP_IP = '192.168.0.107'

# definisikan port number binding  yang akan digunakan 
TCP_PORT = 8080

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024  

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan bind
s.bind((TCP_IP, TCP_PORT))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(1)

# lakukan loop forever
while 1:
	# menerima koneksi
    conn, addr = s.accept()
	
	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
    print ('Alamat koneksi:', addr)
	
	# menerima data berdasarkan ukuran buffer
    data = conn.recv(BUFFER_SIZE)
	
	# menampilkan pesan yang diterima oleh server menggunakan print
    print ("Pesan diterima:", data.decode())
	
	# mengirim kembali data yang diterima dari client kepada client
    conn.send(data)

# tutup koneksi	
conn.close()
