# RaspiWebCar

A toy car controlled by raspberry pi through web browser

## Setup Raspberry Pi

### 1. Install Raspbian OS

* Download Raspbian image from [Link](https://www.raspberrypi.org/downloads/raspbian/)
* Format Micro-SD card using [DiskGenius](http://www.diskgenius.cn/)
* Use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/files/latest/download) to write OS image on Micro-SD

### 2. Setup raspbian mirror and execute system update

* Find Raspbian mirrors from this [Link](http://www.raspbian.org/RaspbianMirrors)
* Edit "apt-get update" source: **sudo nano /etc/apt/sources.list** Comment all lines and add below two lines
  + deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main non-free contrib
  + deb-src http://mirrors.ustc.edu.cn/raspbian/raspbian/ jessie main non-free contrib
* Edit "apt-get upgrade" source, **sudo nano /etc/apt/sources.list.d/raspi.list** Comment all lines and add below line
  + deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ jessie main ui
* Update system using commands: **sudo apt-get update**, **sudo apt-get upgrade**

### 3. Setup samba share

* Install samba: **sudo apt-get install samba samba-common-bin**
* Edit samba configure: **sudo nano /etc/samba/smb.conf**
  + Find the entries for workgroup and wins support, and set them up as follows
  ```
    workgroup = your_workgroup_name
    wins support = yes
  ```
  + Add below section **_at the end of_** conf file
  ```
    [pihome]
      comment= Pi Home
      path=/home/pi
      browseable=Yes
      writeable=Yes
      only guest=no
      create mask=0777
      directory mask=0777
      public=no
  ```
* Set samba password: **sudo smbpasswd -a pi**
* See this [artical](http://raspberrywebserver.com/serveradmin/share-your-raspberry-pis-files-and-folders-across-a-network.html) for more details
* Some useful samba commands
  ```
    sudo /etc/init.d/samba start
    sudo /etc/init.d/samba stop
    sudo /etc/init.d/samba restart
    testparm
  ```

### 4. Install python Flask web framework

* sudo apt-get install python3-flask

### 5. Assembly raspberry car
* Parts list
  + Raspberry Pi 2 x 1
  + L298N x1
  + DC motor x 4
  + 5V battery (Power PI)
  + 12V battery (Power motors)

* ![wiring](https://github.com/neptune46/RaspiWebCar/blob/master/picture/wiring.jpg?raw=true)
* ![wiring](https://github.com/neptune46/RaspiWebCar/blob/master/picture/wiring2.jpg?raw=true)
* ![wiring](https://github.com/neptune46/RaspiWebCar/blob/master/picture/wiring3.jpg?raw=true)

### 6. Control program
* Frontend: HTML + JQuery/Ajax + Hammer (touch screen library)
* Backend: Flask web server
* Car Control: Python RPi.GPIO library

### 7. Connect raspberry car with android smart phone through WIFI
* To play with it outdoor where there is no router available, need to use WIFI Direct mode.
  + The easiest way is to use the "hot spot" functionality of smart phone 
  + Disable normal wifi and data network, then enable WIFI hot spot (setting SSID and password in the first time).
  + Connect raspberry car with this hot spot as usual (setting a static IP address in Raspbian if neccessary).  
  + One additional benefit of this way is, we can use phone to manage wifi connection status.

### 8. Start program and control car
  + Install SSH client JuiceSSH on android phone and login raspberry car.
  + Start program use command: "python webcar.py"
  + Open browser to connect to Flask server with specified IP address "http://192.168.43.24:3000/"
  + If success, a control pannel will be displayed in a web page. Use finger to touch on this area to control car moving.

### 9. Demo video
  + ![video](https://github.com/neptune46/RaspiWebCar/blob/master/demo/video5.gif?raw=true)