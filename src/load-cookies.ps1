#!/usr/bin/env pwsh
Clear-Host
Write-Host "`nGet cookies from https://skillshare.com.
for help with this see the git repo.`n"
$cookie_raw = Read-Host "Paste your cookies here" # prompt the user for input

if ( $cookie_raw -eq "" ) {
    Clear-Host
    Write-Host "error: input string is empty"
    exit 1
}

Write-Host "Working..."
$cookie = "cookie = `"" + $cookie_raw + "`""
Write-Output $cookie > ./cookie.py

Clear-Host
Write-Host "Done`n"