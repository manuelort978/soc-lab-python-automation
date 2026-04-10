# Findings – Python Automation Lab

## Summary
The Python script successfully detected brute-force attack patterns in real time by analyzing Wazuh logs.

## Observations
- Multiple failed login attempts detected (Event ID: 4625)
- Repeated activity from a single IP identified
- Real-time monitoring worked as expected

## Analysis
The behavior matches a brute-force attack pattern, where repeated authentication failures occur from the same source.

## Conclusion
The lab demonstrates the effectiveness of Python-based automation in SOC environments.

## Recommendations
- Implement detection for successful login (Event ID: 4624)
- Automate response actions
