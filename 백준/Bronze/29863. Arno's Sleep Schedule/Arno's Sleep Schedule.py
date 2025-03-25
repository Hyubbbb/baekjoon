sleep_time = int(input())
wake_time = int(input())

if sleep_time >= 20:
    sleep_time -= 24

print(wake_time - sleep_time)