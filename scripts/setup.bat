@echo off

REM cd to repo directory if not already
cd /d "%~dp0\.."

if not exist scripts (
   echo ERROR: Repository root not found!
   exit /b 1
)

python -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip

echo.
echo Setup complete
echo.
echo To activate venv in your terminal instance, run:
echo .venv\Scripts\activate.bat