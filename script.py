import os
import time
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening the browser window)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
webdriver_service = Service('/home/administrator/Downloads/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Set up download folder path to save the PDFs
download_folder = '/home/administrator/Documents/PDFs/'  
os.makedirs(download_folder, exist_ok=True)
chrome_options.add_argument(f"--download.default_directory={download_folder}")

# Open the website
driver.get('https://ceoelection.maharashtra.gov.in/searchlist/')

# Find and select the district from dropdown
district_input = input("Enter the district name: ")

district_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='ctl00_Content_DistrictList']"))
district_dropdown.select_by_visible_text(district_input)

# Find the assembly dropdown and iterate over each option
assembly_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='ctl00_Content_AssemblyList']"))

# Iterate over each assembly option
for assembly_option in assembly_dropdown.options:
    # Select the assembly option, assembly_option_text is the name of the assembly
    assembly_option_text = assembly_option.text
    
    # Select the assembly option from the dropdown
    assembly_dropdown.select_by_visible_text(assembly_option_text)

    # Find the part dropdown and iterate over each option
    part_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='ctl00_Content_PartList']"))

    # Iterate over each part option
    for part_option in part_dropdown.options:

        # Select the part option, part_option_text is the name of the part
        part_option_text = part_option.text

        # Select the part option from the dropdown if the part_option_text is not empty
        part_dropdown.select_by_visible_text(part_option_text)

        # Solve the captcha (We use pytesseract to solve the captcha)
        # find the image element
        captcha_image = driver.find_element(By.XPATH, "//img[@src='Captcha.aspx']")
        # Take a screenshot of the captcha image
        captcha_image.screenshot('captcha.png')  
        # Save the captcha image

        # Use pytesseract to read the text from the captcha image
        pytesseract.pytesseract.tesseract_cmd = '/path/to/tesseract' 
        captcha_text = pytesseract.image_to_string(Image.open('captcha.png')).strip()


        # Enter captcha text and submit
        captcha_input = driver.find_element(By.XPATH, "//input[@id='ctl00_Content_txtcaptcha']")
        captcha_input.send_keys(captcha_text)
        submit_button = driver.find_element(By.XPATH, "//input[@id='ctl00_Content_OpenButton']")
        submit_button.click()

        # After clicking on submit button, a new tab opens with the PDF

        # Wait for the new tab to open and switch to it
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])

         # Wait for the download to complete (modify the wait time as needed)
        time.sleep(5)  # Wait for 5 seconds (adjust as necessary)

        # Close the new tab
        driver.close()

        # Switch back to the original tab, to continue the loop
        driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()
