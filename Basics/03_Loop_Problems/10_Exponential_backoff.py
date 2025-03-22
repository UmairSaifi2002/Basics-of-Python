# Exponential Backoff
# Description: Impement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

# now we import time module
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempts", attempts+1 ,"- wait time", wait_time,"sec")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1