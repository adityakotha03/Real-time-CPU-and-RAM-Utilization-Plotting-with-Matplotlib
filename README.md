# Real-time-CPU-and-RAM-Utilization-Python
This repository contains a Python file that uses the matplotlib library to plot the real-time CPU and RAM utilization of a system.

## Dependencies
- [x] Matplotlib
- [x] psutil

## Usage
1. Clone the repository or download the script "cpu_memory.py".
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script with the following command:
  ```
  python cpu_memory.py --duration <duration> --filename <filename>
  ```
  where <duration> is the duration in seconds to monitor CPU and memory usage (default is 10 seconds) and <filename> is the name of the file to save the utilization plot (default is utilization_plot.png).

**Example usage:**
  
  ```
  python cpu_memory.py --duration 30 --filename myplot.png
  ```
  
This will monitor CPU and memory usage for **"30 seconds"** and save the utilization plot as **"myplot.png"**. The script displays the time left for monitoring in seconds and updates every second.

To stop the monitoring and generate the utilization plot before the specified duration, press ***"CTRL+C"***. The script will generate the utilization plot with the data collected up to that point and save it with the specified filename. The script uses a signal function to handle CTRL+C interrupts and ensure that the utilization plot is saved before exiting.

## Acknowledgments
- [Matplotlib](https://matplotlib.org/)
- [psutil](https://psutil.readthedocs.io/en/latest/)
