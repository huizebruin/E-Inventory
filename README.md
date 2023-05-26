![GitHub release (latest by date)](https://img.shields.io/github/v/release/huizebruin/E-Inventory?style=flat-square)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/huizebruin/E-inventory)
![GitHub repo size](https://img.shields.io/github/repo-size/huizebruin/e-inventory)
![Docker Pulls](https://img.shields.io/docker/pulls/huizebruin/e-inventory)
[![Download][download-img]][download]
![GitHub issues](https://img.shields.io/github/issues/huizebruin/e-inventory)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/huizebruin/e-inventory.svg)](https://github.com/huizebruin/e-inventory/stargazers)


<br><br>
![image](https://github.com/huizebruin/E-Inventory/blob/f494306491ca0796938ba6f583e34a3dd2663792/static/images/e-inventory-logo.png)

# E-Inventory
About E-Inventory<br>
E-Inventory is a home inventory system that helps you keep track of all your products. 
It was developed by Huizebruin using AI, Flask, and Python. With E-Inventory, you can easily see which products you have in stock, where you ordered them from, and even find documentation if you set the website links to your products.

The system is designed to make it easy to add and subtract products from your inventory. Additionally, it offers notifications for parts that are less than 10 in quantity at their location. Here's a fun message to remind you when it's time to restock your inventory:

"Hey there! It's time to restock your inventory! Don't forget to take a look at your E-Inventory to see which products are running low. This way, you can always have enough parts on hand to complete any project!"

E-Inventory is a MIT project and was created with the contribution of Said, Marco, Remco, and Lars.

## Show Your Support

⭐️ Star this project if you find it interesting or useful!

# Installation
* Clone the repo for helping it getting bigger.
* Download the zip from github. <a href="https://github.com/huizebruin/E-Inventory/archive/refs/heads/main.zip" target="_blank">Download</a>
* Unpack it
* Install pyhon above 3.10
* pip install -r requirements.txt
* If you already have a database, Move it to the main directory.
* Run app.py

# Windows exe file on v1.0.10 and later on github.

* Clone the repo for helping it getting bigger.
* Download the zip from github. <a href="https://github.com/huizebruin/E-Inventory/archive/refs/heads/main.zip" target="_blank">Download</a>
* Unpack it
* Run the exe file to start the program
* Go to <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a>
* And go add or delete your products to the database.

# installation on windows.

To install and run the E-Inventory application on Windows, follow these steps:

Prerequisites:

Make sure you have Python installed on your Windows system. 
You can download Python from the official website: 
<a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a>

During the installation process, make sure to select the option "Add Python to PATH" to ensure Python is accessible from the command prompt.
Clone the Repository:

Open the command prompt (CMD) on your Windows system.

Navigate to the directory where you want to clone the E-Inventory repository.

Run the following command to clone the repository:

```git clone https://github.com/huizebruin/E-Inventory.git```

Set Up Virtual Environment (Optional but Recommended):

Change your directory to the cloned repository:

```cd E-Inventory```

Create a virtual environment:

``` python -m venv venv```

Activate the virtual environment:

## For Command Prompt
``` venv\Scripts\activate.bat ```

## For PowerShell
``` venv\Scripts\Activate.ps1 ```

Install Dependencies:

Ensure you are in the root directory of the cloned repository (E-Inventory).

Run the following command to install the required dependencies:

```pip install -r requirements.txt```

Run the Application:

After the dependencies are installed, you can start the application.

In the command prompt, run the following command:

```python app.py```

The E-Inventory application should now be running. Open a web browser and visit <a href="http://localhost:5000" target="_blank">http://localhost:5000</a>  to access the application.

Running the Application on Boot (Windows):

To automatically start the E-Inventory application on boot, you can create a shortcut to the app.py file and place it in the Windows Startup folder.
Press Win + R on your keyboard to open the Run dialog box.
Type shell:startup and click OK. This will open the Windows Startup folder.
In the Startup folder, right-click and select "New" > "Shortcut".
In the "Create Shortcut" dialog box, browse to the location of the app.py file in the cloned repository (E-Inventory). Click Next.
Enter a name for the shortcut (e.g., E-Inventory) and click Finish.
The shortcut will now be added to the Startup folder, and the E-Inventory application will run automatically on boot.

# To install and run the E-Inventory application on Linux, follow these steps:

Prerequisites:

Make sure you have Python installed on your Linux system. Most Linux distributions come with Python pre-installed. You can check if Python is installed by running the following command in the terminal:

```python --version ```

If Python is not installed, you can install it using the package manager specific to your Linux distribution (e.g., apt for Ubuntu-based distributions, dnf for Fedora-based distributions).

Clone the Repository:

Open a terminal on your Linux system.

Navigate to the directory where you want to clone the E-Inventory repository.

Run the following command to clone the repository:

``` git clone https://github.com/huizebruin/E-Inventory.git```

Set Up Virtual Environment (Optional but Recommended):

Change your directory to the cloned repository:

```cd E-Inventory```

Create a virtual environment:

``` python3 -m venv venv ```

Activate the virtual environment:

``` source venv/bin/activate``` 

Install Dependencies:

Ensure you are in the root directory of the cloned repository (E-Inventory).

Run the following command to install the required dependencies:

``` pip install -r requirements.txt``` 

Run the Application:

After the dependencies are installed, you can start the application.

In the terminal, run the following command:

```python app.py ```

The E-Inventory application should now be running. Open a web browser and visit http://localhost:5000 to access the application.

Running the Application on Boot (Linux):

To automatically start the E-Inventory application on boot, you can create a systemd service.

Create a new service file using a text editor:

``` sudo nano /etc/systemd/system/e-inventory.service ```

In the text editor, add the following content:

``` 
[Unit]
Description=E-Inventory Application
After=network.target

[Service]
User=<your_username>
WorkingDirectory=/path/to/E-Inventory
ExecStart=/path/to/venv/bin/python /path/to/E-Inventory/app.py

[Install]
WantedBy=multi-user.target
Replace <your_username> with your actual username and update /path/to/E-Inventory with the actual path to the E-Inventory directory.
```

Save the file and exit the text editor.

Start and enable the service:

```sudo systemctl start e-inventory ```
```sudo systemctl enable e-inventory ```

The E-Inventory application will now start automatically on boot.

This should help you install and run the E-Inventory application on Linux and set it to start automatically on boot. Make sure to follow the prerequisites and steps carefully


# Docker image 
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

Once the container is running, you should be able to access the E-Inventory application by navigating to <a href="http://localhost:5000" target="_blank">http://localhost:5000</a>  in your web browser.




# Features

* exe file for windows so it's easy to start with E-Inventory
* translation to other languages 
* option to send a mail with notification for low stock off unit's.


# Some screenshots

<br>
Home screen<br>

![image](https://github.com/huizebruin/E-Inventory/assets/62996429/9ee741f8-edc3-48c8-aad0-b65d4c1503ce)

When u click on the product name u get a product information screen
<br> Product information<br>
![image](https://github.com/huizebruin/E-Inventory/assets/62996429/8562a4f4-230c-4d97-8efe-8b3001b7b929)


<br> Add component screen

![image](https://github.com/huizebruin/E-Inventory/assets/62996429/b6009676-8321-4458-8d65-35016a45591e)


<br> Notification screen<br>

![image](https://github.com/huizebruin/E-Inventory/assets/62996429/87f0dc15-fc51-4ee1-a139-9635e6a4ce5a)

<br>logbook screen<br>
![image](https://github.com/huizebruin/E-Inventory/assets/62996429/e86c4add-e0fc-445c-a915-646cfe1aba60)

<br> Settings screen <br>
![image](https://github.com/huizebruin/E-Inventory/assets/62996429/9ad31d09-e945-4f73-ad80-1a35a6c4f068)

<br> About screen <br>
![image](https://github.com/huizebruin/E-Inventory/assets/62996429/b4831015-3ee6-44ae-9af4-49774c37ff9b)

<br>

## Contributing

We welcome contributions from everyone! Please check out the Contribution Guidelines for more information on how to get involved.

## Issues

If you encounter any issues or have suggestions for improvements, please create a new issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Show Your Support

⭐️ Star this project if you find it interesting or useful!

  [download-img]: https://img.shields.io/github/downloads/huizebruin/e-inventory/total.svg
  [download]: https://github.com/huizebruin/e-inventory/releases
