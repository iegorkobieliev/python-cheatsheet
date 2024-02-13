# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("Execution completed.")


try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
else:
    print("No errors occurred.")
finally:
    print("This block always executes.")