---
layout: post
title: Running JAVA programs from Notepad++
categories: SCRIPTS
image: /assets/uploads/run_java.jpg
datetime: '2019-06-13 12:00:00'
---
While I was 
learning Java (just the basics) I didn't liked the cumbersome IDEs and to solve this problem I decided to make a batch file to run the java programs from Notepad++.
So today I am here with the guide to use the batch file I made for running java from Notepad++

- - -

## How to use ?

1. First of all download the batch file:
   To download the file [Click here](https://raw.githubusercontent.com/sharadcodes/run_java_bat/master/run_java.bat) and then save it using `CTRL+S`
2. Now download Notepad++ if you don't have it installed
   * [Click here for x86](https://notepad-plus-plus.org/repository/7.x/7.7/npp.7.7.Installer.exe)
   * [Click here for x64](https://notepad-plus-plus.org/repository/7.x/7.7/npp.7.7.Installer.x64.exe)
3. Now open the Notepad++ and press F5 key. A dialog box appears, copy and paste the following into the text box:
   ```bash
   run_java  "$(FULL_CURRENT_PATH)"
   ```
   Now press save.
   After it tick the following keys CTRL, SHIFT & ENTER 
   Give it a name and save it.
4. Now we need to create a folder, to put the file you just downloaded into it. Create a folder at a safe location in any if your drive, and the move the file run_java.bat inside it.
5. Now we need to add it to the `SYSTEM ENVIRONMENT VARIABLES`, so to do this right click on **My Computer in Windows 7 or This PC in Windows 10**, Goto -> Properties -> Advance Options -> Environmnet Variable. Inside path click **NEW** now copy the path of the folder that you made in which you moved the runcpp.bat file & paste it here in new path and save it.
6. Now you can open a Java Source file and press Ctrl+Shift+Enter to compile and run the Java File

- - -

SCREENSHOT OF A SIMPLE PROGRAM WHICH COMPILED AND RAN USING MY BATCH FILE AFTER PRESSING `CTRL+SHIFT+ENTER`

![RUN_JAVA.BAT EXAMPLE](/assets/uploads/run_java.jpg "RUN_JAVA.BAT EXAMPLE")

- - -

If there is any problem you can contact me via contact me link in menu above.

**Thank You**
