from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up WebDriver
driver_path = "/path/to/chromedriver"  # <- Change this
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open browser in maximized mode
driver = webdriver.Chrome(service=service, options=options)

# The Facebook page URL you want to generate reports for
facebook_page_url = "https://www.facebook.com/share/18JiTfeTnd/"

def login_to_facebook():
    try:
        logging.info("Opening Facebook login page...")
        driver.get("https://www.facebook.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

        # Login
        email_field = driver.find_element(By.ID, "email")
        pass_field = driver.find_element(By.ID, "pass")

        email_field.send_keys("your_email_here")  # Replace with your email
        pass_field.send_keys("your_password_here")  # Replace with your password
        pass_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        logging.info("Logged into Facebook.")
    except Exception as e:
        logging.error("Login failed:", exc_info=True)
        driver.quit()
        raise e

def generate_report_for_page(report_num):
    try:
        logging.info(f"Generating report #{report_num} for {facebook_page_url}...")
        driver.get(facebook_page_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Capture screenshot with a unique filename
        screenshot_path = f"screenshots/facebook_report_{report_num}.png"
        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved: {screenshot_path}")

        # Optionally: Count links and buttons (can be expanded for other elements)
        links = driver.find_elements(By.TAG_NAME, "a")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        logging.info(f"Found {len(links)} links and {len(buttons)} buttons on the page.")

        # Save page summary in a text file
        with open(f"reports/facebook_report_{report_num}.txt", "w") as report_file:
            report_file.write(f"Report #{report_num} for {facebook_page_url}\n")
            report_file.write(f"Links found: {len(links)}\n")
            report_file.write(f"Buttons found: {len(buttons)}\n")

    except Exception as e:
        logging.error(f"Failed to generate report #{report_num} for {facebook_page_url}", exc_info=True)

# Create directories if they don't exist
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")
if not os.path.exists("reports"):
    os.makedirs("reports")

# Login to Facebook first
login_to_facebook()

# Generate 1000 reports for the same Facebook page
for report_num in range(1, 1001):
    generate_report_for_page(report_num)

# Quit the driver after completing the tasks
driver.quit()
logging.info("All tasks completed.")