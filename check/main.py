import time

second = time.time()
print(second)

def countdown(t):

    while t:
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -=1
    print("done and dusted")

t = input("enter time to count")

countdown(int(t))