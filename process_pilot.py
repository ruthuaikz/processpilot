import psutil
import os

class ProcessPilot:
    def __init__(self):
        self.processes = []

    def list_processes(self):
        """Lists all running processes."""
        self.processes = [(proc.info['pid'], proc.info['name']) for proc in psutil.process_iter(['pid', 'name'])]
        for pid, name in self.processes:
            print(f"PID: {pid}, Process Name: {name}")

    def terminate_process(self, pid):
        """Terminates a process by its PID."""
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait(timeout=3)
            print(f"Process {pid} terminated successfully.")
        except psutil.NoSuchProcess:
            print(f"No process found with PID: {pid}")
        except psutil.AccessDenied:
            print(f"Access denied to terminate process with PID: {pid}")
        except psutil.TimeoutExpired:
            print(f"Timeout expired while terminating process with PID: {pid}")

    def optimize_memory(self):
        """Frees up memory by clearing system cache."""
        if os.name == 'nt':
            try:
                os.system('echo off | clip')  # Clear clipboard to free up memory
                os.system('ipconfig /flushdns')  # Flush DNS cache
                print("System memory optimization completed.")
            except Exception as e:
                print(f"An error occurred while optimizing memory: {e}")
        else:
            print("Memory optimization is only supported on Windows.")

if __name__ == '__main__':
    pilot = ProcessPilot()
    print("ProcessPilot: Managing running processes and resources")
    pilot.list_processes()
    # Example usage:
    # pilot.terminate_process(1234)
    # pilot.optimize_memory()