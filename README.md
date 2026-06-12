1. Install Python on Windows first.



2- Sketch the Arduino code onto the controller



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

