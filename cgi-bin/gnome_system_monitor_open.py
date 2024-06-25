#!/usr/bin/env python3

import os
import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n")
print("<html><body>")

try:
    # Define the display variable
    display = ":0"

    # Command to open GNOME System Monitor as the correct user
    command = f'sudo -u root DISPLAY={display} gnome-system-monitor &'

    # Execute the command
    os.system(command)

    print("<p>GNOME System Monitor has been opened.</p>")
except Exception as e:
    print(f"<p>Error: {str(e)}</p>")

print("</body></html>")
