@echo off

REM cd to repo directory if not already
cd /d "%~dp0\.."

if not exist scripts (
   echo.
   echo ERROR: Repository root not found!
   exit /b 1
)

echo Creating virtual environment...
python -m venv .venv

echo Upgrading pip...
.venv\Scripts\python.exe -m pip install --upgrade pip

echo Installing requirements...
if not exist requirements.txt (
   echo.
   echo ERROR: requirements.txt not found!
   exit /b 1
)
.venv\Scripts\python.exe -m pip install -r requirements.txt

echo.
echo Setup complete
echo.
echo To activate venv in your terminal instance, run:
echo .venv\Scripts\activate.bat