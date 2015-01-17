This is the extended Version of my other plugin ADB Helper. https://github.com/techbliss/ADB_Helper_For_ida_Pro/blob/master/ADB.py



Changelog!!!

New PyQt GUI

This version have both support for native arm debugging via usb and sdk ADV manager.
Pids Direct to Ida Pro console.
Cheatsheet.
I added support for X64 targets via gdbserver.
either via pids or narmal file run.
targets like Genymotion https://www.genymotion.com/#!/
Misc
install busybox.
Rebbot phone.



Howto

have android sdk installed and added platformtools to %PATH.

Or take the minimalistic version i provided and put example c:\sdk-tool\ and add those to %PATH

Copy other folder plugins to ida and overwrite.
it will copy the ida plugin to ida\plugin folder.
And make a New folder called QtApps in ida\QtApps

start plugin from edit plugins.
after its started run it from same.

android

Follow the steps. :)

gdb follow the steps :)

you can either attach to pids or have file then just aattch to target. :)

IMPORTANT!!!.

REMEMBER to Put Your legit android_server from Hexray in the platform tools folder and the QtApps\SuperADB folder also.



