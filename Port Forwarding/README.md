# Port Forwarding

## Table of Contents
* [SSH](#ssh)
* [Proxychains](#proxychains)
* [httptunnel](#httptunnel)
* [stunnel](#stunnel)
* [rinetd](#rinetd)


## SSH

### Options (useful when performing SSH port forwarding)
```
-f: background SSH process after session is successfully established
-N: do not execute a remote command
```

### Local Port Forwarding
Connect to SSH server [SSH_SERVER], bind [LOCAL_PORT] on SSH client, and forward all traffic sent to [LOCAL_PORT] through [SSH_SERVER] to [REMOTE_HOST] on [REMOTE_PORT]
```
ssh -L [LOCAL_PORT:REMOTE_HOST:REMOTE_PORT] [SSH_SERVER]
```

### Remote Port Forwarding
Connect to SSH server [SSH_SERVER], bind [LOCAL_PORT] on [SSH_SERVER], and forward all traffic sent to [LOCAL_PORT] through SSH client to [REMOTE_HOST] on [REMOTE_PORT]
```
ssh -R [LOCAL_PORT]:[REMOTE_HOST]:[REMOTE_PORT] [SSH_SERVER]
```

### Dynamic Port Forwarding
Connect to SSH server [SSH_SERVER], bind [LOCAL_PORT] on SSH client, and forward all traffic proxied (SOCKS) to [LOCAL_PORT] through [SSH_SERVER]
```
ssh -D [LOCAL_PORT] [SSH_SERVER]
```


## Proxychains
Execute a command and tunnel all network traffic from the command through designated local proxies

### Execute command (and tunnel traffic) via proxychains
```
proxychains [COMMAND] [COMMAND_ARGS]
```

### Example configuration file
* [proxychains.conf](proxychains.conf)


## httptunnel
Forward all traffic to a remote host/port encapsulated in cleartext HTTP. Includes both a server and a client component

### Execute server component to accept HTTP connections from clients on LOCAL_PORT and forward all traffic to [REMOTE_HOST]:[REMOTE_PORT] on any protocol
```
hts -F [REMOTE_HOST]:[REMOTE_PORT] [LOCAL_PORT]
```

### Execute client component to bind LOCAL_PORT and forward all traffic to hts (server component) at [REMOTE_HOST]:[REMOTE_PORT]
```
htc -F [LOCAL_PORT] [REMOTE_HOST]:[REMOTE_PORT]
```


## stunnel
Forward all traffic to a remote host/port encapsulated in encrypted HTTPS. Includes both a server and a client component.

Very effective for circumventing firewalls (such as those that only allow outbound traffic on TCP ports 80 and 443), as all traffic resembles normal HTTPS traffic.

### Generate certificate file (stunnel.pem) to be shared by both server and client components
```
openssl genrsa 4096 > stunnel.key
openssl req -new -key stunnel.key -x509 -days 1000 -out stunnel.crt
cat stunnel.crt stunnel.key > stunnel.pem
rm stunnel.key stunnel.crt
```

### Example configuration files
* Server configuration: [stunnel-server.conf](stunnel-server.conf)
* client configuration: [stunnel-client.conf](stunnel-client.conf)

### Execute stunnel (as server or client)
```
stunnel [CONFIG_FILE]
```


## rinetd
Redirect TCP traffic from one IP address and port to another IP address and port.

### Execute rinetd
```
rinetd -c [CONFIG_FILE]
```

### Example configuration file
* [rinetd.conf](rinetd.conf)


