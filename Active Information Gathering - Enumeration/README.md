# Active Information Gathering / Enumeration

## Table of Contents
   * [Active Information Gathering / Enumeration](#active-information-gathering--enumeration)
* [Nmap](#nmap)
* [DNS Enumeration](#dns-enumeration)
* [SMB Enumeration](#smb-enumeration)
* [SMTP Enumeration](#smtp-enumeration)
* [POP3 Enumeration](#pop3-enumeration)
* [SNMP Enumeration](#snmp-enumeration)
* [FTP Enumeration](#ftp-enumeration)
* [HTTP/HTTPS Enumeration](#httphttps-enumeration)
* [SQL Enumeration](#sql-enumeration)
   * [MySQL](#mysql)
   * [SQL Server (MSSQL)](#sql-server-mssql)
   * [PostgreSQL](#postgresql)
   * [Oracle](#oracle)
* [LDAP Enumeration](#ldap-enumeration)


## Nmap

### Scanning modes
Notes on Scanning modes:
* CONNECT scanning is fast but produces a lot of traffic.
* SYN scanning produces significantly less traffic and more results, but is SLOW
* UDP scanning is SLOW

```
-sn: Ping Sweep, no port scanning
-sT: TCP CONNECT scanning (ports considered open if three-way handshake is completed)
-sS: TCP SYN scanning (ports considered open if SYN-ACK is received from target)
-sA: TCP ACK scanning
-sU: UDP scanning (Port is consider opened if no reply is received, while port is considered closed if "ICMP port unreachable" response is received)
-sV: Service scanning
-sC: Execute the most common scripts following port scan
```

### Options
```
-Pn: treat all target hosts as alive and scan anyway
--version-all: try all software versions during Service scanning
--script [SCRIPT(S)]: execute Nmap scripts after port scanning
-O: Operating system detection
-oA [PREFIX]: Output results in raw, greppable, and XML formats with filenames [PREFIX].nmap, [PREFIX].gnmap, and [PREFIX].xml
-p [PORT(S)]: port(s) to scan (Can be both TCP and UDP ports: -p T:1-65535,U:19,53,123,161)
-A: OS, version, script and traceroute (includes -O)
--open: only display open ports
-Pn: skip ping scanning, treat all targets as live
-d -d: display complete list of ports scanned (open, closed, filtered, etc.)
-T [NUM]: set timing template to [NUM] (higher is faster)
```

### Recommended command for scanning a target
```
nmap -v -oA [OUTPUT_FILENAME_PREFIX] -p1-65535 -sV -sC -O -Pn [TARGET_IP]
```

### Low and VERY SLOW port scan
```
nmap -v -oA [OUTPUT_FILENAME_PREFIX] -p1-65535 -T1 -sS -Pn [TARGET_IP]
```

### Generate comma-separated list of scripts to run, to be used as ```--script``` argument
```
for s in `ls -l /usr/share/nmap/scripts/* | cut -d"/" -f 6 | cut -d"." -f 1`; do echo -ne "$s,"; done
```
Fine-tune results by modifying "ls" command.


## DNS Enumeration
Default listening port: TCP port 53

### Generic Procedure
* Attempt zone transfer for target domain.
* Try subdomain brute force (nmap) later.

### DNS lookup
```
host [HOSTNAME]
```

### DNS reverse lookup
```
host [IP]
```

### Zone Transfer for [DOMAIN]
```
host -l [DOMAIN] [DNS_SERVER]
```
```
dnsrecon -d [DOMAIN] -t axfr -n [DNS_SERVER]
```

### Attempt zone transfer against all name servers discovered for [DOMAIN]
```
dnsrecon -d [DOMAIN] -t axfr
```

### Attempt zone transfer against all name servers discovered for [DOMAIN]
```
dnsenum [DOMAIN]
```

### Attempt zone transfer against name server [DNS_SERVER] for [DOMAIN]
```
dnsenum --dnsserver [DNS_SERVER] [DOMAIN]
```

### Attempt zone transfer against name server [DNS_SERVER]
```
nmap -v -p 53 --script=dns-zone-transfer --script-args "dns-zone-transfer.domain=[DOMAIN]" [DNS_SERVER]
```
**Note:** [DNS_SERVER] must be a domain name, not an IP address.

### List Name Servers for [DOMAIN] (using DNS lookup)
```
host -t ns [DOMAIN]
```

### Nmap scripts
* dns-brute: bruteforce DNS subdomains
* dns-zone-transfer: perform DNS zone transfer (described above)


## SMB Enumeration
Default listening ports: TCP 139 and 445

### Generic Procedure
* Find SMB listeners (nmap 139 and 445).
* Enumerate as much SMB information as possible (via nbtscan and enum4linux, then nmap scripts if necessary).
* Do vuln scanning (nmap scripts).
* Find and utilize exploits.

### Tips
* smb-enum-shares Nmap script tries to login as Guest (on Windows) with a blank password: take note of results to see if this was successful or not.


### nbtscan
scan target IP(s) for NetBIOS name information

#### Options
```
-f [FILE]: scan list of IPs from file [FILE]
-f -: get target IP address from stdin
-v: verbose, print all NetBIOS names received from target
-h: print verbose results in human-readable format (must be used with -v)
```

#### Scan single target
```
nbtscan [IP]
```

#### Scan target range
```
nbtscan [IP_RANGE]
nbtscan [IP1]-[IPn]
```


### enum4linux
Wrapper around native SMB/samba tools (smbclient, net, etc.)

#### Options
```
-a: do all simple enumerations
-v: verbose output, show all commands that are being run
```

#### Important information enumerated by enum4linux
* Target OS info
* SMB shares
* Workgroup listing


### Nmap scripts
* smb\*vuln\*: All SMB vulnerability scanning scripts
  * smb2-vuln-uptime
  * smb-vuln-conficker
  * smb-vuln-cve2009-3103
  * smb-vuln-cve-2017-7494
  * smb-vuln-ms06-025
  * smb-vuln-ms07-029
  * smb-vuln-ms08-067
  * smb-vuln-ms10-054
  * smb-vuln-ms10-061
  * smb-vuln-ms17-010
  * smb-vuln-regsvc-dos
* smb\*-enum-\*: All SMB enumeration scripts
  * smb-enum-domains: Attempts to enumerate domains on a system, along with their policies.
  * smb-enum-groups: Obtains a list of groups from the remote Windows system, as well as a list of the group's users.
  * smb-enum-processes: Pulls a list of processes from the remote server over SMB.
  * smb-enum-services: Retrieves the list of services running on a remote Windows system.
  * smb-enum-sessions: Enumerates the users logged into a system either locally or through an SMB share.
  * smb-enum-shares: Attempts to list shares using the srvsvc.NetShareEnumAll MSRPC function and retrieve more information about them using srvsvc.NetShareGetInfo. If access to those functions is denied, a list of common share names are checked.
  * smb-enum-users: Attempts to enumerate the users on a remote Windows system, with as much information as possible, through two different techniques
  * smb-mbenum: Queries information managed by the Windows Master Browser.
* smb2-capabilities: list the supported capabilities in a SMBv2 server for each enabled dialect.
* smb-brute: Brute force SMB username/password combinations
* smb-double-pulsar-backdoor: Checks if the target machine is running the Double Pulsar SMB backdoor.
* smb-system-info: Pulls back information about the remote system from the registry
* smb-ls: Attempts to retrieve useful information about files shared on SMB volumes
* smb-os-discovery: Attempts to determine the operating system, computer name, domain, workgroup, and current time over the SMB protocol (ports 445 or 139).
* smb-protocols: Attempts to list the supported protocols and dialects of a SMB server.
* smb-psexec: Implements remote process execution similar to the Sysinternals' psexec tool, allowing a user to run a series of programs on a remote machine and read the output.


### Manually connect to SMB share
```
smbclient //'[HOST]'/[SHARE_NAME] -U'[USERNAME]'%'[PASSWORD]' 2>&1
```
**Tip:** Shares can sometimes be connected to anonymously (username '' and password '') or with the "guest" account (username 'guest' and password '')


## SMTP Enumeration
Default listening ports: TCP ports 25 or 587

### Generic Procedure
* Find SMTP servers (nmap TCP 25)
* Attempt to enumerate system info (primarily: enumerate users on the system using VRFY, EXPN, RCPT TO)

### [smtp-vrfy-bf.py](smtp-vrfy-bf.py)
Python script to brute force users via SMTP VRFY.

#### Usage
```
python smtp-vrfy-bf.py [HOST] [PORT] [FILE_CONTAINING_USERNAMES]
```

### Nmap scripts
* smtp-enum-users: Attempts to enumerate the users on a SMTP server by issuing the VRFY, EXPN or RCPT TO commands.
* smtp-commands: Attempts to use EHLO and HELP to gather the Extended commands supported by an SMTP server.
* smtp-brute: Performs brute force password auditing against SMTP servers using either LOGIN, PLAIN, CRAM-MD5, DIGEST-MD5 or NTLM authentication.
* smtp-ntlm-info: This script enumerates information from remote SMTP services with NTLM authentication enabled. 
  * **Note:** Sending an SMTP NTLM authentication request with null credentials will cause the remote service to respond with a NTLMSSP message disclosing system information, including NetBIOS, DNS, and OS build version.
* smtp-vuln\*: SMTP vulnerability scanning
  * smtp-vuln-cve2010-4344
  * smtp-vuln-cve2011-1720
  * smtp-vuln-cve2011-1764


## POP3 Enumeration
Default listening port: TCP 110

### Usual workflow (login and read email)
```
USER [USERNAME]
PASS [PASSWORD]
LIST
RETR [ID]
```

### Nmap scripts
* pop3-brute
* pop3-capabilities: Retrieves POP3 email server capabilities.
* pop3-ntlm-info: Enumerates information from remote POP3 services with NTLM authentication enabled.


## SNMP Enumeration
Usually listening on UDP port 161

### Generic Procedure
* Find SNMP servers (nmap UDP 161)
* Attempt to enumerate system info
* Target default/weak community strings (such as "public", "private", "manager")

### Tips
* Check for Write privileges

### Community string wordlists
* snmp_default_pass.txt (Provided by the Metasploit Framework: /usr/share/wordlists/metasploit/snmp_default_pass.txt)
* snmpcommunities.lst (Provided by Nmap: /usr/share/nmap/nselib/data/snmpcommunities.lst)

### Helpful Windows OID values
* 1.3.6.1.2.1.25.1.6.0: System Processes
* 1.3.6.1.2.1.25.4.2.1.2: Running Programs
* 1.3.6.1.2.1.25.4.2.1.4: Processes Path
* 1.3.6.1.2.1.25.2.3.1.4: Storage Units
* 1.3.6.1.2.1.25.6.3.1.2: Software Name
* 1.3.6.1.4.1.77.1.2.25: User Accounts
* 1.3.6.1.2.1.6.13.1.3: TCP Local Ports

### onesixtyone
Simple SNMP scanner

#### Options
```
-c [FILE]: file containing SNMP community string values to try
-i [FILE]: file containing hosts to scan
-o [FILE]: file to save output to
```

#### Usage
Scan single host with single community string
```
onesixtyone [HOST] [COMMUNITY]
```

Scan multiple hosts (saved to file) with single community string
```
onesixtyone -i [FILE] [COMMUNITY]
```

Scan multiple hosts (saved to file) with multiple community strings (saved to file)
```
onesixtyone -i [HOSTS_FILE] -c [COMMUNITY_FILE]
```

### snmpwalk
Enumerate MIB tree on target hosts (where community string is known) using exact MIB values

#### Options
```
-v1, -v2c, -v3: set SNMP version to use (1, 2c, 3)
-c [STRING]: use community string [STRING] (for versions 1 and 2c)
```

#### Usage
Enumerate entire MIB tree
```
snmpwalk -c [COMMUNITY_STRING] -v[VERSION] [HOST]
```

Enumerate specific OID value from MIB tree
```
snmpwalk -c [COMMUNITY_STRING] -v[VERSION] [HOST] [OID]
```

### snmp-check
Enumerate SNMP MIB tree with human-readable output

#### Options
```
-v1, -v2c: specify SNMP version (1 or 2c)
-c [STRING]: specify community string to use
-w: detect write access
```

#### Usage
Enumerate MIB tree on target
```
snmp-check -c [COMMUNITY] [HOST]
```

### Nmap scripts
* snmp-brute: brute force SNMP community strings
* snmp-info: enumerate basic information using SNMPv3
* snmp-interfaces: enumerate network interfaces
* snmp-ios-config: download Cisco router IOS configuration files using SNMPv1
* snmp-netstat: enumerate open ports in netstat-like output
* snmp-processes: enumerate running processes
* snmp-sysdescr: enumerate system informaion using SNMPv1
* snmp-win32-services: enumerate Windows services
* snmp-win32-shares: enumerate Windows shares
* snmp-win32-software: enumerate software installed on Windows
* snmp-win32-users: enumerate Windows user accounts


## FTP Enumeration
Default listening port: TCP 21

### Nmap scripts
* ftp-anon: Check if server allows anonymous logins
* ftp-brute: brute force FTP passwords
* ftp-proftpd-backdoor: Checks for the presence of the ProFTPD 1.3.3c backdoor
* ftp-syst: Sends FTP SYST and STAT commands and returns the result
* ftp-vsftpd-backdoor: Checks for the presence of the vsFTPd 2.3.4 backdoor
* ftp-vuln-cve2010-4221: Checks for a stack-based buffer overflow in the ProFTPD server, version between 1.3.2rc3 and 1.3.3b


## [HTTP/HTTPS Enumeration](HTTP-HTTPS)


## SQL Enumeration

### MySQL

#### Nmap scripts
* mysql-audit: Audits MySQL database server security configuration against parts of the CIS MySQL v1.0.2 benchmark (requires mysql-audit.username and mysql-audit.password args)
* mysql-brute
* mysql-databases: Attempts to list all databases on a MySQL server (requires mysqluser and mysqlpass args)
* mysql-dump-hashes: Dumps the password hashes from an MySQL server in a format suitable for cracking by tools such as John the Ripper (requires username and password args)
* mysql-empty-password: Checks for MySQL servers with an empty password for root or anonymous.
* mysql-enum: Performs valid-user enumeration against MySQL 5.0 by leveraging a vulnerability
* mysql-info: Connects to a MySQL server and prints information
* mysql-query: Runs a query against a MySQL database and returns the results as a table (requires mysql-query.query, mysql-query.username, and mysql-query.password args)
* mysql-users: Attempts to list all users on a MySQL server (requires mysqluser and mysqlpass args)
* mysql-variables: Attempts to show all variables on a MySQL server (requires mysqluser and mysqlpass args)
* mysql-vuln-cve2012-2122: Attempts to bypass authentication in MySQL 5 and MariaDB servers by exploiting CVE2012-2122

### SQL Server (MSSQL)

#### Tips
* If valid database credentials are discovered, immediately check if xp_cmdshell is enabled.

#### Nmap scripts
* broadcast-ms-sql-discover:
* ms-sql-brute
* ms-sql-config
* ms-sql-dac
* ms-sql-dump-hashes
* ms-sql-empty-password
* ms-sql-hasdbaccess
* ms-sql-info
* ms-sql-ntlm-info: Enumerate info from remote SQL Server instance with NTLM authentication enabled.
* ms-sql-query
* ms-sql-tables
* ms-sql-xp-cmdshell: Attempt to run a command using the SQL Server xp_cmdshell stored procedure.

### PostgreSQL

#### Nmap scripts
* pgsql-brute

### Oracle

#### tnscmd10g
Tool to interact with Oracle listeners

#### Nmap scripts
* oracle-brute
* oracle-brute-stealth
* oracle-enum-users
* oracle-sid-brute
* oracle-tns-version

#### XML DB default credentials
```
sys:sys
scott:tiger
```


## LDAP Enumeration
Default listening port: 389, 636 (SSL/TLS)

### ldapsearch
Null/Anonymous bind:
```
ldapsearch -H ldap://[HOST]:[PORT] -x -s base '' "(objectClass=*)" "*" +
```
Tip: take note of any "namingContexts" entry outputs

### Nmap scripts
* ldap-brute: Attempts to brute-force LDAP authentication
* ldap-novell-getpass: 
* ldap-rootdse: Retrieves the LDAP root DSA-specific Entry (DSE)
* ldap-search: Attempts to perform an LDAP search and returns all matches


