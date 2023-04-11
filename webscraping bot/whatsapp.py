import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Load the list of phone numbers from the CSV file
with open('phone_numbers.csv', 'r') as file:
    reader = csv.reader(file)
    phone_numbers = [row[0] for row in reader]

# Set up the Selenium webdriver
# driver = webdriver.Chrome()

# # Log in to WhatsApp Web

# driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=r'C:/Program Files/chromedriver.exe')
driver.get("https://web.whatsapp.com/")
input("Scan the QR code and then press Enter to continue...")
print("Logged in to WhatsApp Web!")
time.sleep(3)

# Define the message to send
message = "Happy birthday! Wishing you all the best on your special day."

# Loop over the phone numbers and send the message
for number in phone_numbers:
    # Construct the link to open the chat window for this number
    link = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    driver.get(link)

    # Wait for the chat window to load
    time.sleep(10)

    # Find the input field for typing the message
    # input_box = driver.find_element_by_xpath("//div[contains(@class, 'copyable-text')][@contenteditable='true']")
    #input_box = driver.find_element(By.XPATH, "//div[contains(@class, 'selectable-text copyable-text iq0m558w')][@contenteditable='true']")
    #elem = driver.find_element(By.TAG_NAME, "body")
    # input_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    # # Type the message and send it
    # input_box.send_keys(message)
    # input_box.send_keys(Keys.ENTER)
    # clickable = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    # clickable.click()
    driver.find_element(By.XPATH, "//span[@data-testid='send' and @data-icon='send']").click()
    time.sleep(3)
    # send.click()

    # actions = ActionChains(driver)
    # actions.send_keys(Keys.ENTER)
    # actions.perform()


    print(f"Sent message to {number}")

# Close the browser window
driver.quit()

#919619365883
