@echo off
start C:\Users\xxxxxxx\COEIROINK_WIN_CPU_v.2.3.4\COEIROINKv2.exe
powershell -ExecutionPolicy Bypass -File "./scripts/connect.ps1"

python ./scripts/check_speaker_info.py
pause
