#!/bin/bash
# Отключаем гашение экрана
xset s off
xset -dpms
# Запускаем ультра-лёгкий менеджер окон в фоне
openbox-session &
# Пока запускаем терминал во весь экран для тестов
exec xterm -geometry 80x24+0+0
