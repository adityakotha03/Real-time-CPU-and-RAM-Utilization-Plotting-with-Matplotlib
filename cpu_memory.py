import matplotlib.pyplot as plt
import psutil
import time
import argparse
import os
import signal


def save_plot(cpu, ram, filename):
    fig = plt.figure(figsize=(8, 4))
    plt.plot(cpu, ls="--", lw=3, marker="X", markersize=8, markerfacecolor="red", markeredgecolor="black", label="CPU Utilization")
    plt.plot(ram, ls=":", marker="o", markersize=8, markerfacecolor="None", label="RAM Utilization")
    plt.ylim(0, 100)
    plt.xlabel("Time (s)")
    plt.ylabel("CPU and RAM usage (%)")
    plt.legend()
    plt.tight_layout()

    if not filename.endswith(".png"):
        filename += ".png"
    
    plt.savefig(filename)
    print(f"Utilization plot saved as {filename}")


def monitor_utilization(duration, filename="utilization_plot.png"):
    frame_len = 200  # number of data points to show in plot
    cpu = []
    ram = []
    start_time = time.time()

    def signal_handler(sig, frame):
        print("\nPlotting stopped by user. Saving utilization plot...")
        save_plot(cpu, ram, filename)
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        cpu.append(psutil.cpu_percent())
        ram.append(psutil.virtual_memory()[2])
        
        time_elapsed = time.time() - start_time
        time_left = max(duration - time_elapsed, 0)
        print(f"Time Left: {time_left:.2f}s", end="\r")
        
        if time_elapsed >= duration:
            break
        
        time.sleep(1)  # wait for 1 second before taking next measurement

    save_plot(cpu, ram, filename)


parser = argparse.ArgumentParser(description='Monitor CPU and memory usage for a specified duration.')
parser.add_argument('--duration', type=int, default=10, help='Duration in seconds to monitor CPU and memory usage. Default: 10')
parser.add_argument('--filename', type=str, default='utilization_plot.png', help='Name of the file to save the utilization plot. Default: utilization_plot.png')
args = parser.parse_args()

monitor_utilization(args.duration, args.filename)
