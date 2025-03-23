# This program or tool whatever checks if a site is up or not.Sure the ping command does that but come on, let me cook okay :) 

import requests
import time
try: 
    host_id = input(str("Site: "))
    while True: 
        r = requests.get(host_id, timeout = 10.4)
        if r.status_code == 200:
            time.sleep(2)
            print("\nHost is reachable :)\n")
            break

        elif r.status_code != 200: 
            print("Host is not reachable :()")
            continue
except requests.Timeout:
    print("\nRequest Timeout :( \n")
    
except requests.ConnectionError:
    print("\n Connection Error. Check your internet connection.")