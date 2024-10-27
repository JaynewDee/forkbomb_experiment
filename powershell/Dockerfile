# Use a PowerShell-enabled Windows Server Core or Linux image
FROM mcr.microsoft.com/powershell:latest

# Copy the PowerShell script into the container
COPY forkbomb.ps1 /usr/local/bin/forkbomb.ps1

# Execute 
CMD ["pwsh", "/usr/local/bin/forkbomb.ps1"]
