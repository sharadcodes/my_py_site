---
layout: post
title: Saving a web page using terminal
categories: LINUX
image: /assets/uploads/wget.png
datetime: '2019-06-03 08:13:00'
---
So I'm back with yet another interesting topic for today.

We all know the loading time that Chrome/Chromium/Firefox/IE or any other Web Browser usually takes but due to the Graphical interface we all love them (Except Developers!).

Today we will briefly go through the topic of this blog post i.e. saving a web page using terminal, and to do so we are going to use a simple yet powerful Linux command line tool **wget**.

---

According to the [official website](https://www.gnu.org/software/wget/)

> GNU Wget is a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS the most widely-used Internet protocols. It is a non-interactive commandline tool, so it may easily be called from scripts, cron jobs, terminals without X-Windows support, etc.

So let's get started.

- - -

1. **Checking wget is installed or not:**
   In order to check type the following command in your terminal:
   ```bash
   wget --version
   ```
   It will show some output like this:
   ```
   GNU Wget 1.19.4 built on linux-gnu.

   -cares +digest -gpgme +https +ipv6 +iri +large-file -metalink +nls 
   +ntlm +opie +psl +ssl/openssl 

   Wgetrc: 
       /etc/wgetrc (system)
   Locale: 
       /usr/share/locale 
   Compile: 
       gcc -DHAVE_CONFIG_H -DSYSTEM_WGETRC="/etc/wgetrc" 
       -DLOCALEDIR="/usr/share/locale" -I. -I../../src -I../lib 
       -I../../lib -Wdate-time -D_FORTIFY_SOURCE=2 -DHAVE_LIBSSL -DNDEBUG 
       -g -O2 -fdebug-prefix-map=/build/wget-Xb5Z7Y/wget-1.19.4=. 
       -fstack-protector-strong -Wformat -Werror=format-security 
       -DNO_SSLv2 -D_FILE_OFFSET_BITS=64 -g -Wall 
   Link: 
       gcc -DHAVE_LIBSSL -DNDEBUG -g -O2 
       -fdebug-prefix-map=/build/wget-Xb5Z7Y/wget-1.19.4=. 
       -fstack-protector-strong -Wformat -Werror=format-security 
       -DNO_SSLv2 -D_FILE_OFFSET_BITS=64 -g -Wall -Wl,-Bsymbolic-functions 
       -Wl,-z,relro -Wl,-z,now -lpcre -luuid -lidn2 -lssl -lcrypto -lpsl 
       ftp-opie.o openssl.o http-ntlm.o ../lib/libgnu.a 

   Copyright (C) 2015 Free Software Foundation, Inc.
   License GPLv3+: GNU GPL version 3 or later
   <http://www.gnu.org/licenses/gpl.html>.
   This is free software: you are free to change and redistribute it.
   There is NO WARRANTY, to the extent permitted by law.

   Originally written by Hrvoje Niksic <hniksic@xemacs.org>.
   Please send bug reports and questions to <bug-wget@gnu.org>.
   ```
   Now if you have output like the above you are good to go, otherwise you need to install **wget** by executing the following command:
   ```
   sudo apt-get install wget -y
   ```
2. **Saving an offline page using wget:**
   Before beginning this switch to your Desktop or any other directory (for beginners in linux).
   By executing :
   ```
   cd Desktop/
   ```
   Then execute:
   ```
   wget https://example.com
   ```
   After executing the following command you will have an index.html file saved in the folder you have opened your terminal.
   You can replace **https://example.com** with some other **URL**.
