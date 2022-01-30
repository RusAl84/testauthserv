from flask import Flask, request, jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

ListOfColors=['maroon',
    'red',
    'purple',
    'fuchsia',
    'green',
    'olive',
    'yellow',
    'navy',
    'blue',
    'teal',
    'aqua',
    'white',
    'black',
    'gray',
    'orange',
    'aquamarine']	


SecretKey=['red','blue','green','black']
currentKey=[]


@app.route('/')
def dafault_route():
    StrColors=""
    for color in ListOfColors:
        StrColors += " <br> " + color
    return 'Auth server <br>  <br> ListOfColors: ' + StrColors

# отправка сообщений
@app.route("/sendColor", methods=['POST'])
def sendColor():
    msg=""
    msg = request.json
    color = msg['color']
    print(color)
    currentKey.insert(0,color)
    print(currentKey)
    if currentKey[0]==SecretKey[0] and currentKey[1]==SecretKey[1] and currentKey[2]==SecretKey[2]:
        print("isGrated")
        return "isGrated",200

    return f"й: {(msg)} ", 200

# получение цветов
@app.route("/color/<int:id>")
def GetMessage(id):
    print(id)
    if id >= 0 and id < len(ListOfColors):
        print(ListOfColors[id])
        return ListOfColors[id], 200
    else:
        return "Not found", 400

@app.route('/shufle')
def status():
    random.shuffle(ListOfColors)
    allcolors = ""
    for color in ListOfColors:
        allcolors += "<br> " + color
    return allcolors

if __name__ == '__main__':
    random.shuffle(ListOfColors)
    app.run(host="0.0.0.0")