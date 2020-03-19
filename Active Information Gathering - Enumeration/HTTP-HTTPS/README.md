# HTTP/HTTPS Enumeration

## Table of Contents
* [Standard Ports](#standard-ports)
* [nikto](#nikto)
* [dirb](#dirb)
* [gobuster](#gobuster)
* [wpscan](#wpscan)
* [joomscan](#joomscan)
* [Eyewitness](#eyewitness)
* [Nmap scripts](#nmap-scripts)
* [Crawling](#crawling)


## Standard Ports
TCP 80, 443 (SSL/TLS), 8080, 8443 (SSL/TLS)


## nikto
Automated web scanner

### Options
```
-host [HOST]: target host
-port [PORT]: target port
-ssl: use SSL/TLS
-root [ROOT_DIR]: start directory to scan from (default /)
-vhost [VHOSTNAME]: specify Host header
-output [FILE]: output file (.txt extension)
```

### Usage
```
nikto -host [HOST] -port [PORT] -ssl -output [HOST]-nikto.txt
```


## dirb
Brute force web directories

### Options
```
-w: ignore errors
-p [HOST]:[PORT]: Use proxy located at [HOST]:[PORT]
```

### Usage
```
dirb http://site [WORDLIST_FILE] [OPTIONS]
dirb https://site [WORDLIST_FILE] [OPTIONS]
```


## gobuster
Brute force web directories

### Options
```
-u: target base URL
-w: wordlist to use
-e: print full URLs
-t [NUM]: use [NUM] concurrent threads
-x [STRING]: file extension(s) to search for
```


## wpscan
WordPress Security Scanner

### Options
```
--url: target URL
--enumerate [OPTION]:
	p: enumerate plugins
	vp: enumerate only vulnerable plugins
	ap: enumerate all plugins
	t: enumerate themes
	vt: enumerate vulnerable themes
	at: enumerate all themes
	u: enumerate users
--wp-content-dir [DIR]: use custom content dir for scanning
--wp-plugins-dir [DIR]: use custom plugins dir for scanning
```


## joomscan
Joomla Security Scanner

### Options
```
-u: target URL
-ec: enumeration components
--cookie: cookies to send with requests
-a: user-agent to send with requests
--random-agent: send random user-agent headers
```


## Eyewitness
Tool used to capture webpage screenshots from a list of URLs.

### Options
```
--web: screenshot HTTP/HTTPS using Selenium
--headless: screenshot HTTP/HTTPS using PhantonJS
-f [FILE]: screenshot all URLs contained in [FILE]
--no-dns: skip DNS resolution for URLs
```


## Nmap scripts
* \*http\*vuln\*: All HTTP/HTTPS vulnerability scanning scripts
  * http-huawei-hg5xx-vuln
  * http-iis-webdav-vuln: Checks for a vulnerability in IIS 5.1/6.0 that allows arbitrary users to access secured WebDAV folders
  * http-vmware-path-vuln: Checks for a path-traversal vulnerability in VMWare ESX, ESXi, and Server (CVE-2009-3733)
  * http-vuln-cve2006-3392
  * http-vuln-cve2009-3960
  * http-vuln-cve2010-0738
  * http-vuln-cve2010-2861: Adobe ColdFusion
  * http-vuln-cve2011-3192
  * http-vuln-cve2011-3368
  * http-vuln-cve2012-1823
  * http-vuln-cve2013-0156
  * http-vuln-cve2013-6786
  * http-vuln-cve2013-7091
  * http-vuln-cve2014-2126
  * http-vuln-cve2014-2127
  * http-vuln-cve2014-2128
  * http-vuln-cve2014-2129
  * http-vuln-cve2014-3704
  * http-vuln-cve2014-8877
  * http-vuln-cve2015-1427
  * http-vuln-cve2015-1635
  * http-vuln-cve2017-1001000
  * http-vuln-cve2017-5638
  * http-vuln-cve2017-5689
  * http-vuln-cve2017-8917
  * http-vuln-misfortune-cookie: Detects the RomPager 4.07 Misfortune Cookie vulnerability by safely exploiting it.
  * http-vuln-wnr1000-creds: vulnerability on WNR 1000 firmware version V1.0.2.60_60.0.86 and V1.0.2.54_60.0.82NA
* http-adobe-coldfusion-apsa1301: Attempts to exploit an authentication bypass vulnerability in Adobe Coldfusion servers to retrieve a valid administrator's session cookie.
* http-affiliate-id
* http-apache-negotiation
* http-apache-server-status
* http-aspnet-debug
* http-auth-finder
* http-auth
* http-avaya-ipoffice-users
* http-awstatstotals-exec
* http-axis2-dir-traversal
* http-backup-finder
* http-barracuda-dir-traversal
* http-bigip-cookie
* http-brute
* http-cakephp-version
* http-chrono
* http-cisco-anyconnect
* http-coldfusion-subzero
* http-comments-displayer
* http-config-backup
* http-cookie-flags
* http-cors
* http-cross-domain-policy
* http-csrf
* http-default-accounts: Tests for access with default credentials used by a variety of web applications and devices.
* http-devframework
* http-dlink-backdoor
* http-dombased-xss
* http-domino-enum-passwords
* http-drupal-enum
* http-drupal-enum-users
* http-errors
* http-favicon
* http-feed
* http-fetch
* http-fileupload-exploiter
* http-form-brute
* http-form-fuzzer
* http-frontpage-login
* http-generator
* http-git
* http-gitweb-projects-enum
* http-google-malware
* http-grep
* http-headers
* http-icloud-findmyiphone
* http-icloud-sendmsg
* http-iis-short-name-brute
* http-internal-ip-disclosure
* http-joomla-brute
* http-jsonp-detection
* http-litespeed-sourcecode-download
* http-ls
* http-majordomo2-dir-traversal
* http-malware-host
* http-mcmp
* http-methods
* http-method-tamper
* http-mobileversion-checker
* http-ntlm-info
* http-open-proxy
* http-open-redirect
* http-passwd
* http-phpmyadmin-dir-traversal
* http-phpself-xss
* http-php-version
* http-proxy-brute
* http-put
* http-qnap-nas-info
* http-referer-checker
* http-rfi-spider
* http-robots
* http-robtex-reverse-ip
* http-robtex-shared-ns
* http-security-headers
* http-server-header
* http-shellshock
* http-slowloris-check
* http-slowloris
* http-stored-xss
* http-svn-enum
* http-svn-info
* http-tplink-dir-traversal
* http-trace
* http-traceroute
* http-trane-info
* http-title: Shows the title of the default page of a web server
* http-unsafe-output-escaping
* http-useragent-tester
* http-userdir-enum: Attempts to enumerate valid usernames on web servers running with the mod_userdir module or similar enabled.
* http-vhosts: Searches for web virtual hostnames by making a large number of HEAD requests against http servers using common hostnames.
* http-virustotal
* http-vlcstreamer-ls
* http-waf-detect
* http-waf-fingerprint
* http-webdav-scan: A script to detect WebDAV installations
* http-wordpress-brute
* http-wordpress-enum
* http-wordpress-users
* http-xssed: This script searches the xssed.com database and outputs the result.
* ip-https-discover
* membase-http-info
* riak-http-info


## Crawling

### wget 
Automatically crawl [BASE_URL], and save all crawled files/directories into a newly-create directory named after [BASE_URL]:
```
wget --mirror [BASE_URL]
```

Automatically crawl [BASE_URL], and save all results to one file (to likely be deleted soon after):
```
wget --mirror [BASE_URL] -O [FILE]
```

### curl
Automatically crawl a list of URLs read from file [FILE_CONTAINING_FULL_URLS].
```
for l in $(cat [FILE_CONTAINING_FULL_URLS]); do curl -L -i -s -k -X 'GET' "$l" >/dev/null; done
```
Proxying this command through Burp Suite using the ```http_proxy``` and ```https_proxy``` environment variables is highly recommended.

### Nmap scripts
* http-sql-injection: Spiders an HTTP server looking for URLs containing queries vulnerable to an SQL injection attack
* http-exif-spider: Spiders a site's images looking for interesting exif data embedded in .jpg files.
* http-enum: Enumerates directories used by popular web applications and servers.
* http-sitemap-generator: Spiders a web server and displays its directory structure along with number and types of files in each folder.
  * Example options (if crawling directory other than base directory): ```--script http-sitemap-generator --script-args url=/[URL]```

### Burp Suite Free Spider
Burp Suite Free (prior to v2.x) provides some automated crawling functionality using the "Spider" tool.


