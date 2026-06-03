
from extensions.imports import *

class Booking(webdriver.Chrome):

    def __init__(self, teardown=False, driver_path=r"/usr/local/bin/chromedriver"):  # location of driver
        options = Options()
        options.add_experimental_option("detach", True)

        self.teardown = teardown
        service = Service(ChromeDriverManager().install())

        super(Booking, self).__init__(service=service, options=options)
        self.implicitly_wait(10)

        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    # def change_currency(self, currency):
    #     currency_element = self.find_element(By.CSS_SELECTOR,
    #         'button[data-tooltip-text="Choose your currency"]')
    #     currency_element.click()

    #     selected_currency_element = self.find_element(By.CSS_SELECTOR,
    #         f'a[data-modal-header-async-url-param*="selected_currency={currency}"]') #*= means contain substring
    #     selected_currency_element.click()

    def close_popup(self):

        try:
            WebDriverWait(self, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'))
            ).click()
        except:
            pass  # no popup, just continue

    def select_destination(self, destination):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear()
        search_field.send_keys(destination)

        # wait until dropdown actually shows YOUR destination
        WebDriverWait(self, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'autocomplete-result-0'), destination[:4]
            )
        )

        first_result = self.find_element(By.ID, 'autocomplete-result-0')
        first_result.click()

    def select_dates(self, check_in, check_out):
        check_in_elemtn = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in}"]')
        check_in_elemtn.click()

        check_out_elemtn = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out}"]')
        check_out_elemtn.click()

    # def select_adults(self,count=1):
    #      adult_input = self.find_element(By.ID,'group_adults')
    #      adult_input.clear()
    #      adult_input.send_keys(count)

    # def select_children(self,count=0):
    #      child_input = self.find_element(By.ID,'group_children')
    #      child_input.clear()
    #      child_input.send_keys(count)

    # def select_rooms(self,count=1):
    #      room_input = self.find_element(By.ID,'no_rooms')
    #      room_input.clear()
    #      room_input.send_keys(count)

    def select_guests(self, adults=6, children=0, rooms=2):
        self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]').click()

        WebDriverWait(self, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-testid="occupancy-popup"]'))
        )

        popup_buttons = self.find_elements(By.CSS_SELECTOR,
                                           'div[data-testid="occupancy-popup"] button'
                                           )

        # indexes: [0]- adults, [1]+ adults, [2]- children, [3]+ children, [4]- rooms, [5]+ rooms
        for _ in range(adults - 2):    # starts at 2
            popup_buttons[1].click()

        for _ in range(children):
            popup_buttons[3].click()

        for _ in range(rooms - 1):     # starts at 1
            popup_buttons[5].click()

        # Done button is index 7 — use it directly
        popup_buttons[7].click()

    def click_search(self):
        self.find_element(
            By.XPATH, '//button[.//span[text()="Search"]]').click()


    
        
    def booking_filt(self):
        filtration = BookingFiltration(driver=self)
        filtration.sort_by_lowest_price()













    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()
