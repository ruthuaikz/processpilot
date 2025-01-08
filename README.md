# ProcessPilot

## Overview

ProcessPilot is a Python program designed to manage running processes and resources in Windows, aiming to optimize system performance. It provides functionalities to list, terminate processes, and optimize memory usage by clearing system caches.

## Features

- **List Running Processes**: Display all currently running processes with their Process ID (PID) and names.
- **Terminate Processes**: Safely terminate a specific process using its PID.
- **Optimize Memory**: Free up system memory by clearing clipboard and DNS cache (Windows only).

## Installation

To run this program, ensure you have Python installed on your system, along with the `psutil` library. You can install the `psutil` library using pip:

```bash
pip install psutil
```

## Usage

1. **Listing Processes**: 
   - Run the script and it will display all running processes.
   
2. **Terminating a Process**:
   - Use `terminate_process(pid)` method with the specific PID of the process you want to terminate.
   
3. **Optimizing Memory**:
   - Use `optimize_memory()` method to clear clipboard and DNS cache to free up memory.

Here’s a quick example of how to use the script:

```python
from process_pilot import ProcessPilot

pilot = ProcessPilot()
pilot.list_processes()
pilot.terminate_process(1234)  # Replace 1234 with the actual PID
pilot.optimize_memory()
```

## Platform

This program is specifically designed for Windows operating systems.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.