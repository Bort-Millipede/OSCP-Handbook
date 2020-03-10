# Passive Information Gathering

## Table of Contents
* [Google](#google)
* [Google Hacking Database](#google-hacking-database)
* [Netcraft](#netcraft)
* [theharvester](#theharvester)
* [whois](#whois)
* [Recon-ng](#recon-ng)


## Google

### Filters
* "site:[SITE]": search only for results residing on [SITE] and any associated sub-domains
* "inurl:[STRING]": search only for results with URLs containing [STRING]


## [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
Provided by Offensive Security. Contains user-submitted search queries for gathering certain sensitive information about target sites/organizations


## [Netcraft](https://www.netcraft.com/)
Internet monitoring company that can be leveraged to obtain information about internet-facing web servers, including:
* Operating System
* Web Server platform and version
* Uptime
* etc.


## theharvester
Passively gather email addresses, hostnames, and individual people names belonging to a specified domain

### Options
```
-d: domain to search
-b: data source to use (see help/manpage)
-l: limit number of results
```


## whois

### Lookup
```
whois [DOMAIN]
```

### Reverse Lookup
```
whois [IP]
```


## Recon-ng
"Full-featured" web reconnaissance framework. Very similar user interface to Metasploit. Contains MANY different modules of various types

### Notable search modules
* whois_poc: whois point-of-contacts
* google_site_web: sub-domain search in google

