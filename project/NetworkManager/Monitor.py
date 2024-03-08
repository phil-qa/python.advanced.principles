import psutil
def monitor_system():
    while True:
        # Processor Usage
        cpu_percent = psutil.cpu_percent(interval=1)

        # RAM Usage
        ram = psutil.virtual_memory()
        ram_percent = ram.percent

        # Network Utilization
        network_io = psutil.net_io_counters()
        bytes_sent = network_io.bytes_sent
        bytes_recv = network_io.bytes_recv

        print(f"CPU Usage: {cpu_percent}%")
        print(f"RAM Usage: {ram_percent}%")
        print(f"Bytes Sent: {bytes_sent}")
        print(f"Bytes Received: {bytes_recv}")
        print("-" * 40)

        time.sleep(5)  # Sleep for 5 seconds before polling again


if __name__ == "__main__":
    monitor_system()