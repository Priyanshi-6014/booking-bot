#this file will include anclass with instance method 
#That will be responsible to inetarct with our website
#after we have some results, to apply filteration 

from extensions.imports import *

class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def sort_by_lowest_price(self):
        self.driver.find_element(By.CSS_SELECTOR, 
            'button[data-testid="sorters-dropdown-trigger"]'
        ).click()
        
        # wait for dropdown to open
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-id="price"]'))
        )
        
        # re-find to avoid stale reference
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]').click()