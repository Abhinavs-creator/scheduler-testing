import schedule
import time
import datetime

# Function to write "hi" in a new file every time
def write_to_new_file():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # Unique timestamp
    file_name = f"output_{timestamp}.txt"  # Unique file name
    with open(file_name, "w") as f:  # "w" mode creates a new file
        f.write("Schedule triggered\n")
    print(f"Created file: {file_name}")

# Schedule the function to run every 5 seconds
schedule.every(5).seconds.do(write_to_new_file)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
