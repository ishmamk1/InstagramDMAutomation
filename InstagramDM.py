# Important modules needed to be able to access Instagram and use keys on keyboard without manual input.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import random, time

# User's information
username = "username or email"
password = "password"

# Friends to send the message to and the messages being sent.
friendusers = ['messages', 'messages 2']
messages = ["How are you doing today?", 'Wonderful weather we are having!']

# Path for the chromedriver.exe to be accessed from finder/folder.
# An example path to chromedriver.exe. You can find it through rightclicking chromedriver > option (keyboard) > copy 'chromedriver' as Pathname for Mac.
PATH = "/Users/yadayada/directory/chromedriver"

# Download correct version of chromedriver.exe for the right settings on Chrome browser.
driver = webdriver.Chrome(PATH)

# URL of the website.
url = "https://www.instagram.com/direct/inbox/"
driver.get(url)

try:
    # Logging into the user's account.
    try:
        # Finding the user/pass as well as inputting in the information.
        # Time.sleep() function used to add a delay to the inputs.
        # Find information through using inspect to find the name class as well as the full XPATH (used later on).
        usernameentry = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, 'username')))
        usernameentry.send_keys(username)
        time.sleep(random.randint(2,3))

        passentry = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, 'password')))
        time.sleep(random.randint(2, 3))
        passentry.send_keys(password)
        passentry.send_keys(Keys.ENTER)
        print("Logging in")
    except:
        print("Could not login!")


    try:
        # Created to click through various pop-ups that appear from notifications to saving login information.
        time.sleep(10)
        saveLogin = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        saveLogin.click()
        time.sleep(random.randint(4,8))

        notification = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        notification.click()
        time.sleep(random.randint(2, 3))

        # Click the 'Send Message' button to send the Direct message.
        msgPopup = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Send Message')]")))
        msgPopup.click()
        time.sleep(random.randint(2, 3))
        print('Finding the user.')
    except:
        print ("Could not find or click the direct message button")
        driver.quit()


    for frienduser in friendusers:
        # Loops through each friend in the friendusers list to send messages to each person.
        # Find information through using inspect to find the name class as well as the full XPATH.
        try:
            # Searches for the friend in friendusers list.
            searchuser = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, 'queryBox'))).send_keys(frienduser)
            time.sleep(random.randint(2, 3))

            # Selects the first option when friend is inputted in search bar.
            selectDM = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/button")))
            selectDM.click()
            time.sleep(random.randint(2, 3))

            #Clicks the next button to proceed.
            nextButton = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div")))
            nextButton.click()
            time.sleep(random.randint(2, 3))
            print('User found. Direct message sending.')

            # Once chat with friend is open, sendMsg is used to click to send the message.
            sendMsg = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))

            # Loops through each message in messages list and sends to each friend.
            for msg in messages:
                sendMsg.send_keys(msg)
                time.sleep(random.randint(2, 3))
                sendMsg.send_keys(Keys.ENTER)
            print('Direct message successfully sent.')

            # Clicks the message button again to activate the loop for the next user.
            time.sleep(random.randint(2, 3))
            clickMsgIcon = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button')))
            clickMsgIcon.click()
            time.sleep(random.randint(3,5))

        except:
            print("Wasn't able to select user or click Next.")
            driver.quit()

except:
    print("An error has occurred")
    time.sleep(1)
    driver.quit()



