#this file will include anclass with instance method 
#That will be responsible to inetarct with our website
#after we have some results, to apply filteration 

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By  # ADD THIS
from selenium.webdriver.support import expected_conditions as EC


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def sort_by_lowest_price(self):
        self.find_element(By.CSS_SELECTOR, 
            'button[data-testid="sorters-dropdown-trigger"]'
        ).click()
        
        # wait for dropdown to open
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-id="price"]'))
        )
        
        # re-find the element right before clicking to avoid stale reference
        self.find_element(By.CSS_SELECTOR, 'button[data-id="price"]').click()
        

    