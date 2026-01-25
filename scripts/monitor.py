#!/usr/bin/env python3
import psutil
import requests
import datetime
import os

# ===========================
# [Server Resource Monitor Script]
# ===========================

# Slack Webhook URL (Replace with your own)
WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

# Thresholds
CPU_THRESHOLD = 80      # %
MEM_THRESHOLD = 85      # %
DISK_THRESHOLD = 90     # %

def send_slack_alert(message):
    payload = {"text": message}
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Failed to send Slack message: {e}")

def main():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if cpu > CPU_THRESHOLD or mem > MEM_THRESHOLD or disk > DISK_THRESHOLD:
        message = (
            f"🚨 *Server Alert ({now})*\n"
            f"CPU: {cpu}%\nMemory: {mem}%\nDisk: {disk}%"
        )
        send_slack_alert(message)
    else:
        print(f"[{now}] Resources OK: CPU={cpu}%, MEM={mem}%, DISK={disk}%")

    if not SLACK_WEBHOOK_URL:
        raise ValueError("SLACK_WEBHOOK_URL environment variable is not set")

if __name__ == "__main__":
    main()