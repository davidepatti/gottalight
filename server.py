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

@app .route( "/getinfo" )
def getinfo():
    return Response(subprocess.check_output(['lightning-cli', 'getinfo']),mimetype='application(json')

@app .route( "/listpeers" )
def listpeers():
    return Response(subprocess.check_output(['lightning-cli', 'listpeers']),mimetype='application/json')

@app .route( "/listfunds" )
def listfunds():
    return Response(subprocess.check_output(['lightning-cli', 'listfunds']),mimetype='application/json')

@app .route( "/search_node" )
def search_node():
    return "https://1ml.com/testnet/node/"

@app .route( "/listinvoices" )
def listinvoices():
    return Response(subprocess.check_output(['lightning-cli', 'listinvoices']),mimetype='application(json')

@app .route( "/invoice" )
def invoice():
    p1=request.args.get("amount")
    p2=request.args.get("label")
    p3=request.args.get("desc")
   
    return Response(subprocess.check_output(['lightning-cli','invoice', p1, p2, p3]),mimetype='application/json')


@app .route( "/invoiceqr" )
def invoiceqr():
    p1=request.args.get("amount")
    p2=request.args.get("label")
    p3=request.args.get("desc")
    invoice= subprocess.check_output(['lightning-cli','invoice', p1, p2, p3])
    bolt11 = json.loads(invoice.decode('utf-8'))['bolt11']
    
    return send_file(qrcode(bolt11,mode='raw',border=10),mimetype='image/png')

@app .route("/waitinvoice")
def waitinvoice():
    p1=request.args.get("bolt11")
    return Response(subprocess.check_output(['lightning-cli','waitinvoice',p1]),mimetype='application/json')


@app .route("/pay")
def pay():
    bolt11=request.args.get("bolt11")
    return Response(subprocess.check_output(['lightning-cli','pay', bolt11]),mimetype='application/json')
    
@app .route("/connect")
def connect():
    p1=request.args.get("id")
    return Response(subprocess.check_output(['lightning-cli','connect', p1]),mimetype='application/json')

@app .route("/fundchannel")
def fundchannel():
    p1=request.args.get("id")
    p2=request.args.get("amount")
    return Response(subprocess.check_output(['lightning-cli','fundchannel', p1,p2]),mimetype='application/json')

@app .route("/getroute")
def getroute():
    node_id=request.args.get("node_id")
    msatoshi=request.args.get("msatoshi")
    riskfactor=request.args.get("riskfactor")
    return Response(subprocess.check_output(['lightning-cli','getroute', node_id,msatoshi,riskfactor]),mimetype='application/json')

if __name__ == "__main__" :
    app.run( host = '0.0.0.0' ,  debug = True )
