#!/bin/bash

# Kill Appium cũ nếu còn chạy
pkill -f appium

echo "Starting Appium server for device 47c92427 on port 4723..."
appium -p 4723 --session-override --base-path /wd/hub > appium_device1.log 2>&1 &

echo "Starting Appium server for device AHB00009462 on port 4725..."
appium -p 4725 --session-override --base-path /wd/hub > appium_device2.log 2>&1 &

echo "✅ 2 Appium servers started!"
echo "- Device 47c92427 → http://127.0.0.1:4723/wd/hub"
echo "- Device AHB00009462 → http://127.0.0.1:4725/wd/hub"
