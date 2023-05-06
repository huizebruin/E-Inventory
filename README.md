![GitHub release (latest by date)](https://img.shields.io/github/v/release/huizebruin/E-Inventory?style=flat-square)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/huizebruin/E-inventory)
![GitHub repo size](https://img.shields.io/github/repo-size/huizebruin/e-inventory)
![GitHub](https://img.shields.io/github/license/huizebruin/e-inventory)
![Docker Pulls](https://img.shields.io/docker/pulls/huizebruin/e-inventory)
![GitHub all releases](https://img.shields.io/github/downloads/huizebruin/e-inventory/total)
![GitHub issues](https://img.shields.io/github/issues/huizebruin/e-inventory)

<br><br>
![image](https://github.com/huizebruin/E-Inventory/blob/c83cb22340e3007ff446083cc1a54936f50b14e8/static/images/icon.png)

# E-Inventory
About E-Inventory<br>
E-Inventory is a home inventory system that helps you keep track of all your parts. It was developed by Huizebruin using AI, Flask, and Python, with a sqlite3 database. With E-Inventory, you can easily see which parts you have in stock, where you ordered them from, and even find documentation.

The system is designed to make it easy to add and subtract parts from your inventory. Additionally, it offers notifications for parts that are less than 10 in quantity at their location. Here's a fun message to remind you when it's time to restock your inventory:

"Hey there! It's time to restock your inventory! Don't forget to take a look at your E-Inventory to see which parts are running low. This way, you can always have enough parts on hand to complete any project!"

E-Inventory is a MIT project and was created with the contribution of Said, Marco, Remco, and Lars.


# Installation
* Clone the repo for helping it getting bigger.
* Download the zip from github.
* Unpack it
* Install pyhon above 3.10
* pip install -r requirements.txt
* If you already have a database, Move it to the main directory.
* Run app.py
* On this moment unable te make a exe file for windows.

## docker image 
``` docker pull huizebruin/e-inventory:latest ```
* Port 5000 extern and 5000 internal ( external port may be changed but the internal not)

docker info

<a href="https://hub.docker.com/r/huizebruin/e-inventory" target="_blank">https://hub.docker.com/r/huizebruin/e-inventory</a>

To use this image, you can follow these general steps:

Install Docker on your system if it's not already installed.
You can download Docker Desktop for Windows from the Docker website at 

<a href="https://www.docker.com/products/docker-desktop" target="_blank">https://www.docker.com/products/docker-desktop</a>


Open a command prompt or terminal window and run the following command to pull the E-Inventory Docker image from Docker Hub:

```docker pull huizebruin/e-inventory```
Once the image is downloaded, you can run a Docker container using the following command:

```docker run -p 5000:5000 huizebruin/e-inventory```
This command maps port 5000 inside the container to port 5000 on the host (in this case, Windows 10).

Once the container is running, you should be able to access the E-Inventory application by navigating to ```http://localhost:5000``` in your web browser.




# Features

* exe file for windows so it's easy to start with E-Inventory
* translation to other languages 
* option to send a mail with notification for low stock off unit's.


# Some screenshots

<br>
Home screen<br>

![image](https://user-images.githubusercontent.com/62996429/235307589-85000c2c-afc9-416c-a11e-7b3108ba9264.png)


<br> Add component screen

![image](https://user-images.githubusercontent.com/62996429/235307618-87b74d35-8f5a-416b-8e51-6072dc232787.png)

<br> Notification screen<br>

![image](https://user-images.githubusercontent.com/62996429/235307641-de788ad1-4e57-4091-a81e-2b748d175bb1.png)

<br> About screen <br>

![image](https://user-images.githubusercontent.com/62996429/235307659-3e916f65-7b69-4f7a-b546-b21cc1dca94c.png)
<br>

