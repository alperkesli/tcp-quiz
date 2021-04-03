#!/usr/bin/env python
import socket
import sys

def soruSor(server):
    sorular = server.recv(1024)
    print sorular,
    cevaplar = raw_input("Cevap: ")
    while cevaplar not in ['a', 'b', 'c', 'd']:
        print "Gecersiz cevap!"
        cevaplar = raw_input("Cevap: ")
    server.sendall(cevaplar)
    girdi = server.recv(1024)
    print girdi

def puan(server):
    cikti = server.recv(1024)
    print cikti

def final(server):
    cikti = server.recv(1024)
    print cikti


HOST = 'localhost'   
PORT = 12000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

while True:
    sec = server.recv(1024)
    if sec[0] == "S":
        soruSor(server)
    elif sec[0] == "P":
        puan(server)
    elif sec[0] == "F":
        final(server)
        break
    elif sec[0] == "C":
        final(server)
    else:
        print "Gecersiz tercih ", sec
