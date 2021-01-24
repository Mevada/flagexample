from flask import Flask,render_template,request

flag = {} # Flag

app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/action',methods=['POST'])
def action():
    senderID = request.form.get('senderID')
    message = request.form.get('message')

    flag[senderID] = True
    
    return render_template('main.html',senderID = senderID,message=message,flag=flag)

@app.route('/check/<string:senderID>',methods=['GET'])
def check(senderID):
    if (senderID in flag) and (flag[senderID]):
        return 'sender id in flag'
    else:
        return 'sender id not in flag'

if __name__ == '__main__':
    app.run(threaded=True)