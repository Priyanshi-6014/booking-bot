# Booking Bot 🏨

A Selenium-based web scraping bot that automates hotel searches on Booking.com.

## Features
- Automatically searches for hotels by destination
- Selects check-in and check-out dates
- Configures number of adults, children, and rooms
- Sorts results by lowest price
- Extracts hotel names, prices, and ratings
- Monitors price changes over time

## Tech Stack
- Python 3
- Selenium 4
- WebDriver Manager
- Chrome WebDriver

## Installation

**1. Clone the repository:**
```bash
git clone https://github.com/Priyanshi-6014/booking-bot.git
cd booking-bot
```

**2. Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

Edit `run.py` with your search parameters:

```python
with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.close_popup()
    bot.select_destination('Montreal')
    bot.select_dates('2026-07-24', '2026-07-25')
    bot.select_guests(adults=2, children=0, rooms=1)
    bot.click_search()
    bot.sort_by_lowest_price()
    bot.report_results()
```

Then run:
```bash
python run.py
```

## Project Structure
```
bot/
  run.py                        # entry point
  requirements.txt              # packages to install
  booking/
    __init__.py
    booking.py                  # main bot class
    booking_filtration.py       # filtering and sorting
    constants.py                # base URL and constants
  extensions/
    __init__.py
    imports.py                  # all shared imports in one place
```

## Shared Imports
All Selenium imports are centralized in `extensions/imports.py`:
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
```

To use them in any file:
```python
from extensions.imports import *
```

## Notes
- Chrome must be installed on your machine
- WebDriver Manager handles ChromeDriver automatically
- Booking.com UI may change over time — selectors may need updating
