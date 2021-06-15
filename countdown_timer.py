import time

def countdown(t):

    while t: #while t > 0 for clarity
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r") #overwrite previous line
        time.sleep(1)
        t -= 1

    print('GAS')

t = input("Enter the time in seconds: ")

countdown(int(t))