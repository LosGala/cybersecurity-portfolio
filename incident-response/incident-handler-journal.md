# Incident Handler Journal
**Google Cybersecurity Certificate | Portfolio Activity**
**Analyst:** Mario Galarza

---

## Entry #1

**Date:** May 30, 2026

**Description:** Documentation of a ransomware attack targeting a small US healthcare clinic, resulting in encrypted files and full operational disruption.

**Tools Used:** None (initial documentation entry)

---

## The 5 W's

**WHO caused the incident?**
An organized group of unethical hackers known for targeting organizations in the healthcare and transportation sectors. The group used spear phishing emails as the initial attack vector to gain access to the clinic's internal network.

**WHAT happened?**
Employees reported being unable to access files including medical records. A ransom note appeared on their computers stating all company files had been encrypted. The attackers demanded a large sum of money in exchange for the decryption key. The clinic was forced to shut down its computer systems and contact external organizations for technical assistance.

**WHEN did the incident occur?**
Tuesday morning at approximately 9:00 a.m. The incident caused immediate and sustained disruption to business operations throughout the day.

**WHERE did the incident occur?**
At a small US-based healthcare clinic specializing in primary care services. The attack affected internal computer systems across the organization, compromising access to patient records and critical business software.

**WHY did the incident occur?**
The attackers successfully delivered spear phishing emails containing malicious attachments to multiple employees. Once an employee downloaded the attachment, malware was installed on their computer. The attackers then used this access to deploy ransomware that encrypted critical files across the network. The incident likely succeeded due to a lack of employee security awareness training and insufficient email filtering controls.

---

## Additional Notes

- Key question: Did the clinic have data backups in place? If so, recovery could proceed without paying the ransom.
- The healthcare sector is a high-value target due to the sensitivity of patient data and the critical nature of operations — any disruption creates immediate pressure to pay.
- This incident highlights the importance of both technical controls (email filtering, EDR, backups) and human controls (phishing awareness training) working together.
- Follow-up: Were the phishing emails reported by any employee before the malware executed? Early detection could have contained the blast radius significantly.


---

## Entry #2

**Date:** May 30, 2026

**Description:** SIEM investigation using Wazuh to identify failed SSH login attempts for root account on a mail server.

**Tools Used:** Wazuh (SIEM platform)

---

## The 5 W's

**WHO:** Unknown external threat actors attempting brute force SSH access.

**WHAT:** Over 300 failed SSH login attempts targeting the root account on Buttercup Games' mail server (mailsv).

**WHEN:** Events identified across historical log data indexed in Wazuh.

**WHERE:** Buttercup Games mail server (mailsv) — /mailsv/secure.log

**WHY:** Root account targeted via brute force — likely automated attack seeking privileged access to the mail server.

---

## Additional Notes
- Query used: `host.keyword: mailsv AND (fail* OR failed) AND root`
- High volume of failed attempts suggests automated brute force, not manual attack
- Recommendation: disable root SSH login, implement fail2ban, enforce key-based authentication only

---

## Entry #3

**Date:** May 30, 2026

**Description:** Investigation of a suspicious file hash using VirusTotal to determine whether a file downloaded by an employee contained malware. This entry covers the Detection and Analysis phase of the NIST Incident Response Lifecycle.

**Tools Used:** VirusTotal (threat intelligence platform for file hash analysis)

- Obtained the SHA-256 hash of the suspicious file
- Searched the hash on VirusTotal to check detections across multiple antivirus engines
- Reviewed vendor reports, file behavior, and associated IP addresses/domains
- VirusTotal returned positive detections from multiple vendors — file confirmed as malicious
- Findings documented and escalated to incident response team for containment

---

## Entry #4

**Date:** May 30, 2026

**Description:** Used Splunk SIEM to perform queries and investigate suspicious login activity across organizational systems. This entry covers the Detection and Analysis phase of the NIST Incident Response Lifecycle.

**Tools Used:** Splunk (SIEM platform for log aggregation and security event analysis)

- Ingested sample log data into Splunk for analysis
- Used SPL (Search Processing Language) to filter events by host, time range, and event type
- Identified patterns of failed login attempts across multiple accounts
- Correlated events across different log sources to build a timeline of suspicious activity
- Splunk dashboards used to visualize attack patterns and frequency

## The 5 W's

**WHO:** Unknown external threat actor attempting unauthorized access via credential stuffing.

**WHAT:** Multiple failed login attempts detected across several user accounts within a short time window, suggesting an automated credential stuffing attack.

**WHEN:** Events detected during log review session — timestamps spread across a 2-hour window.

**WHERE:** Organizational authentication systems — events captured in Splunk from web application and VPN logs.

**WHY:** Attacker likely used a list of previously breached credentials to attempt unauthorized access. Lack of MFA made accounts vulnerable to this type of attack.

---

## Reflections/Notes

**Were there any specific activities that were challenging for you? Why or why not?**
The most challenging activity was the network incident analysis using the NIST CSF framework. Mapping a real attack scenario across all five framework functions — Identify, Protect, Detect, Respond, and Recover — required thinking about security holistically rather than just reacting to the immediate threat. It pushed me to consider long-term security posture improvements, not just immediate fixes.

**Has your understanding of incident detection and response changed since taking this course?**
Yes, significantly. Before this course I understood security from a data perspective — detecting anomalies in datasets. Now I understand the full lifecycle of an incident: how attacks unfold, how to document them systematically, and how frameworks like NIST CSF provide structure to what could otherwise be a chaotic response. Detection is only one piece of a much larger process.

**Was there a specific tool or concept that you enjoyed the most? Why?**
SIEM tools — particularly Splunk and Wazuh — were the most interesting to me because they directly connect my existing data analytics skills to security operations. Writing SPL queries feels very similar to writing SQL for anomaly detection, which is something I have real hands-on experience with. SIEM is where my background gives me a genuine advantage over candidates coming purely from a security background.

