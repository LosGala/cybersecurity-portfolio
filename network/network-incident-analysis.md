# Cybersecurity Incident Report - Network Analysis
**Google Cybersecurity Certificate | Portfolio Activity**
**Analyst:** Mario Galarza
**Date:** May 2026
**Framework:** NIST Cybersecurity Framework (CSF)

---

## Summary

The organization experienced a Denial of Service (DoS) attack that disrupted internal network services for approximately two hours. The attack involved a flood of ICMP ping packets sent through an unconfigured firewall, overwhelming the network and preventing normal internal traffic from accessing any network resources. The incident was resolved by blocking ICMP packets, taking non-critical services offline, and restoring critical services.

---

## NIST CSF Analysis

### 1. IDENTIFY
**Type of attack:** DoS (Denial of Service) — ICMP Flood Attack

**Systems affected:**
- Internal network infrastructure
- All network-facing services (temporarily unavailable)
- Firewall (misconfiguration exploited)

**Root cause:** The firewall was not properly configured to limit or filter incoming ICMP packets. This allowed a malicious actor to flood the network with ICMP ping requests, consuming all available bandwidth and processing resources.

**Attack vector:** External — malicious actor sent a flood of ICMP pings through an unconfigured firewall to the company's network.

**Impact:** Complete disruption of internal network services for 2 hours. All employees lost access to network resources during the attack window.

---

### 2. PROTECT
**Immediate actions taken:**
- New firewall rule implemented to limit the rate of incoming ICMP packets
- IP source address verification added to the firewall to detect spoofed IP addresses in ICMP packets
- IDS/IPS deployed to filter suspicious ICMP traffic based on anomalous characteristics

**Recommended improvements:**
- Conduct regular firewall configuration audits to identify and close misconfigurations before they are exploited
- Implement network segmentation to limit the blast radius of future attacks
- Establish and enforce security policies for firewall rule management — all changes must be reviewed and approved
- Train IT staff on DoS attack vectors and firewall hardening best practices
- Document and maintain an updated asset inventory to understand which systems are most exposed

---

### 3. DETECT
**Monitoring improvements implemented:**
- Network monitoring software deployed to detect anomalous traffic patterns in real time
- IDS/IPS configured to flag unusual ICMP traffic volumes and characteristics

**Additional detection recommendations:**
- Set up automated alerts for sudden spikes in ICMP or any single protocol traffic
- Implement baseline traffic profiling — establish normal traffic patterns so anomalies are detected faster
- Enable logging on all firewall rules to maintain an audit trail of traffic events
- Monitor for spoofed IP addresses and unusual geographic traffic sources
- Schedule regular review of network logs and IDS/IPS alerts

---

### 4. RESPOND
**Incident response actions taken:**
- Blocked all incoming ICMP packets via firewall rule update
- Took non-critical network services offline to reduce load and contain impact
- Restored critical services incrementally once attack traffic was controlled
- Investigated the incident to identify root cause (unconfigured firewall)

**Future response plan:**
- Activate incident response team immediately upon detection of abnormal traffic spike
- Isolate affected network segments to contain the attack and protect critical systems
- Apply rate-limiting firewall rules as an immediate containment measure
- Notify stakeholders of service disruption with estimated resolution time
- Collect and preserve network logs, IDS alerts, and traffic captures for forensic analysis
- After containment, conduct a post-incident review to document lessons learned
- Report the incident to relevant authorities if attack is sustained or causes significant data loss

---

### 5. RECOVER
**Recovery actions taken:**
- Critical network services restored within 2 hours of attack onset
- Non-critical services brought back online after attack traffic was fully blocked

**Recovery improvement plan:**
- Develop and document a formal Disaster Recovery Plan (DRP) for network attacks
- Establish Recovery Time Objectives (RTO) for all critical services — define maximum acceptable downtime
- Implement redundant network infrastructure to reduce single points of failure
- Create data backup procedures to ensure data availability is not impacted during future attacks
- After full recovery, communicate incident summary and resolution steps to all stakeholders
- Conduct a tabletop exercise simulating a similar DoS attack to validate the response and recovery plan

---

## Key Lessons Learned

1. Firewall misconfigurations are a critical vulnerability — regular audits are essential
2. Without an IDS/IPS, the attack went undetected until services were already disrupted
3. No disaster recovery plan meant recovery was slower and less structured than it should be
4. Rate limiting and IP source verification are basic but effective controls against ICMP floods

