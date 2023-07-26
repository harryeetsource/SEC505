$subnetList = Get-Content -Path 'blocklist.txt' # Please replace this with your file path

$totalIps = 0

foreach ($subnet in $subnetList) {
    $ip, $maskBits = $subnet -split "/"
    $hostBits = 32 - [int]$maskBits
    $totalIpsInSubnet = [math]::Pow(2, $hostBits) # Don't subtract 2 for total IPs including network and broadcast addresses
    $totalIps += $totalIpsInSubnet
}

$totalIps
