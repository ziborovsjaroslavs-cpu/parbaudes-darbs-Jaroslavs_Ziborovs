$apturetie = Get-Service |
    Where-Object { $_.Status -eq "Stopped" } |
    Sort-Object Name |
    Select-Object Name, Status
    Get-Service | Where-Object {$_.Status -eq "Stopped"}
Get-Service | where Status -eq "Stopped"
gsv | where-object {$_.Status -match "Stopped|Running"}
