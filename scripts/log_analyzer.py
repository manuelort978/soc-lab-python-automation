import json
import time
from collections import defaultdict

LOG_FILE = "/var/ossec/logs/alerts/alerts.json"
THRESHOLD = 5

failed_attempts = defaultdict(int)

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

def analyze():
    with open(LOG_FILE, "r") as f:
        loglines = follow(f)

        print("Monitoring logs in real-time...\n")

        for line in loglines:
            try:
                log = json.loads(line)

                event_id = log.get("data", {}).get("win", {}).get("system", {}).get("eventID")
                ip = log.get("data", {}).get("win", {}).get("eventdata", {}).get("ipAddress")

                if event_id == "4625" and ip:
                    failed_attempts[ip] += 1

                    print(f"[INFO] Failed login from {ip} (count={failed_attempts[ip]})")

                    if failed_attempts[ip] == THRESHOLD:
                        print(f"\n [ALERT]: Possible brute force attack from {ip}\n")

            except json.JSONDecodeError:
                continue
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    analyze()
