# Linux Privilege Escalation

## Table of Contents
* [Tips](#tips)
* [Notable Local Exploits](#notable-local-exploits)
* [Enumeration](#enumeration)


## Tips
* Make sure low-privilege shell is fully interactive with command: ```python -c 'import pty;pty.spawn("/bin/bash")'```
* check PATH variable and ensure it is set "properly" (isn't mostly empty). If PATH looks strange, set it to something more "normal"
* check for sudo privileges (usually requires user password): ```sudo -l```
* Try logging in using different creds discovered for the same system: different accounts may have sudo privileges.
* Get the list of users from /etc/passwd and attempt username:password (ie admin:admin) brute-force attack via adjacent protocols (manually-created non-root users start at id 1000).
* For local exploits that need to be compiled, ALWAYS try compiling them on the target system first. If compilation tools are not installed/available on the target system, compile them locally.


## Notable Local Exploits
* Mempodipper (Linux Kernel 2.6.39 < 3.2.2):
  * [https://www.exploit-db.com/exploits/18411](https://www.exploit-db.com/exploits/18411)
  * [https://www.exploit-db.com/exploits/35161](https://www.exploit-db.com/exploits/35161)
  * **Tip:** Success appears to be somewhat random; If one exploit version fails, try the other.
* Dirty Cow (Linux Kernel 2.6.22 < 3.9):
  * [https://www.exploit-db.com/exploits/40616](https://www.exploit-db.com/exploits/40616)
  * [https://www.exploit-db.com/exploits/40847](https://www.exploit-db.com/exploits/40847)
  * [https://www.exploit-db.com/exploits/40838](https://www.exploit-db.com/exploits/40838)
  * [https://www.exploit-db.com/exploits/40839](https://www.exploit-db.com/exploits/40839)
  * [https://www.exploit-db.com/exploits/40611](https://www.exploit-db.com/exploits/40611)


## Enumeration

### Generic Tools
* [pspy](https://github.com/DominicBreuker/pspy)
* [LinEnum](https://github.com/rebootuser/LinEnum)
* [linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
* [Linux Privilege Escalation Checker](https://github.com/sleventyeleven/linuxprivchecker)

### Get all users on system
```
cut -d":" -f 1 /etc/passwd
```
**Note:** created user accounts start with ID 1000.

### Get Linux Distribution and Version
```
ls /etc/*-release
cat /etc/*-release
```

### Get kernel version and bitness
```
uname -mrs
```

### Look at environment variables
```
cat /etc/profile
cat /etc/bashrc
cat ~/.bash_profile
cat ~/.bashrc
cat ~/.bash_logout
env
set
```

### Look at cronjobs
```
crontab -l
ls -alh /var/spool/cron
ls -al /etc/ | grep cron
ls -al /etc/cron*
cat /etc/cron*
cat /etc/at.allow
cat /etc/at.deny
cat /etc/cron.allow
cat /etc/cron.deny
cat /etc/crontab
cat /etc/anacrontab
cat /var/spool/cron/crontabs/root
```

### Search filesystem for world-writeable directories/files

#### World-writeable files
```
find / -perm -2 ! -type l -ls 2>/dev/null
```

#### World-writeable directories
```
find / -writable -type d 2>/dev/null
find / -perm -222 -type d 2>/dev/null
find / -perm -o w -type d 2>/dev/null
```

#### World-executable directories
```
find / -perm -o x -type d 2>/dev/null
```

#### World-writeable/executable directories
```
find / \( -perm -o w -perm -o x \) -type d 2>/dev/null
```

### Search filesystem for cleartext passwords in files
```
grep -i user [filename]
grep -i pass [filename]
grep -C 5 "password" [filename]
```

#### Search specifically for Joomla files containing cleartext passwords
```
find . -name "*.php" -print0 | xargs -0 grep -i -n "var $password"
```

### Search for "interesting" items in home directories
```
ls -ahlR /home/
```

### Search for writable files in /etc

#### Writeable by anyone
```
ls -aRl /etc/ | awk '$1 ~ /^.*w.*/' 2>/dev/null
find /etc/ -readable -type f 2>/dev/null
find /etc/ -readable -type f -maxdepth 1 2>/dev/null
```

#### Writeable by owner
```
ls -aRl /etc/ | awk '$1 ~ /^..w/' 2>/dev/null
```

#### Writeable by group
```
ls -aRl /etc/ | awk '$1 ~ /^.....w/' 2>/dev/null
```

#### Writeable by other
```
ls -aRl /etc/ | awk '$1 ~ /w.$/' 2>/dev/null
```

### Search for files with suid permission
```
find / -perm -u=s -type f 2>/dev/null
```

## Exploitation

### [uidgid0.c](uidgid0.c)
Small executable for obtaining root group privileges (when current shell is running as root user but not root group: ```uid=0(root) gid=33(www-data)```).

#### Compiling
```
gcc -o uidgid0 uidgid0.c
```

#### Executing (on target system)
```
chmod +x uidgid0
./uidgid0
```

