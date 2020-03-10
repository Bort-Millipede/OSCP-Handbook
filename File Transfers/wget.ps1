param ([String]$url="",[String]$outfile="")
If($url -eq "") { $sn = $MyInvocation.MyCommand.Name; Write-Host "Usage: $sn -url [URL] [-outfile [FILENAME]]"; Exit }
If($outfile -eq "") { [array]$ss = $url.split("/"); $outfile = $ss[$ss.Count-1] }
$storageDir = $pwd
$webclient = New-Object System.Net.WebClient
$webclient.DownloadFile($url,$outfile)

