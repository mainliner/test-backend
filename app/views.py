from app import app, db, models
from apns import APNs, Payload
from flask import render_template, flash, redirect, request

import os
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/send',methods=['GET','POST'])
def send():
    #if request.method == 'GET':
    #    return render_template('send.html') 
    certfile= os.path.abspath(os.path.dirname(__file__))+ '/PushChatCert.pem'
    keyfile= os.path.abspath(os.path.dirname(__file__))+ '/pushchatkey2.pem'
    apns = APNs(use_sandbox=True, cert_file=certfile, key_file=keyfile)
    # Send a notification
    token_hex = '5315b5bdabc6b9da640e7103200e83b0126904cf3b26ed00498797ddb34e3f06'
    payload = Payload(alert="Hello World!", sound="default", badge=1,custom={'url':'http://ddd.d.com'})
    apns.gateway_server.send_notification(token_hex, payload)
    #for (token_hex, fail_time) in apns.feedback_server.items():
    #    return "send successful" + str(fail_time)
    return "successful"

def store_user(jsondata):
    try:
        udid=jsondata['udid']
        language=jsondata['language']
        push=jsondata['push']
        last=jsondata['last']
        token=None
        if jsondata.has_key('token'):
            if(jsondata['token'] is not None):
                token=jsondata['token']
        checkuser = models.User.query.filter_by(udid=udid).first()
        if checkuser is not None:
            print '>The user exists, update the data'
            checkuser.udid=udid
            checkuser.language=language
            checkuser.push=push
            checkuser.last=datetime.date.today()
            checkuser.token=token
            db.session.commit()
        else:
            print '>The user doesnt exists, create one'
            newuser = models.User(udid=udid,language=language,push=push,last=last,token=token)
            db.session.add(newuser)
            db.session.commit()
    except:
        print "store data error"

@app.route('/receive/user',methods=['POST'])
def receive_user():
    if request.headers['Content-Type'] == 'application/json':
        store_user(request.json)
        return "updata successful"
    else:
        return "wrong request data"
