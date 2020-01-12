---
layout: post
title: Accessing files of android from Linux terminal.
categories: LINUX
image: /assets/uploads/ssh_illustration.png
datetime: '2019-06-04 12:00:00'
---
In the series related to cool Linux terminal tools, I am here with yet another popular and favourite functionality used mainly by Linux administrators and geeks.
The world famous **SSH**.
- - -

According to the manual:

> ssh (SSH client) is a program for logging into a remote machine and for executing commands on a remote machine.  It is intended to provide secure encrypted communications between two untrusted hosts over an insecure network.  X11 connections, arbitrary TCP ports and UNIX-domain sockets can also be forwarded over the secure channel.
ssh connects and logs into the specified hostname .

The user must prove his/her identity to the remote machine using one of several methods.

- - -

Lets begin with our setup for connecting our android with our Linux environment.

### Step 1: Installing the android client app from Playstore
  
Head over to the official app link : [Click here](https://play.google.com/store/apps/details?id=com.arachnoid.sshelper&hl=en_IN)

  
### Step 2 : Open the app after installation
  
You will see three tabs: **LOG, CONFIGURATION & TERMINAL**
  
  
Click over **CONFIGURATION**
  
Now you will see a list stating **Application, Current Network Type, Device name and many more.**
  
Now what is important to us is the **Server address(assigned), SSH server port number** & **Server Password.**
  
   
---

Before going to next step connect your Laptop or PC with Hot-Spot  from your android mobile.
  
Now after  you will see the Server address is changed and it will be something like this:
  

```bash
176.123.12.9
```

The digits above can differ, so till now if you have accomplished everything you are good to go.


Click on the Server Password row in your app to edit the default **password**. 


**Change it to a new password.**

---

### Step: 3. Executing command in our terminal
  
Execute the following command in terminal :

```bash
ssh 176.123.12.9 -p 2222
```

Change **176.123.12.9** with the **server address** that is shown in your app after connecting Hot-Spot with the PC or laptop and the **2222** with the **SSH server port number** shown in your app.

 
Now press enter to execute the command.
 

If everything is fine you will get something like this:   

```bash
ssh 176.123.12.9 -p 2222
SSHelper Version 12.5 Copyright 2018, P. Lutus
sharad@176.123.12.9's password:
```

**Now enter the password that you entered in your app in Server Password**
You will see that your domain name has changed, in my case it shows first my device model name then the new domain :   

```bash   
sharad@ubuntu:~$ ssh 176.123.12.9 -p 2222
SSHelper Version 12.5 Copyright 2018, P. Lutus
sharad@176.123.12.9's password: 
ASUS_X00TD:4.4.78-perf+u0_a482@localhost:~$
```

Now press **ls**  and then enter to see the memory that you can access.
  
Usually it is restricted to internal memory but due to some bugs it shows SDCard instead of Internal Storage.

- - -

Here is a screenshot of my terminal:
![SSH](/assets/uploads/ssh.png "SSH")
I have blurred out my IP and some folders for privacy concerns.
Now you can copy,move, delete as usual from command line. 

- - -

Hope you enjoyed, see you soon !
