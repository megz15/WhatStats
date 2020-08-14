# WhatStats
View frequency of messages by different contacts in group/individual WhatsApp chats (among other planned stuff)

![WhatStats Demo](/demo.png)

## ABOUT PROJECT
WhatStats v1.0. Can be used to view frequency of individual or group chats. It's in a really primitive state but I hope to improve it further. 
<br>Tasks:<br>
- [x] Actually start with the project   (Aug 11, 2020)
- [x] Implementing GUI using tkinter    (Aug 14, 2020)
- [x] Set frequency intervals           (Aug 14, 2020)
- [ ] Create graph for frequency of particular string in chat
- [ ] Show misc info like most frequently used characters/phrases, most active users and days/times with most activity etc
- [ ] Live plotting of graph

This would all come slowly as I'm implementing features as I'm learning them. Feedback would be appreciated.

## REQUIREMENTS:
1. [Python 3](https://www.python.org/downloads/): I use 3.7.7
2. [Matplotlib](https://matplotlib.org/): Plotting library for python. Install it using ```pip install matplotlib``` in Command Prompt.
3. WhatsApp exported chat in form of text file<br>
    - Open WhatsApp<br>
    - Open the required individual or group chat<br>
    - Tap the three-dot menu button, go to 'More' and select 'Export chat'<br>
    - Select 'Without Media'<br>
    - Move the exported text file to your computer<br>

## USAGE:
1. Open *'WhatStats.py'*
2. Enter the path and filename of the exported chat text file,<br>
  For eg, ```C:/Users/Meghraj/Downloads/WhatsApp Chat with Openwatch.txt```
    > Note: Preferably don't rename the text file for optimal results
3. Press enter and wait for graph to form
4. Use the buttons at the bottom of the Window to better view the graph (pan/zoom/reset) using Left and Right Mouse Buttons, X, Y and Ctrl Keys

\
\
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)<br>
Made with :heart: by Meghraj Goswami<br>
For Terms of Service visit https://bit.ly/3aeIVfl
