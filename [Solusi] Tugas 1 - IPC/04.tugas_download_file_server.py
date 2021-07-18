# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
TCP_IP = '127.0.0.1'

# definisikan port untuk binding
TCP_PORT = 5005

# definisikan ukuran buffer untuk menerima pesan
BUFFER_SIZE = 4096  

# buat socket (bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding ke IP dan port
s.bind((TCP_IP, TCP_PORT))

# lakukan listen
s.listen(1)

#  siap menerima koneksi
conn, addr = s.accept()
print ('Connection address:', addr)

# buka file bernama "file_didownload.txt
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open("download.txt", "rb") 

try:
    # baca file tersebut sebesar buffer 
    byte = f.read(BUFFER_SIZE)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file dari server ke client
        conn.send(byte)
        
        # baca sisa file hingga EOF
        byte = f.read(BUFFER_SIZE)
        
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup socket
s.close()

# tutup koneksi
conn.close()
