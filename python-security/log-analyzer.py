# Log Analyzer - Security Tool
# Analyst: Mario Galarza
# Description: Python script to analyze authentication logs
# and detect suspicious login patterns

import re
from collections import Counter
from datetime import datetime

# Sample log data (simulating /var/log/auth.log format)
sample_logs = [
    "May 30 09:01:22 server sshd[1234]: Failed password for root from 192.168.1.100 port 22 ssh2",
    "May 30 09:01:25 server sshd[1234]: Failed password for root from 192.168.1.100 port 22 ssh2",
    "May 30 09:01:28 server sshd[1234]: Failed password for admin from 10.0.0.5 port 22 ssh2",
    "May 30 09:01:30 server sshd[1234]: Failed password for root from 192.168.1.100 port 22 ssh2",
    "May 30 09:02:00 server sshd[1234]: Accepted password for mario from 10.0.0.1 port 22 ssh2",
    "May 30 09:03:10 server sshd[1234]: Failed password for root from 203.0.113.5 port 22 ssh2",
    "May 30 09:03:12 server sshd[1234]: Failed password for root from 203.0.113.5 port 22 ssh2",
    "May 30 09:03:14 server sshd[1234]: Failed password for root from 203.0.113.5 port 22 ssh2",
]

def parse_failed_logins(logs):
    """Extract failed login attempts from log entries."""
    failed = []
    pattern = r"Failed password for (\w+) from ([\d.]+)"
    for log in logs:
        match = re.search(pattern, log)
        if match:
            failed.append({
                "user": match.group(1),
                "ip": match.group(2),
                "log": log.strip()
            })
    return failed

def detect_brute_force(failed_logins, threshold=3):
    """Flag IPs with failed attempts above threshold."""
    ip_counts = Counter(entry["ip"] for entry in failed_logins)
    flagged = {ip: count for ip, count in ip_counts.items() if count >= threshold}
    return flagged

def generate_report(failed_logins, flagged_ips):
    """Generate a simple security report."""
    print("=" * 50)
    print("AUTHENTICATION LOG ANALYSIS REPORT")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    print(f"\nTotal failed login attempts: {len(failed_logins)}")
    print(f"Unique IPs with failed attempts: {len(set(e['ip'] for e in failed_logins))}")
    
    if flagged_ips:
        print("\n[!] POTENTIAL BRUTE FORCE DETECTED:")
        for ip, count in flagged_ips.items():
            print(f"    IP: {ip} — {count} failed attempts")
    else:
        print("\n[OK] No brute force patterns detected.")
    
    print("\nTop targeted usernames:")
    user_counts = Counter(e["user"] for e in failed_logins)
    for user, count in user_counts.most_common(3):
        print(f"    {user}: {count} attempts")

# Run analysis
failed = parse_failed_logins(sample_logs)
flagged = detect_brute_force(failed, threshold=3)
generate_report(failed, flagged)
