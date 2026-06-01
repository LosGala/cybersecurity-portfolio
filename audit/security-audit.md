# Security Audit - Botium Toys
**Google Cybersecurity Certificate | Portfolio Activity**
**Analyst:** Mario Galarza
**Date:** May 2026

---

## Scope and Goals

**Scope:** Entire security program at Botium Toys — all assets, internal processes, and procedures related to controls and compliance best practices.

**Goals:** Assess existing assets and complete the controls and compliance checklist to determine which controls and compliance best practices need to be implemented to improve Botium Toys' security posture.

**Risk Score:** 8/10 (High)

---

## Controls Assessment Checklist

| Control | In Place? | Notes |
|---|---|---|
| Least Privilege | ❌ No | All employees have access to internally stored data including cardholder data and PII/SPII |
| Disaster Recovery Plans | ❌ No | No disaster recovery plans currently in place |
| Password Policies | ❌ No | Password policy exists but requirements are nominal — not in line with current minimum complexity standards |
| Separation of Duties | ❌ No | Not implemented — increases risk of fraud and unauthorized access |
| Firewall | ✅ Yes | Firewall blocks traffic based on defined security rules |
| Intrusion Detection System (IDS) | ❌ No | IDS has not been installed |
| Backups | ❌ No | No backups of critical data exist |
| Antivirus Software | ✅ Yes | Installed and monitored regularly |
| Manual Monitoring for Legacy Systems | ✅ Yes | IT department monitors end-of-life systems |
| Encryption | ❌ No | Credit card information is not encrypted in the internal database |
| Password Management System | ❌ No | No centralized password management system in place |
| Locks (offices, storefront, warehouse) | ✅ Yes | Physical locks in place |
| CCTV Surveillance | ✅ Yes | Surveillance cameras in use |
| Fire Detection/Prevention | ✅ Yes | Fire alarm and sprinkler system in place |

---

## Compliance Checklist

### Payment Card Industry Data Security Standard (PCI DSS)

| Best Practice | Compliant? |
|---|---|
| Only authorized users have access to customers' credit card information | ❌ No |
| Credit card information is stored, accepted, processed, and transmitted in a secure environment | ❌ No |
| Encryption procedures implemented for credit card transaction touchpoints | ❌ No |
| Secure password management policies adopted | ❌ No |

### General Data Protection Regulation (GDPR)

| Best Practice | Compliant? |
|---|---|
| EU customers' data is kept private/secured | ❌ No |
| Plan to notify EU customers within 72 hours if data is compromised | ✅ Yes |
| Data is properly classified and inventoried | ❌ No |
| Privacy policies, procedures, and processes enforced | ✅ Yes |

### System and Organizations Controls (SOC type 1, SOC type 2)

| Best Practice | Compliant? |
|---|---|
| User access policies are established | ❌ No |
| Sensitive data (PII/SPII) is confidential/private | ❌ No |
| Data integrity ensures data is consistent, complete, accurate, and validated | ✅ Yes |
| Data is available to individuals authorized to access it | ✅ Yes |

---

## Recommendations

Based on the risk assessment, the following controls should be prioritized immediately:

**Critical (Implement First):**
1. **Least Privilege & Separation of Duties** — Restrict employee access to only the data required for their role. This directly reduces the risk of internal fraud and unauthorized access to cardholder data and PII/SPII.
2. **Encryption** — Implement encryption for all credit card data stored, processed, and transmitted. This is a PCI DSS requirement and a critical gap.
3. **Intrusion Detection System (IDS)** — Deploy an IDS to detect and alert on suspicious network activity in real time.

**High Priority:**
4. **Disaster Recovery Plans & Backups** — Establish data backup procedures and a formal disaster recovery plan to ensure business continuity in case of a security incident.
5. **Password Management System** — Implement a centralized password manager that enforces minimum complexity requirements (8+ characters, letters, numbers, special characters).

**Medium Priority:**
6. **PCI DSS Full Compliance** — Address all four PCI DSS gaps, particularly around access control and encryption, to avoid regulatory fines.
7. **GDPR Data Classification** — Classify and inventory all data, especially EU customer data, to ensure proper handling and compliance.

---

## Key Takeaways

- Botium Toys has significant gaps in both administrative controls (least privilege, password policy) and technical controls (encryption, IDS, backups).
- Physical security controls are adequate (CCTV, locks, fire detection).
- The highest immediate risks are: unencrypted credit card data, unrestricted employee access to sensitive data, and lack of disaster recovery capability.
- Non-compliance with PCI DSS and GDPR exposes the company to financial penalties and reputational damage.

