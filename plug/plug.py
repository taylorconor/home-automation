import socket
import sys
import base64

ON_PAYLOAD = "AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu36Lfog=="
OFF_PAYLOAD = "AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu3qPeow=="
HS100_PORT = 9999

socket.setdefaulttimeout(2)

def send(ip, port, payload):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(base64.b64decode(payload))
    s.close()

def plugs():
    return [line.split()[1] for line in open("/etc/hosts", 'r') if 'hs100' in line]

def turn_on():
    for name in plugs():
        send(name, HS100_PORT, ON_PAYLOAD)

def turn_off():
    for name in plugs():
        send(name, HS100_PORT, OFF_PAYLOAD)

        
if __name__ == "__main__":        
    if len(sys.argv) is not 2 or sys.argv[1] not in ["on", "off"]:
        print "Usage:\n" + sys.argv[0] + " (on|off)\n"
    elif sys.argv[1] == "on":
        turn_on()
    else:
        turn_off()
