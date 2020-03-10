# Traffic Monitoring

## Table of Contents
* [Wireshark](#wireshark)
* [tcpdump](#tcpdump)
* [iptables](#iptables)


## Wireshark
Keep "Capture Filters" in mind. If you know exactly what you are looking for, this should reduce noise and shorten loading times later on.


## tcpdump

### Usage
```
tcpdump [OPTIONS] [DISPLAY_FILTERS]
```

### Options
```
-i: interface to listen on
-r: read raw packets from pcap file
-w: write raw packets to file instead of displaying them
-n: only display numeric addresses
-X: print packet contents along with headers, in hex and ASCII
```

### Display Filters
```
and/or: chain multiple filters together
host [HOST]: display traffic transmitted to/from [HOST]
port [PORT]: display traffic transmitted to/from [PORT]
```


## iptables
The volume of incoming/outgoing traffic to/from a specific IP address can be monitored using iptables

### Monitor traffic coming in from [REMOTE_IP]
```
iptables -I INPUT 1 -s [REMOTE_IP] -j ACCEPT
```

### Monitor traffic going out to [REMOTE_IP]
```
iptables -I OUTPUT 1 -d [REMOTE_IP] -j ACCEPT
```

### Reset traffic counters
```
iptables -Z
```

### View traffic counters
```
iptables -vn -L
```

