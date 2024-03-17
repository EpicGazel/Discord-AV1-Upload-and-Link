@echo off
setlocal enabledelayedexpansion

rem Check if a file was provided
if "%~1"=="" (
    echo Usage: %~nx0 "VIDEO-FILE"
    exit /b 1
)

rem Check if the video file exists
if not exist "%~1" (
    echo Error: Video file not found: %~1
    exit /b 1
)

rem Construct the start command
call .venv\Scripts\activate.bat
set Command=python main.py -f "%~1"

rem Execute the command
call %Command%

:end
