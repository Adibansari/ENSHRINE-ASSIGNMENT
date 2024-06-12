from openai import OpenAI
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_dummy_data(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.0,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Please generate data that is asked in the prompt, nothing more or less."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_valid_email():
    email = ""
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email = generate_dummy_data("Generate a valid random email address without additional comments.")
    return email

def generate_valid_phone():
    phone = ""
    while not re.match(r"\(\d{3}\) \d{3}-\d{4}", phone):
        phone = generate_dummy_data("Generate a valid random phone number in the format (XXX) XXX-XXXX without additional comments.")
    return phone

def fill_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://form.jotform.com/241617189501153")
    wait = WebDriverWait(driver, 30)  # Increased wait time

    # Generate dummy data
    first_name = generate_dummy_data("Generate a random first name without additional comments.")
    middle_name = generate_dummy_data("Generate a random middle name in single word only without additional comments.")
    last_name = generate_dummy_data("Generate a random last name without additional comments.")
    street_address = generate_dummy_data("Generate a random street address without additional comments.")
    street_address_line2 = generate_dummy_data("Generate a random street address line 2 without additional comments.")
    city = generate_dummy_data("Generate a random city without additional comments.")
    state = generate_dummy_data("Generate a random state without additional comments.")
    postal_code = generate_dummy_data("Generate a random postal code without additional comments.")
    email = generate_valid_email()
    phone = generate_valid_phone()
    linkedin = generate_dummy_data("Generate a random LinkedIn profile URL without additional comments.")
    ai_agents_info = generate_dummy_data("Write something interesting about AI Agents or LLMs without additional comments.")
    web_automation_info = generate_dummy_data("Write something interesting about Web Automation without additional comments.")
    reversed_linked_list = " -> ".join(reversed(['node1', 'node2', 'node3', 'node4']))

    # Locate form fields and fill them
    driver.find_element(By.NAME, "q11_fullName[first]").send_keys(first_name)
    driver.find_element(By.NAME, "q11_fullName[middle]").send_keys(middle_name)
    driver.find_element(By.NAME, "q11_fullName[last]").send_keys(last_name)
    driver.find_element(By.NAME, "q16_currentAddress[addr_line1]").send_keys(street_address)
    driver.find_element(By.NAME, "q16_currentAddress[addr_line2]").send_keys(street_address_line2)
    driver.find_element(By.NAME, "q16_currentAddress[city]").send_keys(city)
    driver.find_element(By.NAME, "q16_currentAddress[state]").send_keys(state)
    driver.find_element(By.NAME, "q16_currentAddress[postal]").send_keys(postal_code)
    
    driver.find_element(By.NAME, "q12_emailAddress").send_keys(email)
    driver.find_element(By.NAME, "q13_phoneNumber13[full]").send_keys(phone)
    driver.find_element(By.NAME, "q19_linkedin").send_keys(linkedin)
    driver.find_element(By.NAME, "q24_writeSomething").send_keys(ai_agents_info)
    driver.find_element(By.NAME, "q25_writeSomething25").send_keys(web_automation_info)
    driver.find_element(By.NAME, "q23_reverseA").send_keys(reversed_linked_list)

    # Upload resume
    try:
        resume_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
        resume_path = r"C:\\Users\\HP\\Downloads\\MyResume.pdf"
        resume_input.send_keys(resume_path)
    except TimeoutException:
        print("Element not found for resume upload.")
        driver.save_screenshot('debug_screenshot_resume.png')
        driver.quit()
        return

    # Generate and upload cover letter content
    try:
        cover_letter_content = generate_dummy_data("Generate a cover letter content for a data science position for a dummy candidate without additional comments.")
        cover_letter_input = wait.until(EC.presence_of_element_located((By.NAME, "q22_coverLetter")))
        cover_letter_input.send_keys(cover_letter_content)
    except TimeoutException:
        print("Element not found for cover letter upload.")
        driver.save_screenshot('debug_screenshot_cover_letter.png')
        driver.quit()
        return

    time.sleep(5)  # Adjust the sleep time as needed

    # Submit form
    try:
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()
    except TimeoutException:
        print("Submit button not found.")
        driver.save_screenshot('debug_screenshot_submit.png')
        driver.quit()
        return

    time.sleep(2)  # Wait for form submission
    driver.quit()

if __name__ == "__main__":
    fill_form()
