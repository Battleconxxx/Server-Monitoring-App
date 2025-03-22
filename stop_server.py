import os
import subprocess

# Define the port your server is running on
PORT = 3000  # Change this to your server's port

# Find the process running on the specified port
try:
    result = subprocess.check_output(f"lsof -i :{PORT} -t", shell=True, text=True).strip()
    if result:
        print(f"Stopping server running on port {PORT} with PID: {result}")
        os.system(f"kill -9 {result}")
    else:
        print(f"No process found running on port {PORT}")
except subprocess.CalledProcessError:
    print(f"No process is running on port {PORT}")
