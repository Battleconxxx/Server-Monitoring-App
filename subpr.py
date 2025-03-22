import subprocess as sp

with open("network_log.txt", "w") as logfile:
    process = sp.Popen(["netstat", "-c"], stdout=logfile, text=True)

    try:
        process.wait()
    except:
        print("Stopping monitoring")
        process.terminate()