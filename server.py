import subprocess
import json
from flask import Flask
from flask import request
from flask import send_file
from flask import Response
from flask_qrcode import QRcode

app = Flask( __name__ , static_url_path='')
qrcode = QRcode(app)

@app .route( "/" )
def index():
    return app.send_static_file('index.html')

@app .route( "/listpeers" )
def listpeers():
    return subprocess.check_output(['./listpeers.sh', ''])

@app .route( "/listfunds" )
def listfunds():
    return subprocess.check_output(['./listfunds.sh', ''])

@app .route( "/getinfo" )
def getinfo():
    return subprocess.check_output(['./getinfo.sh', ''])

@app .route( "/invoice" )
def invoice():
    p1=request.args.get("amount")
    p2=request.args.get("label")
    p3=request.args.get("desc")
   
    #return subprocess.check_output(['./invoice.sh', p1, p2, p3])
    return Response(subprocess.check_output(['./invoice.sh', p1, p2, p3]),mimetype='application/json')


@app .route( "/invoiceqr" )
def invoiceqr():
    p1=request.args.get("amount")
    p2=request.args.get("label")
    p3=request.args.get("desc")
    invoice= subprocess.check_output(['./invoice.sh', p1, p2, p3])
    bolt11 = json.loads(invoice.decode('utf-8'))['bolt11']
    
    return send_file(qrcode(bolt11,mode='raw',border=10),mimetype='image/png')


if __name__ == "__main__" :
    app.run( host = '0.0.0.0' ,  debug = True )
