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
    return app.send_static_file('gottalight_gui.html')

@app .route( "/getinfo" )
def getinfo():
    return Response(subprocess.check_output(['lightning-cli', 'getinfo']),mimetype='application/json')

@app .route( "/listpeers" )
def listpeers():
    return Response(subprocess.check_output(['lightning-cli', 'listpeers']),mimetype='application/json')

@app .route( "/listfunds" )
def listfunds():
    return Response(subprocess.check_output(['lightning-cli', 'listfunds']),mimetype='application/json')

@app .route( "/listinvoices" )
def listinvoices():
    return Response(subprocess.check_output(['lightning-cli', 'listinvoices']),mimetype='application/json')

@app .route( "/invoice" )
def invoice():
    p1=request.args.get("amount")
    p2=request.args.get("label")
    p3=request.args.get("desc")
   
    resp = "["
    try:
        resp+=(subprocess.check_output(['lightning-cli','invoice', p1, p2, p3],stderr=subprocess.STDOUT)).decode('utf-8')
        resp+=", \"SUCCESS\"]"

    except subprocess.CalledProcessError as e:
        resp+=e.output.decode('utf-8')+", \"ERROR\"]"

    return Response(resp,mimetype='application/json')


@app .route( "/invoiceqr" )
def invoiceqr():
    p1=request.args.get("amount")
    p2=request.args.get("label")
    p3=request.args.get("desc")

    bolt11 = "ERROR"

    resp = "["
    try:
        invoice=(subprocess.check_output(['lightning-cli','invoice', p1, p2, p3],stderr=subprocess.STDOUT)).decode('utf-8')
        #bolt11 = json.loads(invoice.decode('utf-8'))['bolt11']
        bolt11 = json.loads(invoice)['bolt11']
        #invoice= subprocess.check_output(['lightning-cli','invoice', p1, p2, p3])
    except subprocess.CalledProcessError as e:
        resp+=e.output.decode('utf-8')+", \"ERROR\"]"
        return Response(resp,mimetype='application/json')

    return send_file(qrcode(bolt11,mode='raw',border=10),mimetype='image/png')

@app .route("/waitinvoice")
def waitinvoice():
    p1=request.args.get("bolt11")
    return Response(subprocess.check_output(['lightning-cli','waitinvoice',p1]),mimetype='application/json')


@app .route("/pay")
def pay():
    bolt11=request.args.get("bolt11")
    resp = "["
    try:
        resp+=(subprocess.check_output(['lightning-cli','pay', bolt11],stderr=subprocess.STDOUT)).decode('utf-8')
        resp+=", \"SUCCESS\"]"

    except subprocess.CalledProcessError as e:
        resp+=e.output.decode('utf-8')+", \"ERROR\"]"

    return Response(resp,mimetype='application/json')
    
@app .route("/delexpiredinvoce")
def delexpiredinvoce():
    return Response(subprocess.check_output(['lightning-cli','delexpiredinvoce']),mimetype='application/json')

@app .route("/getlog")
def getlog():
    return Response(subprocess.check_output(['lightning-cli','getlog']),mimetype='application/json')

@app .route("/listconfigs")
def listconfigs():
    return Response(subprocess.check_output(['lightning-cli','listconfigs']),mimetype='application/json')

@app .route("/listforwards")
def listforwards():
    return Response(subprocess.check_output(['lightning-cli','listforwards']),mimetype='application/json')

@app .route("/devrescanoutputs")
def devrescanoutputs():
    return Response(subprocess.check_output(['lightning-cli','dev-rescan-outputs']),mimetype='application/json')

@app .route("/connect")
def connect():
    p1=request.args.get("id")
    resp = "["
    try:
        resp+=(subprocess.check_output(['lightning-cli','connect', p1],stderr=subprocess.STDOUT)).decode('utf-8')
        resp+=", \"SUCCESS\"]"

    except subprocess.CalledProcessError as e:
        resp+=e.output.decode('utf-8')+", \"ERROR\"]"

    return Response(resp,mimetype='application/json')

@app .route("/close")
def closeid():
    p1=request.args.get("id")
    resp = "["
    try: 
        resp+=(subprocess.check_output(['lightning-cli','close', p1],stderr=subprocess.STDOUT)).decode('utf-8')
        resp+=", \"SUCCESS\"]"

    except subprocess.CalledProcessError as e:
        resp+=e.output.decode('utf-8')+", \"ERROR\"]"

    return Response(resp,mimetype='application/json')

@app .route("/disconnect")
def disconnect():
    p1=request.args.get("id")
    resp = "["
    try: 
        resp+=(subprocess.check_output(['lightning-cli','disconnect', p1],stderr=subprocess.STDOUT)).decode('utf-8')
        resp+=", \"SUCCESS\"]"
    except subprocess.CalledProcessError as e:
        resp+=e.output.decode('utf-8')+", \"ERROR\"]"

    return Response(resp,mimetype='application/json')

@app .route("/fundchannel")
def fundchannel():
    p1=request.args.get("id")
    p2=request.args.get("amount")
    resp = "["
    try: 
        resp+=(subprocess.check_output(['lightning-cli','fundchannel', p1,p2],stderr=subprocess.STDOUT)).decode('utf-8')
        resp+=", \"SUCCESS\"]"
    except subprocess.CalledProcessError as e:
        resp+=e.output.decode('utf-8')+", \"ERROR\"]"

    return Response(resp,mimetype='application/json')

@app .route("/getroute")
def getroute():
    node_id=request.args.get("node_id")
    msatoshi=request.args.get("msatoshi")
    riskfactor=request.args.get("riskfactor")
    resp = "["
    try: 
        resp+=(subprocess.check_output(['lightning-cli','getroute', node_id,msatoshi,riskfactor],stderr=subprocess.STDOUT)).decode('utf-8')
        resp+=", \"SUCCESS\"]"
    except subprocess.CalledProcessError as e:
        resp+=e.output.decode('utf-8')+", \"ERROR\"]"
    return Response(resp,mimetype='application/json')

if __name__ == "__main__" :
    app.run( host = '0.0.0.0' ,  debug = True )
