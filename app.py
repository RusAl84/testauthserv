from flask import Flask, request, jsonify
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)
# global ListOfColors
ListOfColors = []
SecretKey=['green','blue','red']
currentKey=['','','','']

@app.route('/')
def dafault_route():
    return 'Auth server '

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
    ListOfColors.append('red')
    ListOfColors.append('blue')
    ListOfColors.append('green')
    app.run(host="0.0.0.0")