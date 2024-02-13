from datetime import datetime, timedelta

current_date = datetime.now()
future_date = current_date + timedelta(days=7)
print(current_date)
print(future_date)

# 37 Working with Dates
# from datetime import datetime, timedelta

now = datetime.now()

# Format date
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)

# Add days to a date
future_date = now + timedelta(days=7)
print(future_date)
