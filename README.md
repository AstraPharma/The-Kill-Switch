**The Kill Switch — 3D Printed PC Panic Button
**


This project is a physical desktop “Kill Switch” for your PC. It is a 3D-printed button box that connects to your computer through USB. When pressed, it sends a keyboard shortcut to Windows. A small Python script running in the background detects that shortcut, shows a dramatic warning popup, and then force-closes open user applications.


**
Important Warning**



This project force-closes applications. Unsaved work may be lost. This is intended for your own PC as a fun desktop utility / panic button. Do not use it on someone else’s computer. Do not use it where forced application closing could cause data loss, work loss, or system problems. The script is designed to avoid critical Windows system processes, but you should still test it carefully before relying on it.



**Bill of Materials**

1 × Arduino Pro Micro ATmega32U4

1 × 6×6×5 mm tactile push button

1 × USB cable, depending on your Pro Micro port

2 × small hookup wires

4 × M3 × 8 mm screws

1x Super glue



**Filament**

Black, red and white PLA. Get creative and switch things up if you want.



**Wiring**

The wiring is very simple. The tactile button connects to GND and D2 on the Arduino Pro Micro.The Arduino uses INPUT_PULLUP, so no external resistor is needed. When the button is not pressed, the input reads HIGH. When the button is pressed, D2 is connected to GND and reads LOW.


**Set up**

1. Install Python on Windows first.



2- Sketch the Arduino code onto the controller, I used Arduino IDE.



3- Then install the required packages by running this command in command prompt:



pip install keyboard psutil pywin32



If that does not work, use:



py -m pip install keyboard psutil pywin32



Required Packages

keyboard — listens for the hotkey

psutil — finds and terminates user processes

pywin32 — closes File Explorer windows safely

tkinter — built into Python, used for the custom popup



**Running the Script**



Open PowerShell in the folder containing kill\_switch.py.

(Type powershell into the File Explorer address bar)



Paste this command inside:



py kill\_switch.py



Now press the physical button.



If everything is working, the popup will appear and your open user applications will close.



.

.

.



To generate an EXE, you will need pyinstaller. Install it with this command:



pip install pyinstaller



Then you can run this and it will generate your EXE:



pyinstaller --onefile --noconsole kill\_switch.py







**Run Automatically at Startup**



To make the Kill Switch start with Windows:



Press Win + R

Type:

shell:startup

Press Enter.

Copy kill\_switch.exe into that folder.



Now the Kill Switch will arm itself automatically every time Windows starts.

