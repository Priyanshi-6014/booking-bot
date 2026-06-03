from booking.booking import *

with Booking() as bot:
    bot.land_first_page()
    bot.close_popup()
    # bot.change_currency(currency="USD")
    bot.select_destination('Montreal')
    bot.select_dates('2026-07-24', '2026-07-25')
    bot.select_guests()
    bot.click_search()
    filtration = BookingFiltration(driver=bot)  # pass bot as driver
    filtration.sort_by_lowest_price()
