from datetime import datetime as dt

today = dt.today().date()
format_date = today.strftime("%y%m%d")
print(format_date)