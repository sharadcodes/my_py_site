---
layout: post
title: The Ultimate Windows 10 deblotter script
categories: SCRIPTS
image: /assets/uploads/win_deblot_script.png
datetime: '2019-05-23 12:14:38'
---

> It is a Script to debloat Windows 10

- - -

#### Download from the link below

[CLICK HERE TO DOWNLOAD THE SCRIPT](https://github.com/Sycnex/Windows10Debloater/archive/master.zip)

#### OR Clone using Git clone

```bash
https://github.com/Sycnex/Windows10Debloater.git
```

First of all **Huge thanks** to [**Richard Newton**](https://github.com/Sycnex) for making this script.

Now we shall see how to run the script as stated in the original docs below.

- - -

#### How To Run the Windows10Debloater.ps1 and the Windows10DebloaterGUI.ps1 files

**There are different methods of running the PowerShell script. The methods are as follows:**

**First Method:**

1. Download the .zip file on the main page of the github and extract the .zip file to your desired location
2. Once extracted, open PowerShell (or PowerShell ISE) as an Administrator
3. Enable PowerShell execution\
   ```bash
   Set-ExecutionPolicy Unrestricted -Force
   ```
4. On the prompt, change to the directory where you extracted the files:
   e.g. - 
   ```bash
   cd c:\temp
   ```
5. Next, to run either script, enter in the following:
   e.g. - 
   ```bash
   .\Windows10DebloaterGUI.ps1
   ```

**Second Method:**

1. Download the .zip file on the main page of the github and extract the .zip file to your desired location
2. Right click the PowerShell file that you'd like to run and click on "Run With PowerShell"
3. This will allow the script to run without having to do the above steps but Powershell will ask if you're sure you want to run this script.

> Remember this script NEEDS to be run as admin in order to function properly.

- - -

_**How To Run the Windows10SysPrepDebloater.ps1 file**_

For the **WindowsSysPrepDebloater.ps1** file, there are a couple of paramters that you can run so that you can specify which functions are used. 

The parameters are: 

```bash
-SysPrep, -Debloat, and -StopEdgePDF.
```

**To run this with parameters, do the following:**

1. Download the .zip file on the main page of the github and extract the .zip file to your desired location
2. Once extracted, open PowerShell (or PowerShell ISE) as an Administrator
3. On the prompt, change to the directory where you extracted the files:
   e.g. - 

```bash
cd c:\temp
```

4. Next, to run either script, enter in the following:
   e.g. - 
   ```bash
   .\Windows10SysPrepDebloater.ps1 -Sysprep, -Debloat -Privacy    and -StopEdgePDF
   ```

- - -

### Sysprep, Interactive, and GUI Application

There are now 3 versions of my Windows10Debloater - There is an interactive version, a GUI app version, and a pure silent version.

* **Windows10SysPrepDebloater.ps1** - The silent version now utilizes the switch parameters: -Sysprep, -Debloat -Privacy and -StopEdgePDF. The silent version can be useful for deploying MDT Images/sysprepping or any other way you deploy Windows 10. This will work to remove the bloatware during the deployment process.
* **Windows10Debloater.ps1** - This interactive version is what it implies - a Windows10Debloater script with interactive prompts. This one should not be used for deployments that require a silent script with optional parameters. This script gives you choices with prompts as it runs so that you can make the choices of what the script does.
* **Windows10DebloaterGUI.ps1** There is now a GUI Application named Windows10DebloaterGUI.ps1 with buttons to perform all of the functions that the scripts do. This is better for the average user who does not want to work with code, or if you'd prefer to just see an application screen. 

- - -

### The scheduled tasks that are disabled are:

XblGameSaveTaskLogon,
XblGameSaveTask,
Consolidator,
UsbCeip,
DmClient

These scheduled tasks that are disabled have absolutely no impact on the function of the OS.

- - -

### Bloatware that is removed:

3DBuilder,
Appconnector,
Bing Finance,
Bing News,
Bing Sports,
Bing Weather,
Fresh Paint,
Get started,
Microsoft Office Hub,
Microsoft Solitaire Collection,
Microsoft Sticky Notes,
OneNote,
OneConnect,
People,
Skype for Desktop,
Alarms,
Camera,
Maps,
Phone,
SoundRecorder,
XboxApp,
Zune Music,
Zune Video,
Windows communications apps,
Minecraft,
PowerBI,
Network Speed Test,
Phone,
Messaging,
Office Sway,
OneConnect,
Windows Feedback Hub,
Bing Food And Drink,
Bing Travel,
Bing Health And Fitness,
Windows Reading List,
Twitter,
Pandora,
Flipboard,
Shazam,
CandyCrush,
CandyCrushSoda,
King apps,
iHeartRadio,
Netflix,
DrawboardPDF,
PicsArt-PhotoStudio,
FarmVille 2 Country Escape,
TuneInRadio,
Asphalt8,
NYT Crossword,
CyberLink MediaSuite Essentials,
Facebook,
Royal Revolt 2,
Caesars Slots Free Casino,
March of Empires,
Phototastic Collage,
Autodesk SketchBook,
Duolingo,
EclipseManager,
ActiproSoftware,
BioEnrollment,
Windows Feedback,
Xbox Game CallableUI,
Xbox Identity Provider, and
ContactSupport.

### Credit

a60wattfish, abulgatz, xsisbest, Damian, Vikingat-RAGE, and Reddit user /u/GavinEke for the suggestions and fixes.
