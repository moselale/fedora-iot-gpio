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

chip = gpiod.Chip('gpiochip0')

# scorrevole = chip.get_lines([27])
# scorrevole.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
# portone = chip.get_lines([22])
# portone.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
# i = 4

def getOpposite(val):
    if val == 0:
        return 1
    else:
        return 0

# while i>0:
#     sbarra.set_values([getOpposite(sbarra.get_values()[0])])
#     print(getOpposite(sbarra.get_values()[0]))
#     scorrevole.set_values([getOpposite(scorrevole.get_values()[0])])
#     portone.set_values([getOpposite(portone.get_values()[0])])
#     i = i-1
#     time.sleep(1)


class Sbarra(Resource):
    def get(self):
        # if not sbarraRequested:
        #     sbarraRequested = True
        sbarra.set_values([getOpposite(sbarra.get_values()[0])])
        return {'oppened': "yes"}

api.add_resource(Sbarra, '/sbarra')
# api.add_resource(PollutionResource, '/pollution')
# api.add_resource(GasResource, '/gas')

print(__name__)
if __name__ == '__main__':
    print("Starting process...")
    
    sbarra = chip.get_lines([17])
    sbarra.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
    # sbarraRequested = False
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)