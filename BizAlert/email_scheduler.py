import time
from apscheduler.schedulers.background import BackgroundScheduler
from NewBusinessAlert.BizAlert.routes import send_daily_newsletter
from datetime import datetime

# Create a scheduler
scheduler = BackgroundScheduler()

# Define the job to be executed
def job():
    print("Running job...")
    send_daily_newsletter()

# Schedule the job to run every morning at 9 am
scheduler.add_job(job, 'cron', hour=9, minute=10)

# Start the scheduler
scheduler.start()

try:
    # Keep the script running
    print("Scheduler is running. Press Ctrl+C to exit.")
    while True:
        # This is here to simulate application activity (which keeps the main thread alive).
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    # Shut down the scheduler gracefully when exiting the script
    print("Shutting down the scheduler.")
    scheduler.shutdown()
