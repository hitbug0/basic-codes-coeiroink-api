$maxAttempts = 100
$waitTimeSeconds = 0.5

for ($i = 1; $i -le $maxAttempts; $i++) {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:50032/docs" -Method Head
        if ($response.StatusCode -eq 200) {
            Write-Host "HTTP connection successful: HTTP status code 200 OK"
            break
        } else {
            Write-Host "HTTP connection succeeded, but the HTTP status code is not 200."
        }
    } catch {
        Write-Host "waiting for HTTP connection..."
    } finally {
        Start-Sleep -Seconds $waitTimeSeconds
    }
}

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
Start-Process -FilePath $chromePath -ArgumentList "http://localhost:50032/docs"
