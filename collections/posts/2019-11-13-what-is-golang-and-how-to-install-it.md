---
layout: post
title: What is Golang and how to install it
categories: GOLANG
author: Sharad Raj
image: /assets/uploads/go.png
date: '2019-11-13 12:00:00'
---
What is Golang ?, a quick intro as well as its installation on Windows will be covered in this article. However I will expand this article to linux installation as well.

Let's get started

- - -

Well Go as the word suggests it is developed by Google. Go was developed in 2007 by Robert Griesemer, Rob Pike, and Ken Thompson.

They describe it as

> “Go was born out of frustration with existing languages and environments for systems programming.”

Or in a nutshell it is a procedural, open-source, super clean, blazing fast, flexible and an easy to maintain programming language.

> So what can the Go lang do? 

Well to answer this question here is a list of tech giants and how they use GO.

1. Google: Google uses it to write many of its internal services, the source for Chrome, Android SDK etc are written in Go.
2. Medium: Their Neo4j database is having services written in Go for managing.
3. Uber: The rides you book are being managed by services written in Go

And many more giants like BBC, Docker etc use GO as their go to language.

Hugo is a popular static site generator written in go.

Examples are endless ...

- - -

Now without further wait lets quickly jump on to the installation section.

I will be covering Windows installation for now.

- - -

## Go Installation for Windows

### Step 1: Downloading the Go lang MSI installer

```bash
System requirements are:
1. Windows 7, Server 2008R2 or later
2. Architecture: amd64, 386
```

The Go project provides two installation options for Windows users (besides installing from source): a zip archive that requires you to set some environment variables and an MSI installer that configures your installation automatically

We will go with the MSI installer as it is easy for a beginner.

First of all open this link: <https://golang.org/dl/>

This will open a page like the one shown below in the screenshot.

![](/assets/uploads/gowin1.png)

Click on the link highlighted using in the red box. This will start download of MSI installer for GO.

### Step 2: Installing GO using MSI installer

Open the MSI file and follow along with me.

If you are on Windows 8,8.1 or 10 you might get a dialog like this.

![](/assets/uploads/wingo1.png)

**Just click on Run**

Now wait for the installer to load, after some time it will show something like this as shown in the below screenshot.

![](/assets/uploads/wingo2.png)

Click on next.

Now accept the license by ticking the check box and clicking next.

![](/assets/uploads/wingo3.png)

Now it will ask for the folder in which the Go lang should be installed. 

By default it is `C:\Go\`

Leave it as default and click Next

![](/assets/uploads/wingo4.png)

Now after this click on install button:

![](/assets/uploads/wingo5.png)

Now it will prompt you to allow the admin rights so click on next on that prompt:

![](/assets/uploads/wingo7.jpeg)

Now if everything is right it will take approx 1 minute to install.

You will see the window like the one below this after the successful install, click on finish.

![](/assets/uploads/wingo8.png)

- - -

Woo hooo, that's it the installation part is completed. :smile:

- - -

## Testing GO installation

Your system must be ready to run GO now but a test is always good.

So quickly open up your command prompt and type

```bash
go
```

If you see the output on cmd like the screenshot below. It means you are good to GO :thumbsup:

![](/assets/uploads/wingo9.png)

- - -

Huge thanks  :heart: to Hitesh Sir for giving the oppurtunity to share something with the community.
