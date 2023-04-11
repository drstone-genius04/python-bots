import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import csv

# Load the list of phone numbers from the CSV file
with open('phone_numbers.csv', 'r') as file:
    reader = csv.reader(file)
    phone_numbers = [row[0] for row in reader]

# Load the list of messages from the text file
with open('messages.txt', 'r') as file:
    messages = file.readlines()

# Set up the Selenium webdriver for WhatsApp
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=r'C:/Program Files/chromedriver.exe')
driver.get("https://web.whatsapp.com/")
input("Scan the QR code and then press Enter to continue...")
print("Logged in to WhatsApp Web!")
time.sleep(3)

# Set up the web scraper
url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
movies = soup.find_all("td", class_="titleColumn")

# Loop over the movies and send a message for each one
for i, movie in enumerate(movies):
    title = movie.find("a").text.strip()
    year = movie.find("span", class_="secondaryInfo").text.strip("()")
    
    # Construct the message to send
    message = f"Movie #{i+1}: {title} ({year})"

    # Loop over the phone numbers and send the message
    for number in phone_numbers:
        # Construct the link to open the chat window for this number
        link = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        driver.get(link)

        # Wait for the chat window to load
        time.sleep(10)

        # Find the input field for typing the message and send it
        input_box = driver.find_element(By.XPATH, "//div[contains(@class, 'selectable-text copyable-text iq0m558w')][@contenteditable='true']")
        input_box.send_keys(Keys.ENTER)
        input_box.send_keys(Keys.CONTROL, 'v')
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)

        print(f"Sent message to {number}")

# Close the browser window
driver.quit()
