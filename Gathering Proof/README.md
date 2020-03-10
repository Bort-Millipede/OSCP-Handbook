# Gathering Proof

## Table of Contents
* [Generic Procedure](#generic-procedure)
* [Windows](#windows)
* [*nix](#nix)


## Generic Procedure
Commands for proof screenshots should usually be executed in the following order:
* print current user
* print whether current user is an admin (if not root or SYSTEM)
* print proof.txt (or local.txt if not admin)
* print ipconfig/ifconfig


## Windows

### Get current user
```
whoami
```
```
echo %USERNAME%
```
On older Windows where whoami is not pre-installed and %USERNAME% is not set): transfer whoami.exe (/usr/share/windows-binaries/whoami.exe) to target system (via FTP or debug.exe).

### Display whether current user is an admin (if not SYSTEM)
```
net user [USER] | findstr "Group Memberships"
```
* admin user: output will contain "Administrators"
* non-admin user: output will NOT contain "Administrators"

### Display proof.txt (almost all cases)
* Newer Windows (Vista/2008 and later): ```type "C:\Users\Administrator\Desktop\proof.txt"```
* Older Windows (XP/2003 and earlier): ```type "C:\Documents and Settings\Administrator\Desktop\proof.txt"```

### Display networking information
```
ipconfig
```


## *nix

### Get current user
```
id
```

### Display whether current user is root
output of ```id``` should be: ```uid=0(root) gid=0(root) ...```

### Display proof.txt (almost all cases)
```
cat /root/proof.txt
```

### Display networking information
```
/sbin/ifconfig
```

