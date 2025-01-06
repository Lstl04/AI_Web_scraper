from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_website_content_and_clean(website):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(r"C:\Users\louis\Documents\Projects\AI Scrapper\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(website)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    content = soup.body
    print("Website content retrieved")
    for element in content(["script", "style"]):
        element.extract()

    cleaned_content = content.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    print(cleaned_content)
    driver.quit()
    return cleaned_content
    
