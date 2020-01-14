# RoboConWorkshop2020 - End-to-end testing through multiple interfaces

Welcome to the repository for our workshop!

[Click here to come to the presentation](https://prezi.com/view/En9AeCy2cxu7i6kOqkAi/)

## Download

If you are unfamiliar with git, I recommend you yo to download this repository as a zip file. Just click on the green *Clone or download* button and select *Download ZIP*.

## Installation Package

We have included a installation file for the libraries that we suggest that you use (you are more than welcome to use other libraries to solve the task).

To install the package in your current python enviroment, all you need to do is to run:

```
pip install -r requirements.txt
```

from inside the repository folder.

---

## Optional - Virtual Enviroment

If you don't want to install the package in your current python enviroment you can follow the instructions down below on how to set up a virtual enviroment.

---

### Windows

To create the virtual enviroment in Windows run this command in the root of the workshop directory:

```
python3 -m venv .\Python_Enviroment
```

#### Activating the virtual enviroment in cmd.exe

If you are using cmd.exe, run this command to activate the virtual enviroment:

```
.\Python_Enviroment\Scripts\activate.bat
```

After activating the enviroment you can follow the instructions up in *Installation package*. The libraries will only be installed in the virtual enviroment.

#### Activating the virtual enviroment in PowerShell

If you are using Powershell, run this command to activate the virtual enviroment:

```
.\Python_Enviroment\Scripts\Activate.ps1
```

After activating the enviroment you can follow the instructions up in *Installation package*. The libraries will only be installed in the virtual enviroment.

---

### Mac and Linux

To create the virtual enviroment in Mac or Linux run this command in the root of the workshop directory:

```
python3 -m venv /Python_Enviroment
```

To activate the enviroment run this:

```
source Python_Enviroment/bin/activate
```

After activating the enviroment you can follow the instructions up in *Installation package*. The libraries will only be installed in the virtual enviroment.