# Setup Guide – Python Automation Lab (Wazuh)

## Overview

This guide explains how to build a SOC automation lab using Python to analyze Wazuh logs in real time.

---

## Requirements

### Systems

* Wazuh Server (Ubuntu-Server)
* Windows 10 Endpoint
* Attacker machine (Ubuntu-Desk)

---

## Step 1 – Verify Wazuh Installation

Ensure Wazuh is running:

sudo systemctl status wazuh-manager

---

## Step 2 – Verify Log Generation

Run:
```Terminal
sudo tail -f /var/ossec/logs/archives/archives.json
```
Trigger failed logins and confirm Event ID 4625 appears.

---

## Step 3 – Install Python

```
python3 --version
```

*If not installed*:

```
sudo apt install python3
```

---

## Step 4 – Create Project

```
mkdir soc-python-lab
cd soc-python-lab
```

---

## Step 5 – Create Script

```
nano log_analyzer.py
```

Paste the script and save.

---


## Step 6 – Run Script

```
sudo python3 log_analyzer.py
```

---

## Step 7 – Simulate Attack

Run brute-force attack using Hydra or manual login attempts.

---

## Step 8 – Observe Detection

The script should display alerts for repeated failed logins.

---

## Troubleshooting

### No logs detected

* Verify Wazuh agent
* Check Windows audit policies

### Permission denied

Run with sudo

---

## Validation Checklist

* [ ] Logs are generated
* [ ] Script runs without errors
* [ ] Alerts are triggered
* [ ] Real-time monitoring works
