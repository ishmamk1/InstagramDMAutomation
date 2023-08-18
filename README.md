# InstagramDmAutomation

# Description

This program allows you to automate the process of sending direct messages to your friends on Instagram. It uses Selenium to interact with the Instagram web interface and perform actions such as logging in, navigating to the messaging section, and sending messages to specific friends.

# Prerequisites
Before using this program, make sure you have the following:

Python installed on your machine.

Chrome browser installed.

Chromedriver installed and its path configured in the PATH variable in the script.

Selenium library installed. You can install it using pip:
```bash
pip install selenium
```

# Installation
1. Clone or download this repository to your local machine.

2. Make sure you have fulfilled the prerequisites mentioned above.



# How to use the program:

1) Install selenium module through your console by using 'pip install selenium' (without apostrophes).
```bash
pip install selenium
```

2) Download chromedriver.exe through https://chromedriver.chromium.org/downloads. Make sure you download the right version of chromedriver as the update of your chrome browser. You can check through the settings and scrolling down until you find 'About Chrome'.

3) Store chromedriver in a folder where you can find the path for the application. (Will need the path to the file which can be found by right clicking the file and copying path name).

4) Open the main.py file and provide your Instagram username and password in the respective variables:

```bash
username = "your_username_or_email"
password = "your_password"
```

5) Customize the friendusers and messages lists to include the usernames of your friends and the messages you want to send.

```bash
friendusers = ['ishmam', 'hello']
messages = ["How are you doing today?", 'Wonderful weather we are having!']
```

6) Configure the path to the Chromedriver executable:

```bash
PATH = "/path/to/chromedriver"
```


7) Run the program.
```bash
python main.py
```



# How the program works (Indepth Guide):

**Importing Necessary Modules:**

1) The script begins by importing essential modules from the Selenium library, including webdriver, By, WebDriverWait, expected_conditions, and Keys.
2) It also imports the random and time modules for introducing delays.

**User Information and Configuration:**

1) Replace the username and password variables with your Instagram credentials.
2) Modify the friendusers list with the usernames of the friends you want to message.
3) Customize the messages list with the messages you want to send.

**Chromedriver Setup:**

1) Set the PATH variable to the path where the chromedriver.exe is located on your system.
2) Initialize the webdriver.Chrome instance with the specified PATH.

**Navigating to Instagram Direct Messages:**

1) The script opens the Instagram Direct Message URL using the driver.get() method.

**Logging In:**

1) The script attempts to log into your Instagram account.
2) It locates the username and password fields using WebDriverWait and sends the credentials using send_keys().
3) The "Enter" key is pressed using Keys.ENTER to submit the login.

**Handling Notifications Pop-Up:**

1) The script handles a pop-up related to notifications by locating and clicking the "Not Now" button using WebDriverWait.

**Sending Direct Messages:**

1) The script locates the "Send Message" button using WebDriverWait and clicks it.
2) It iterates through each friend in the friendusers list to send messages.

**Searching and Messaging Friends:**

1) For each friend, the script searches for their username in the search box using WebDriverWait.
2) The first option (user) is selected by clicking on it.
3) The "Next" button is clicked using WebDriverWait to proceed.

**Sending Messages:**

1) The script locates the message input box and iterates through each message in the messages list.
2) It sends each message using send_keys() and simulates pressing the "Enter" key using Keys.ENTER.

**Completing the Loop:**

1) After sending messages, the script clicks the message icon to prepare for the next friend.

**Error Handling:**

1) The script includes error handling to manage various situations such as login failures and element locators not being found.

**Exiting the Script:**

1) If an error occurs, the script prints an error message and waits briefly before exiting.
2) Commented lines indicate additional steps that can be taken, such as handling additional pop-ups.

# Warnings

1) The script may require adjustments based on Instagram's UI changes.
2) Be cautious with automating actions on websites to avoid violating their terms of service.


