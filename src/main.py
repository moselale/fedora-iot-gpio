import os

import gpiod
import time
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

pinSbarra = 17
pinScorrevole = 27
pinPortone = 22

def getOpposite(val):
    if val == 0:
        return 1
    else:
        return 0

class Sbarra(Resource):
    def get(self):
        try:
            sbarra.request(consumer='sbarra', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
        except:
            print()
    #    sbarra.set_values([getOpposite(sbarra.get_values()[0])])
        sbarra.set_values([0])
        time.sleep(4)
        sbarra.set_values([1])
        return {'sbarra': "yes"}

class Scorrevole(Resource):
    def get(self):
        try:
            scorrevole.request(consumer='scorrevole', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
        except:
            print()
    #    scorrevole.set_values([getOpposite(scorrevole.get_values()[0])])
        scorrevole.set_values([0])
        time.sleep(4)
        scorrevole.set_values([1])
        return {'scorrevole': "yes"}

class Portone(Resource):
    def get(self):
        try:
            portone.request(consumer='portone', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
        except:
            print()
    #    portone.set_values([getOpposite(portone.get_values()[0])])
        portone.set_values([0])
        time.sleep(4)
        portone.set_values([1])
        return {'portone': "yes"}


api.add_resource(Sbarra, '/sbarra')
api.add_resource(Scorrevole, '/scorrevole')
api.add_resource(Portone, '/portone')


print(__name__)
if __name__ == '__main__':
    print("Starting process...")
    
    chip = gpiod.Chip('gpiochip0')
    
    sbarra = chip.get_lines([17])
    scorrevole = chip.get_lines([27])
    portone = chip.get_lines([22])

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)