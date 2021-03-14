# WhatStats
View frequency of messages by different contacts in group/individual WhatsApp chats

![WhatStats Demo](/demo.png)

## ABOUT PROJECT
Started on Aug 11, 2020, WhatStats is a utlity program that can be used to view statistics of members in individual and group WhatsApp chats. v2 brings new features such as automatic date parsing, significantly faster loading times (17 seconds -> 0.02 seconds), setting intervals in minutes, hours or days, showing frequency of particular terms, miscellaneous image and message stats and much more.

I keep implementing new features as I learn more. Feedback would be appreciated.

## REQUIREMENTS:
1. [Python 3](https://www.python.org/downloads/): I use 3.9.1
2. [Matplotlib](https://matplotlib.org/): Plotting library for python. Install it using ```pip install matplotlib``` in terminal.
3. [Dateutil](https://dateutil.readthedocs.io/en/stable/): Extensions to the standard datetime module. Install it using  ```pip install python-dateutil``` in terminal.
4. [PySimpleGUI](https://pysimplegui.readthedocs.io/): GUI library for python. Install it using ```pip install pysimplegui``` in terminal.
5. [Pandas](https://pandasguide.readthedocs.io/en/latest/) and [Raccoon](https://raccoon.readthedocs.io/en/latest/): Dataframes in python. Install both using ```pip install pandas raccoon``` in terminal
6. WhatsApp exported chat in form of text file<br>
    - Open WhatsApp<br>
    - Open the required individual or group chat<br>
    - Tap the three-dot menu button, go to 'More' and select 'Export chat'<br>
    - Select 'Without Media'<br>
    - Move the exported text file to your computer<br>

## USAGE:
1. Open *'WhatStats.py'* or the compiled exe file
2. First set the date format (auto by default, or [make your own format using this](https://strftime.org/)) and interval (minutes/hours/days)
3. Then enter the path and filename of the exported chat text file,<br>
  For eg, ```C:/Users/Meghraj/Downloads/WhatsApp Chat with Openwatch.txt```,<br>
  or click on the green '+' button to add the file
4. Select the date range and the user for which you want the statistics
5. While in the graph window, use the buttons at the bottom of the window to better view the graph (pan/zoom/reset) using Left and Right Mouse Buttons, X, Y and Ctrl Keys

\
\
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)<br>
Made with :heart: by Meghraj Goswami<br>
For Terms of Service visit https://bit.ly/3aeIVfl
