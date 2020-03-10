$username = '[USERNAME]'
$securePassword = ConvertTo-SecureString "[PASSWORD]" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential $username, $securePassword
Start-Process -FilePath [COMMAND_NAME] -ArgumentList '[CMD_ARG1]','[CMD_ARG2]',...,'[CMD_ARGN]' -Credential $credential

