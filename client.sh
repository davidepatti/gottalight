#!/bin/sh
NODE_SSH_ACCESS="user@someaddress"
# this path is valid for MaCOS, change using your path
FIREFOX_PATH="/Applications/Firefox.app/Contents/MacOS/firefox"
echo 'user_pref("network.proxy.socks", localhost);' >> prefs.js
echo 'user_pref("network.proxy.socks_port", 8192);' >> prefs.js

#
$FIREFOX_PATH -no-remote -P prefs.js
ssh -ND 8192 $NODE_SSH_ACCESS
