# GottaLight

Web Interface Testing Environment for the c-lightning implementation of Bitcoin Lightning Network 

**WARNING**: still in very experimental early development stage, use on testnet ONLY

## Requirements
* A Bitcoin full node (see [this guide](https://medium.com/@meeDamian/bitcoin-full-node-on-rbp3-revised-88bb7c8ef1d1) for Raspberry Pi)
* A Lightning Network full node (install c-lightning following [this guide](https://medium.com/@meeDamian/c-lightning-node-on-rbp3-b950660fb835))
* Install the following packages, for example:

`apt-get install python3 python3-pip libopenjp2-7 libtiff5`

* Then use pip3 to install flask and qrcode:

`sudo pip3 install flask`

`sudo pip3 install flask_qrcode`

## Installation

* Switch to the user that can run command line c-lightning commands. For example, assuming that user is "lightning":
`sudo su - lightning`
* Clone the source code:
`git clone https://github.com/davidepatti/gottalight.git`
* Execute the gottalight server:
`python3 gottalight.py` 

Now c-lightning API and functionalities will be available via URLs by connecting with browswer to the port 5000 of your node.

**TIP:** some JSON visualization helper could be useful when formatting the server response. For example something like [JSONView extension](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) (for Chrome) or similar. Please notice that Mozilla Firefox doesn't require such tip.

## Security

In order to acces the web server, port 5000 of your node should be open.
The simplest (**and dangerous!**) solution could be just to open such port to every connection:

`sudo ufw allow from any to any proto tcp port 5000`

**IMPORTANT:** A best approach should be to restrict the connection to only some particular clients.
For example, connect only from nodes in a 192.168.1.x local network:

`sudo ufw allow from 192.168.1.0/24 to any proto tcp port 5000`

**TIP:** Even if the gottalight server is made accessible from local network addresses only, you could still access it by making a tunnel with ssh. Just follow these simple steps:

* let's assume that your lighning node has address 192.168.1.114 and that the local network is connected to the internet using a router which has and external address *public_address_of_your_router*. 

* Configure the router so that port 8022 is forwarded to the port 22 (ssh) of the lighning node 192.168.1.114.

* Then, from another an external machine type to estabilish an ssh tunnel:

`ssh -D 8192 -N youruser@public_address_of_router -p 8022`

* Finally, use Mozilla Firefox to access http://public_address_of_your_router:5000 , after setting *localhost:8192* as proxy in the Network Settings (please note that this is not possible with Chrome or other).






