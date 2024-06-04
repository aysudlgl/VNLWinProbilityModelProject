'''
# importing pygame
import pygame

pygame.init()

# setting window size
win = pygame.display.set_mode((500, 400))

# setting title to the window
pygame.display.set_caption("Bubble sort")

# initial position
x = 40
y = 40

# width of each bar
width = 20

# height of each bar (data to be sorted)
height = [200, 50, 130, 90, 250, 61, 110,
          88, 33, 80, 70, 159, 180, 20]

run = True


# method to show the list of height
def show(height):
    # loop to iterate each item of list
    for i in range(len(height)):
        # drawing each bar with respective gap
        pygame.draw.rect(win, (255, 0, 0), (x + 30 * i, y, width, height[i]))


# infinite loop
while run:

    # execute flag to start sorting
    execute = False

    # time delay
    pygame.time.delay(10)

    # getting keys pressed
    keys = pygame.key.get_pressed()

    # iterating events
    for event in pygame.event.get():

        # if event is to quit
        if event.type == pygame.QUIT:
            # making run = false so break the while loop
            run = False

    # if space bar is pressed
    if keys[pygame.K_SPACE]:
        # make execute flag to true
        execute = True

    # checking if execute flag is false
    if execute == False:

        # fill the window with black color
        win.fill((0, 0, 0))

        # call the height method to show the list items
        show(height)

        # update the window
        pygame.display.update()

    # if execute flag is true
    else:

        # start sorting using bubble sort technique
        for i in range(len(height) - 1):

            # after this iteration max element will come at last
            for j in range(len(height) - i - 1):

                # starting is greater than next element
                if height[j] > height[j + 1]:
                    # save it in temporary variable
                    # and swap them using temporary variable
                    t = height[j]
                    height[j] = height[j + 1]
                    height[j + 1] = t

                # fill the window with black color
                win.fill((0, 0, 0))

                # call show method to display the list items
                show(height)

                # create a time delay
                pygame.time.delay(50)

                # update the display
                pygame.display.update()

# exiting the main window
pygame.quit()
'''

from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Set up the ChromeDriver service
service = Service('/Users/aysudalogullari/Downloads/chromedriver-mac-x64/chromedriver')
driver = webdriver.Chrome(service=service)

# Function to fetch real-time teams data using Selenium
def fetch_teams_data():
    teams_data = {}

    try:
        # Open the webpage
        driver.get('https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2023/standings/women/#advanced')

        # Wait until the table is loaded
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'vbw-o-table-wrapper'))
        )

        # Get the page source and parse with BeautifulSoup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the table containing the standings
        table = soup.find('table', class_='vbw-o-table')

        # Extract the rows from the table body
        rows = table.find('tbody').find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            team_name = cells[1].text.strip()
            matches_total = int(cells[2].text.strip())
            matches_won = int(cells[3].text.strip())
            matches_lost = int(cells[4].text.strip())
            set_ratio = float(cells[14].text.strip())
            point_ratio = float(cells[17].text.strip())

            teams_data[team_name] = {
                'Matches Total': matches_total,
                'Matches Won': matches_won,
                'Matches Lost': matches_lost,
                'Set Ratio': set_ratio,
                'Point Ratio': point_ratio
            }

        # Print extracted data
        for team, data in teams_data.items():
            print(f"Team: {team}, Matches Won: {data['Matches Won']}, Matches Lost: {data['Matches Lost']}, Set Ratio: {data['Set Ratio']}, Point Ratio: {data['Point Ratio']}")

    finally:
        # Close the web driver
        driver.quit()

    return teams_data

@app.route('/api/teams', methods=['GET'])
def get_teams():
    teams_data = fetch_teams_data()
    return jsonify(teams_data)

@app.route('/api/schedule/<year>/<month>', methods=['GET'])
def get_schedule(year, month):
    base_url = 'https://en.volleyballworld.com/api/v1/globalschedule/competitions'
    url = f'{base_url}/{year}/{month}'

    response = requests.get(url)
    if response.status_code == 200:
        schedule_data = response.json()
        return jsonify(schedule_data)
    else:
        return jsonify({"error": f"Failed to retrieve data: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
