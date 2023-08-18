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

-The script begins by importing essential modules from the Selenium library, including webdriver, By, WebDriverWait, expected_conditions, and Keys.
-It also imports the random and time modules for introducing delays.

**User Information and Configuration:**

-Replace the username and password variables with your Instagram credentials.
-Modify the friendusers list with the usernames of the friends you want to message.
-Customize the messages list with the messages you want to send.

**Chromedriver Setup:**

-Set the PATH variable to the path where the chromedriver.exe is located on your system.
-Initialize the webdriver.Chrome instance with the specified PATH.

**Navigating to Instagram Direct Messages:**

-The script opens the Instagram Direct Message URL using the driver.get() method.

**Logging In:**

-The script attempts to log into your Instagram account.
-It locates the username and password fields using WebDriverWait and sends the credentials using send_keys().
-The "Enter" key is pressed using Keys.ENTER to submit the login.

**Handling Notifications Pop-Up:**

-The script handles a pop-up related to notifications by locating and clicking the "Not Now" button using WebDriverWait.

**Sending Direct Messages:**

-The script locates the "Send Message" button using WebDriverWait and clicks it.
-It iterates through each friend in the friendusers list to send messages.

**Searching and Messaging Friends:**

-For each friend, the script searches for their username in the search box using WebDriverWait.
-The first option (user) is selected by clicking on it.
-The "Next" button is clicked using WebDriverWait to proceed.

**Sending Messages:**

-The script locates the message input box and iterates through each message in the messages list.
-It sends each message using send_keys() and simulates pressing the "Enter" key using Keys.ENTER.

**Completing the Loop:**

-After sending messages, the script clicks the message icon to prepare for the next friend.

**Error Handling:**

-The script includes error handling to manage various situations such as login failures and element locators not being found.

**Exiting the Script:**

-If an error occurs, the script prints an error message and waits briefly before exiting.
-Commented lines indicate additional steps that can be taken, such as handling additional pop-ups.


