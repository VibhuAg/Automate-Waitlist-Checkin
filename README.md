# Automating the Waitlist Check-in for Testudo
This series of files will help automate the waitlist check in process for UMD. It uses the pyautogui library and the Automate app on Android to automate swipe and click gestures on both the phone and computer. The bat file can be used with the Windows task scheduler to automatically run the script at a specified time howsoever often desired.  
<br>
<br>
## Duo Bypass
Because the Waitlist check-in process through TESTUDO at UMD uses 2 factor authentication, it was necessary to use a script for the phone as well. To achieve this, I used the Automate app for Android. The .flo file can be opened and used through the Automate app. The time awaits block can be changed to whatever time is desired to run the script. One of the last blocks that opens the app may need to be modified for the individual user because their Duo app may not be in the same place mine is. If all goes well, running this file on the Automate app should open the Duo app and approve a log in request when one is sent by the other files in this project.  
<br>
## WaitlistAutomate.bat
This file is exclusively used to schedule the python script to run at a designated time everyday. This way the student doesn't have to worry about checking in for a class they've been waitlisted for and losing their spot if they forget. The file locations in the quotes should be changed in order to have the .bat file work properly. More about how to make this functional with Windows Task Scheduler can be read here: https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279  
<br>
## Waitlistscript.py
This is the python script that handles logging into TESTUDO and checking into the waitlist. Because this is run through pyautogui, some of the initial coordinates will need to be modified in order to open Chrome correctly. This script will open Chrome, open a new tab, go to TESTUDO, go to the Waitlist Check-in, and send the Duo push request. From there, the Duo Bypass script will take over to finish the log in process.
