# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
TCP_IP = "127.0.0.1"

# definisikan port number proses di server
TCP_PORT = 5005

# definisikan ukuran buffer untuk mengirim
BUFFER_SIZE = 4096

# buat socket (apakah bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server
s.connect((TCP_IP, TCP_PORT))

# buka file bernama "file_diupload.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open("upload.txt", "rb") 

try:
    # baca file tersebut sebesar buffer 
    byte = f.read(BUFFER_SIZE)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file
        s.send(byte)
        
        # baca sisa file hingga EOF
        byte = f.read(BUFFER_SIZE)
        #print(byte)
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup koneksi setelah file terkirim
s.close()
