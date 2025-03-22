import subprocess
import getpass
import shlex
import re
from collections import deque
import sys
import os

MAX_REQUEST = 100
PORT = 3000
password = getpass.getpass('Enter password: ')
ip_pattern = re.compile(r'IP (\d+\.\d+\.\d+\.\d+)')

def monitor():

    cmd_str = "sudo -S tcpdump -i any -nn port 3000"
    cmd = shlex.split(cmd_str)

    ip_requests = {}

    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    process.stdin.write(password+"\n")
    process.stdin.flush()

    for line in process.stdout:
        print(line)
        match = ip_pattern.search(line)
        if match:
            ip = match.group(1)

            if ip in ip_requests:
                ip_requests[ip]+=1
            else:
                ip_requests[ip] = 1

            if ip_requests[ip] > MAX_REQUEST:
                print(f"DDoS ALERT! IP {ip} sent more than {MAX_REQUEST} times")
                process.terminate()
                print("Monitor terminated")

                stopper = subprocess.check_output("lsof -i :3000 -t", shell=True, text=True).strip()
                if stopper:
                    print(f"Stopping server running on port {PORT} with PID: {stopper}")
                    os.system(f"kill -9 {stopper}")
                else:
                    print("PID not found")

                sys.exit(0)
        
        else:
            ip_requests.clear()
    


if __name__ == '__main__':
    monitor()