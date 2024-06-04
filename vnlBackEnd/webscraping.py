from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the ChromeDriver service
service = Service('/Users/aysudalogullari/Downloads/chromedriver-mac-x64/chromedriver')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)

try:
    # Open the webpage
    driver.get('https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2023/standings/women/#round-p')

    # Wait until the table is loaded
    WebDriverWait(driver, 100000000).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'vnl-standings__table'))
    )

    # Find the table containing the standings
    table = driver.find_element(By.CLASS_NAME, 'vnl-standings__table')

    # Extract the rows from the table body
    rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    # Loop through the rows and extract the required data
    for row in rows:
        team_name = row.find_element(By.CLASS_NAME, 'team-name').text.strip()
        # Adjust these indexes based on the actual structure
        wins = row.find_elements(By.TAG_NAME, 'td')[1].text.strip()  # Adjust index if necessary
        losses = row.find_elements(By.TAG_NAME, 'td')[2].text.strip()  # Adjust index if necessary
        print(f"Team: {team_name}, Wins: {wins}, Losses: {losses}")
finally:
    # Close the web driver
    driver.quit()
