# Updating Kali
The following updates should be applied (and can be done safely) on the [32-bit PWK Kali VM](https://support.offensive-security.com/pwk-kali-vm/) periodically, especially before a major event (such as an exam attempt or lab extension).

## Table of Contents
* [searchsploit](#searchsploit)
* [nmap](#nmap)
* [wpscan](#wpscan)
* [locate](#locate)

## searchsploit
```
searchsploit -u
```

## nmap
```
nmap --script-updatedb
```

## wpscan
```
wpscan --update
```

## locate
```
updatedb
```

