# GottaLight
Testing Environment for Bitcoin Lightning Network 
**WARNING**: still in very experimental early development stage, use on testnet ONLY

## Requirements
* A Bitcoin full node (see [this guide](https://medium.com/@meeDamian/bitcoin-full-node-on-rbp3-revised-88bb7c8ef1d1) for Raspberry Pi)
* A Lightning Network full node (install c-lightning following [this guide](https://medium.com/@meeDamian/c-lightning-node-on-rbp3-b950660fb835))
* python3 

## Installation

* Switch to the user that can run command line c-lightning commands. For example, assuming that user is "lightning":
`sudo su - lightning`
* Clone the source code:
`git clone https://github.com/davidepatti/gottalight.git`
* Execute the gottalight server:
`python3 server.py` 

Now c-lightning API and functionalities will be available via URLs. For example, connecting with browswer to the port 5000 of your node.

## Security

In order to acces the web server, port 5000 of your node should be open.
The simplest (and unsecure) solution could be just to open such port to every connection:

`sudo ufw allow from any to any proto tcp port 5000`

**IMPORTANT:** A best approach should be to restrict the connection to only some particular clients.
For example, connect only from local nodes in a 192.168.1.x local network:

`sudo ufw allow from 192.168.1.0/24 to any proto tcp port 5000`
