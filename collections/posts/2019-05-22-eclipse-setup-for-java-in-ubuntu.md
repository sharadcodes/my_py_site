---
layout: post
title: Eclipse setup for Java in Ubuntu 18.04+
categories: IDES
image: /assets/uploads/eclipse.png
datetime: '2019-05-22 12:13:25'
---

Before starting  the installation of Eclipse in our Ubuntu we should first check whether we have **JAVA DEVELOPMENT KIT (JDK)** installed or not, so in order to install your Eclipse successfully follow the procedure

- - -

## STEP 1

**Checking JDK is installed or not:**

Run the command below

```
java -version
```

If you get output something like

![JDK VERSION CHECK COMMAND](/assets/uploads/jdk_version_check.png "JDK VERSION CHECK COMMAND")

Then you are good to proceed to the installation **STEP 3** otherwise proceed to next step.

- - -

## STEP 2

**JDK types**

_Now before the installation you should know that there are two types of **JDK**_ _available._

1. _Open JDK_
2. _Oracle JDK_

_We will be going with Open JDK, however you can install Oracle JDK._

_Oracle JDK has some extra commercial features but for a beginner Open JDK is sufficient._

**INSTALLATION**

Run the following commands one by one

```bash
sudo apt update
```

```bash
sudo apt install default-jdk
```

```bash
sudo apt install default-jre
```

```bash
java -version
```

- - -

## STEP 3

**Eclipse installation**

Run the following command

```bash
sudo snap install --classic eclipse
```

This will install eclipse in your Ubuntu and produces following output after installation.

```bash
eclipse 4.8.0 from 'snapcrafters' installed
```

- - -

### After installation

Launch the IDE from application menu wait for some time, let it start.
No you can leave all the things and click Launch or specify any folder where all the projects have to be saved. 

**Click Launch**

![OPENING](/assets/uploads/eclipse_path.png "OPENING")

- - -

#### My eclipse screenshot with dark theme

![Eclipse](/assets/uploads/eclipse.png "Eclipse")

_Thank You !_
