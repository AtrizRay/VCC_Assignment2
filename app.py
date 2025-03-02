import time
import psutil 

def continuous_system_monitor():

    print("⚡ Continuous System Monitor Started - Runs Forever!")
    print("Manually terminate using Ctrl+C if running locally, or kill the process if inside VM.")

    while True:
        # Capture system stats
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        # Log the metrics (can be replaced with log to file if needed)
        print(f"[MONITOR LOG] CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")

        # Sleep briefly to simulate reasonable monitoring frequency
        time.sleep(1)

if __name__ == "__main__":
    continuous_system_monitor()
