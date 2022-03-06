import psutil
from flask import Flask, render_template
import time
import urllib

def main():
    start = time.time()
    url='https://www.cisco.com/index.html'
    out_folder=r"C:\Users\Justin Pitt\Desktop\interview notes"
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    f = open(out_folder+"\cisco.html", "w")
    f.write(content)
    f.close()
    end = time.time()
    return(end - start)

app = Flask(__name__)
@app.route('/')
def home():
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/')
    disk_total = disk.total >> 30
    disk_used = disk.used >> 30
    disk_free = disk.free >> 30
    free = psutil.virtual_memory().free >> 20
    time_download = main()
    return render_template("home.html", cpu_usage=cpu, total_disk=disk_total, used_disk=disk_used, free_disk=disk_free, free_memory=free, time_to_download=time_download)

if __name__ == "__main__":
    app.run(debug=True)