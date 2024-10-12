# CRUD example with Flask + RethinkDB + Schema + YML

It's just that: a CRUD example with Flask + RethinkDB + Schema + YML. This project has been developed in Windows 11 using WSL2 with the Ubuntu-22.04 distribution.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes.

### Prerequisites

You need a working environment with:
* [Visual Studio Code](https://code.visualstudio.com/) - The Editor used in this project
* [Git](https://git-scm.com) - You can install it from https://git-scm.com/downloads.
* [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) - The Windows Subsystem for Linux (WSL) lets developers install a Linux distribution (such as Ubuntu, OpenSUSE, Kali, Debian, Arch Linux, etc) and use Linux applications, utilities, and Bash command-line tools directly on Windows, unmodified, without the overhead of a traditional virtual machine or dualboot setup.
* [Ubuntu-22.04](https://releases.ubuntu.com/jammy/) - Ubuntu 22.04.5 LTS (Jammy Jellyfish).
* [Python3](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively.
* [pip3]() - pip3 is a command line tool for installing Python 3 modules.
* [venv](https://docs.python.org/3/library/venv.html) - The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories.
* [RethinkDB](https://rethinkdb.com/) - RethinkDB is the open-source, scalable database that makes building realtime apps dramatically easier.

## General Installation instructions for WSL

You can now install everything you need to run WSL with a single command. Open PowerShell or Windows Command Prompt in administrator mode by right-clicking and selecting "Run as administrator", enter the wsl --install command, then restart your machine.

````
PS C:\WINDOWS\system32>wsl --install
````

To show all distributions available in WSL2:

````
PS C:\WINDOWS\system32>wsl --list --online
````

For this project I have used the WSL2 virtual machine Ubuntu-22.04. To install it:

````
PS C:\WINDOWS\system32>wsl --install Ubuntu-22.04
````

## General Installation instructions for Python and Pip

In a WSL2 Ubuntu-22.04 console:

````
$ sudo apt update
$ sudo apt upgrade
$ python3 --version
$ pip3 --version
````

if is not installed then:

````
$ sudo apt install python3 python3-pip -y
````

## General Installation instructions for VENV

VENV lets you work in an independent virtual environment. To install it open a WSL2 Ubuntu-22.04 console:

````
$ sudo apt install python3-venv -y
````

## General Installation instructions for RethinkDB

I have used the WSL Ubuntu-22.04 terminal in Visual Studio Code in my Windows 11.

I have followed the instructions in the official RethinkDB page https://rethinkdb.com/docs/install/ubuntu/ for Ubuntu-22.04:

````
$ source /etc/lsb-release && echo "deb https://download.rethinkdb.com/repository/ubuntu-$DISTRIB_CODENAME $DISTRIB_CODENAME main" | \
    sudo tee /etc/apt/sources.list.d/rethinkdb.list
$ wget -qO- https://download.rethinkdb.com/repository/raw/pubkey.gpg | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get install rethinkdb
````

after that you can check the version of your installation

````
$ rethinkdb --version
````

## Start using this project

First of all clone this project from a WSL2 Ubuntu-22.04 console:

```
$ git clone https://github.com/tcrurav/FlaskRethinkDBSchemaYML.git
```

Enter in the directory of the project:

````
$ cd FlaskRethinkDBSchemaYML
````

Create a virtual environment:

````
$ python3 -m venv venv
````

Activate the new created virtual environment:

````
$ source venv/bin/activate
````

Now install all the requirements of the project:

````
$ pip install requirements.txt
````

Create a new WSL2 Ubuntu-22.04 console from Visual Studio Code, then go to the same directory of the project and activate the virtual environment as well:

````
$ cd FlaskRethinkDBSchemaYML
$ source venv/bin/activate
````

Now run RethinkDB:

````
$ rethinkdb
````

In the other WSL2 Ubuntu-22.04 you had clone the project you can now run the project:

````
$ flask run
````

Enjoy!!!

## Test it with POSTMAN

Test this example with the following end-points available here:
https://documenter.getpostman.com/view/3446841/2sAXxJiab6

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - The Editor used in this project
* [Git](https://git-scm.com) - You can install it from https://git-scm.com/downloads.
* [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) - The Windows Subsystem for Linux (WSL) lets developers install a Linux distribution (such as Ubuntu, OpenSUSE, Kali, Debian, Arch Linux, etc) and use Linux applications, utilities, and Bash command-line tools directly on Windows, unmodified, without the overhead of a traditional virtual machine or dualboot setup.
* [Ubuntu-22.04](https://releases.ubuntu.com/jammy/) - Ubuntu 22.04.5 LTS (Jammy Jellyfish).
* [Python3](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively.
* [pip3]() - pip3 is a command line tool for installing Python 3 modules.
* [venv](https://docs.python.org/3/library/venv.html) - The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories.
* [RethinkDB](https://rethinkdb.com/) - RethinkDB is the open-source, scalable database that makes building realtime apps dramatically easier.

## Acknowledgements

* https://gist.github.com/PurpleBooth/109311bb0361f32d87a2. A very complete template for README.md files.
* https://dev.to/emma_donery/python-dotenv-keep-your-secrets-safe-4ocn. the file .env explained to work in a python environment.