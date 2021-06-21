import time
from datetime import datetime as dt

hosts_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "https://www.facebook.com"]

while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now()\
                < dt(dt.now().year, dt.now().month, dt.now().day, 17):
            print("Working hours")
            with open(hosts_path,"r+") as file:
                content = file.read()
                for website in websites:
                    if website in content:
                        pass
                    else:
                        # mapping hostnames to your localhost IP address
                        file.write(redirect + " " + website + "\n")

        else:
            with open(hosts_path,"r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                # removing hostnames from host file
                file.truncate()

            print("Fun hours")
        time.sleep(5)