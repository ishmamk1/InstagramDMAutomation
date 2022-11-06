# InstagramDmAutomation

# How to use the program:

1) Install selenium module through your console by using 'pip install selenium' (without commas).

2) Download chromedriver.exe through https://chromedriver.chromium.org/downloads. Make sure you download the right version of chromedriver as the update of your chrome browser. You can check through the settings and scrolling down until you find 'About Chrome'.

3) Store chromedriver in a folder where you can find the path for the application.

4) Download the code and edit it through a programming editor. Change the username, password, messages, and friends you want to message. Paste in your path to the chromedriver as well. 

5) Run the program.


# How the program works:

- The program opens up 'https://www.instagram.com/' and inputs your username and password. It then uses the send_keys() function from selenium.webdriver.common.keys to click the 'Enter' key for you.

- Instagram then prompts two pop-ups regarding saving your login and managing notiflications, which can be bypassed by finding the full XPATH of the 'Not Now' button and creating a string of code that allows the program to locate it. The click() function is used to click the button located to proceed to the next step.

- Same process is used to find the 'Send Message' button which is clicked. Another pop-up is displayed where it asks you to input the information of the user you want to send the message to. After copying the XPATH of the search button, a loop for each friend in the friendusers list inputs the friend's username and sends a direct message.

- After the direct message is sent, the script clicks the Message button to prompt the loop to move onto the next friend in the list, repeating the process. It will keep repeating until all the messages have been sent to each friend in the list.
