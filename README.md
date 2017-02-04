# RaspiWebCar

A toy car controlled by raspberry pi through web browser

## Setup Raspberry Pi

### 1. Install Raspbian OS

* Download Raspbian image from [Link](https://www.raspberrypi.org/downloads/raspbian/)
* Format Micro-SD card using [DiskGenius](http://www.diskgenius.cn/)
* Use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/files/latest/download) to write OS image on Micro-SD

### 2. Setup raspbian mirror and execute system update

* Find Raspbian mirrors from this [Link](http://www.raspbian.org/RaspbianMirrors)
* Edit "apt-get update" source: **sudo nano /etc/apt/sources.list**. Comment all lines and add below two lines
  + deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main non-free contrib
  + deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main non-free contrib
* Edit "apt-get upgrade" source, **sudo nano /etc/apt/sources.d/raspi.list**. Comment all lines and add below line
  + deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ jessie main ui
* Update system using commands: **sudo apt-get update**, **sudo apt-get upgrade**

### 3. Setup samba share

* Install samba: **sudo apt-get install samba samba-common-bin**
* Set samba password: **sudo smbpasswd -a pi**
* Edit samba configure: **sudo nano /etc/samba/smb.conf**, add below section **at the end of** conf file
```
    [pishare]
    comment = RaspberryPi share folder
    path = /home/pi/share
    writeable = yes
    read only = no
    create mask = 0777
    directory mask = 0777
    browsable=yes
    public=yes
    guest ok = yes
    valid users=pi
```

