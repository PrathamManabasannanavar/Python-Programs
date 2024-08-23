import subprocess;
import psutil;
import time;

def openBrowser(path):
    return subprocess.Popen(path).pid;

def removeBrowser(pid):
    try:
        process = psutil.Process(pid)
        process.terminate(); #terminate the process
    except:
        print("Browser already closed!!")

# chromepid = openBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe");
bravepid = openBrowser(["C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe", "youtube.com"]);
print(bravepid)
bravepid2 = openBrowser(["C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe", "youtube.com"]);
print(bravepid2)
time.sleep(5); #sleep for 10s
removeBrowser(bravepid);
# removeBrowser(chromepid);