#!/usr/bin/env python
import socket
import threading
import sys
import time
import datetime

HOST = 'localhost'
PORT = 12000
puan = [0, 0, 0, 0]
soru_sayisi = int(raw_input("soru sayisi belirleyiniz: "))
filename = raw_input("soru dosyasi giriniz: ")
t = [0, 0, 0, 0]
f = open(filename, 'r')
isDone = False

def yarisma(client_sayisi, oyuncu_num, sorular, cevaplar):
    global puan
    global f
    global t
    global isDone
    client_sayisi[oyuncu_num].sendall("S\n")
    time.sleep(0.1)
    client_sayisi[oyuncu_num].sendall(sorular+"\n")
    time.sleep(0.1)
    data = client_sayisi[oyuncu_num].recv(1024)
    t[oyuncu_num] = datetime.datetime.now()
    if (not isDone) and (cevaplar == data + '\n'):
        puan[oyuncu_num] += 10
        isDone = not isDone
        client_sayisi[oyuncu_num].sendall("Dogru cevap!\n")
        time.sleep(0.1)
    else:
        if cevaplar == data + '\n':
            client_sayisi[oyuncu_num].sendall("Gec kaldiniz!\n")
            time.sleep(0.1)
        else:
            client_sayisi[oyuncu_num].sendall("Yanlis cevap!\n")
            time.sleep(0.1)

def puanGoster(client_sayisi):
    global puan
    for i, conn in enumerate(client_sayisi):
        conn.sendall("P\n")
        time.sleep(0.1)
        conn.sendall("Puaniniz: "+str(puan[i])+"\n")
        time.sleep(0.1)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(4)

print "Oyuncular bekleniyor..."
(conn1, addr) = server.accept()
print "Oyuncu 1 baglandi"
(conn2, addr) = server.accept()
print "Oyuncu 2 baglandi "
(conn3, addr) = server.accept()
print "Oyuncu 3 baglandi "
(conn4, addr) = server.accept()
print "Oyuncu 4 baglandi "

client_sayisi = [conn1, conn2, conn3, conn4]
conn1.sendall("C\n")
time.sleep(0.1)
conn1.sendall("Oyuncu 1 olarak katildiniz\n")
time.sleep(0.1)
conn2.sendall("C\n")
time.sleep(0.1)
conn2.sendall("Oyuncu 2 olarak katildiniz\n")
time.sleep(0.1)
conn3.sendall("C\n")
time.sleep(0.1)
conn3.sendall("Oyuncu 3 olarak katildiniz\n")
time.sleep(0.1)
conn4.sendall("C\n")
time.sleep(0.1)
conn4.sendall("Oyuncu 4 olarak katildiniz\n")
time.sleep(0.1)


for soruNo in range(soru_sayisi):
    conn1.sendall("C\n")
    time.sleep(0.1)
    conn1.sendall("Soru "+str(soruNo+1)+"\n")
    time.sleep(0.1)
    conn2.sendall("C\n")
    time.sleep(0.1)
    conn2.sendall("Soru "+str(soruNo+1)+"\n")
    time.sleep(0.1)
    conn3.sendall("C\n")
    time.sleep(0.1)
    conn3.sendall("Soru "+str(soruNo+1)+"\n")
    time.sleep(0.1)
    conn4.sendall("C\n")
    time.sleep(0.1)
    conn4.sendall("Soru "+str(soruNo+1)+"\n")
    time.sleep(0.1)

    sorular = f.readline()
    cevaplar = f.readline()
    isDone = False
    
    oyuncu1 = threading.Thread(target = yarisma, name = "Thread1", args = (client_sayisi, 0, sorular, cevaplar,))
    oyuncu2 = threading.Thread(target = yarisma, name = "Thread2", args = (client_sayisi, 1, sorular, cevaplar,))
    oyuncu3 = threading.Thread(target = yarisma, name = "Thread3", args = (client_sayisi, 2, sorular, cevaplar,))
    oyuncu4 = threading.Thread(target = yarisma, name = "Thread4", args = (client_sayisi, 3, sorular, cevaplar,))
    oyuncu1.start()
    oyuncu2.start()
    oyuncu3.start()    
    oyuncu4.start()
    oyuncu1.join()
    oyuncu2.join()
    oyuncu3.join()    
    oyuncu4.join()
    puanGoster(client_sayisi)

if puan[0] > puan[1] & puan[2] & puan[3]:
    print "Oyuncu 1 kazandi, puan: ", puan
    conn1.sendall("F\n")
    time.sleep(0.1)
    conn1.sendall("KAZANDIN\n")
    time.sleep(0.1)
    conn2.sendall("F\n")
    time.sleep(0.1)
    conn2.sendall("KAYBETTIN\n")
    time.sleep(0.1)
    conn3.sendall("F\n")
    time.sleep(0.1)
    conn3.sendall("KAYBETTIN\n")
    time.sleep(0.1)
    conn4.sendall("F\n")
    time.sleep(0.1)
    conn4.sendall("KAYBETTIN\n")
    time.sleep(0.1)

elif puan[0] & puan[2] & puan[3] < puan[1]:
    print "Oyuncu 2 kazandi, puan: ", puan
    conn2.sendall("F\n")
    time.sleep(0.1)
    conn2.sendall("KAZANDIN\n")
    time.sleep(0.1)
    conn1.sendall("F\n")
    time.sleep(0.1)
    conn1.sendall("KAYBETTIN\n")
    time.sleep(0.1)
    conn3.sendall("F\n")
    time.sleep(0.1)
    conn3.sendall("KAYBETTIN\n")
    time.sleep(0.1)
    conn4.sendall("F\n")
    time.sleep(0.1)
    conn4.sendall("KAYBETTIN\n")
    time.sleep(0.1)

elif puan[0] & puan[1] & puan [3] < puan[2]:
    print "Oyuncu 3 kazandi, puan: ", puan
    conn3.sendall("F\n")
    time.sleep(0.1)
    conn3.sendall("KAZANDIN\n")
    time.sleep(0.1)
    conn1.sendall("F\n")
    time.sleep(0.1)
    conn1.sendall("KAYBETTIN\n")
    time.sleep(0.1)
    conn2.sendall("F\n")
    time.sleep(0.1)
    conn2.sendall("KAYBETTIN\n")
    time.sleep(0.1)
    conn4.sendall("F\n")
    time.sleep(0.1)
    conn4.sendall("KAYBETTIN\n")
    time.sleep(0.1)

elif puan[0] & puan[1] & puan [2] < puan[3]:
    print "Oyuncu 3 kazandi, puan: ", puan
    conn4.sendall("F\n")
    time.sleep(0.1)
    conn4.sendall("KAZANDIN\n")
    time.sleep(0.1)
    conn1.sendall("F\n")
    time.sleep(0.1)
    conn1.sendall("KAYBETTIN\n")
    time.sleep(0.1)
    conn2.sendall("F\n")
    time.sleep(0.1)
    conn2.sendall("KAYBETTIN\n")
    time.sleep(0.1)
    conn3.sendall("F\n")
    time.sleep(0.1)
    conn3.sendall("KAYBETTIN\n")
    time.sleep(0.1)

else:
    print "Berabere, puan: ", puan
    conn1.sendall("F\n")
    time.sleep(0.1)
    conn1.sendall("BERABERE\n")
    time.sleep(0.1)
    conn2.sendall("F\n")
    time.sleep(0.1)
    conn2.sendall("BERABERE\n")
    time.sleep(0.1)
    conn3.sendall("F\n")
    time.sleep(0.1)
    conn3.sendall("BERABERE\n")
    time.sleep(0.1)
    conn4.sendall("F\n")
    time.sleep(0.1)
    conn4.sendall("BERABERE\n")
    time.sleep(0.1)

server.close()
