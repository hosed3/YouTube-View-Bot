@echo off
title Youtube View Bot by Hosed3
color d
echo YOUTUBE VIEW BOT BY HOSED3 
echo THIS BOT IS FOR EDUCATIONAL PURPOSES oONLY
python YVB.py
echo BOT IS DONE DO U WANT START AGAIN? @_@
echo (ONLY ANSWER IS yes OR no)
set /p love=
if %love%==yes goto love
if %love%==no goto hate
:love
python YVB.py
echo BOT IS DONE DO U WANT START AGAIN? @_@
echo (ONLY ANSWER IS yes OR no)
set /p love=
if %love%==yes goto love
if %love%==no goto hate
:hate
quit