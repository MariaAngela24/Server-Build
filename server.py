import socket

NEWLINE = "\r\n"

RESPONSE = """
HTTP/1.1 200 OK

<h1>My web page</h1>
"""
RESPONSE = NEWLINE.join(RESPONSE.strip().split("\n"))


def server():
    s = socket.socket()
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(('localhost', 10000))
    s.listen(1)

    num = 0

    while True:
        c, a = s.accept()
        print "Connection from ", a
        num += 1

        valid = False
        buf = ""
        #infinite loop
        while True:
            data = c.recv(10)
            if not data:
                break

            buf += data

            if NEWLINE + NEWLINE in buf:
                valid = True
                break
            
        if valid:
            r = RESPONSE + NEWLINE + "<marquee>I have received %s connections</marquee>" % num
            c.send(r)
        else:
            print "invalid request"
        c.close()

if __name__ == '__main__':
    print "Listening..."
    server()

"""
GET / HTTP/1.1
Headers: blah
Headers: blah

\r\n\r\n

HTTP/1.1 200 OK

Hello!
"""