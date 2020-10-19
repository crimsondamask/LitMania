import socket

SERVER = '192.168.137.17'
PORT = 52363

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn :
        print('Connected to', addr)
        TXTFILE = open('sample.txt', 'a')
        while True :
            data = conn.recv(32)
            SAMPLE = data.decode()
            TXTFILE.write(SAMPLE)
        TXTFILE.close()
