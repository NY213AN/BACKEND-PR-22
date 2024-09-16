import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 120)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up!")

# Example usage: Countdown from 10 seconds
countdown(60)
