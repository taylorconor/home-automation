from bottle import route, run
import time
import plug

@route('/home/lights/on')
def index():
    plug.turn_on()

@route('/home/lights/off')
def index():
    plug.turn_off()

if __name__ == "__main__":
    while True:
        run(host="0.0.0.0", port=8080, quiet=True)
        time.sleep(1)
