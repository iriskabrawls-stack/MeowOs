#!/bin/bash
# Отключаем гашение экрана
xset s off
xset -dpms

# Запускаем dbus (ещё не запущен в среде openbox)
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
    eval $(dbus-launch --sh-syntax --exit-with-session)
fi

# Запускаем ультра-легкий менеджер окон
openbox-session &

# Терминал для отладки (при его закрытии X-сессия завершится)
exec xterm -geometry 80x24+0+0
