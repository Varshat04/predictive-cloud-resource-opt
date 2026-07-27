@echo off
title CloudOptimizer - Startup Script

:: 1. to_start_backend
echo Starting AI Backend Server...
cd backend
start cmd /k "env\Scripts\activate && python app.py"

:: 2. time_for_server_load
timeout /t 5 /nobreak

:: 3. to_open_frontend
echo Opening AI Dashboard...
start "" "..\frontend\login.html"

echo.
echo ✅ System is running!
pause