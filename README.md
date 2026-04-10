# SOC Automation Lab – Python and Wazuh

## Overview

This project demonstrates real-time security monitoring and threat detection using Python and Wazuh SIEM.

The lab focuses on automating the detection of brute-force attacks by analyzing Windows authentication logs.

---

## Objectives

* Automate log analysis using Python
* Detect brute-force attacks in real time
* Parse JSON logs from Wazuh
* Develop SOC automation skills

---

## Features

* Real-time log monitoring (tail-like behavior)
* Detection of failed login attempts (Event ID 4625)
* Identification of suspicious IP addresses
* Threshold-based alerting

---

## Technologies Used

* Python 3
* Wazuh SIEM
* Windows Event Logs

---

## How It Works

1. The script monitors Wazuh logs in real time
2. Extracts relevant fields using safe parsing (.get())
3.  Counts failed login attempts per IP
4. Triggers an alert when threshold is reached

---

## Detection Logic

* Event ID 4625 -> Failed login
* Threshold -> 5 attempts per IP

---

## Project Structure

* `/scripts` -> Python automation script
* `/reports` -> Analysis results
* `/queries` -> Threat hunting queries

---

## Example Output

[INFO] Failed login from 192.168.56.103 (count=1)\
  [ALERT]: Possible brute force attack from 192.168.56.103

---

## Future Improvements

* Detect successful login after brute force (Event ID: 4624)
* Block malicious IPs automatically

---

## Skills Demonstrated

* Python scripting for cybersecurity
* SIEM log analysis
* Real-time monitoring
* Threat detection automation
