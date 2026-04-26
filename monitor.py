import psutil
import time

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80

def check_system():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    print(f"CPU: {cpu}% | Memory: {memory}%")

    if cpu > CPU_THRESHOLD:
        print("High CPU Usage detected!")

    if memory > MEM_THRESHOLD:
        print("High Memory usage detected!")

if __name__ == "__main__":
    while True:
        check_system()
        time.sleep(5)