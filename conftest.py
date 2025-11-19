from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options
import json
from pathlib import Path

@pytest.fixture(scope="function")
def driver():

    chrome_options = Options()
    

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
 
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    
    driver.get("https://www.saucedemo.com/")
    
    yield driver 
    
 
    driver.quit()

@pytest.fixture(scope="session")
def test_data():
    data_file_path = Path(__file__).parent / "tests"  / "test_data.json"
    with open(data_file_path, 'r') as f:
        data = json.load(f)
    return data
