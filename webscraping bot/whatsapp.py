import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Load the list of phone numbers from the CSV file
with open('phone_numbers.csv', 'r') as file:
    reader = csv.reader(file)
    phone_numbers = [row for row in reader]



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

message = "Happy birthday! Wishing you all the best on your special day."


for number in phone_numbers:
    
    link = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    driver.get(link)

    
    time.sleep(10)

    
    driver.find_element(By.XPATH, "//span[@data-testid='send' and @data-icon='send']").click()
    time.sleep(3)
    

 


    print(f"Sent message to {number}")


driver.quit()

#919619365883
