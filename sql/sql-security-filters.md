# SQL Filters for Security Analysis
**Google Cybersecurity Certificate | Portfolio Activity**
**Analyst:** Mario Galarza

---

## Overview
SQL queries used to investigate security events, filter login attempts, and identify suspicious activity in organizational databases.

---

## Basic Filtering

```sql
-- Retrieve all failed login attempts
SELECT * FROM log_in_attempts
WHERE success = 0;

-- Filter by date
SELECT * FROM log_in_attempts
WHERE login_date = '2022-05-09';

-- Filter activity after business hours
SELECT * FROM log_in_attempts
WHERE login_time > '18:00:00';
```

## AND / OR / NOT Operators

```sql
-- Failed logins after hours (AND)
SELECT * FROM log_in_attempts
WHERE login_time > '18:00:00' AND success = 0;

-- Logins from specific countries (OR)
SELECT * FROM log_in_attempts
WHERE country = 'MEX' OR country = 'USA';

-- Exclude specific department (NOT)
SELECT * FROM employees
WHERE NOT department = 'Information Technology';
```

## LIKE Operator & Wildcards

```sql
-- Find users in offices starting with 'EAST'
SELECT * FROM employees
WHERE office LIKE 'EAST%';

-- Find usernames with pattern
SELECT * FROM employees
WHERE username LIKE 'a%';

-- Find entries with specific pattern in middle
SELECT * FROM log_in_attempts
WHERE country LIKE 'US%';
```

## Security Use Cases

```sql
-- Investigate suspicious logins from specific IP range
SELECT username, login_date, login_time, ip_address
FROM log_in_attempts
WHERE ip_address LIKE '192.168.%'
AND success = 0
ORDER BY login_date DESC;

-- Find employees in specific department for patch update
SELECT first_name, last_name, email, device_id
FROM employees
WHERE department = 'Finance'
AND office LIKE 'SOUTH%';

-- Detect after-hours access attempts
SELECT username, login_date, login_time, country
FROM log_in_attempts
WHERE login_time NOT BETWEEN '07:00:00' AND '18:00:00'
AND success = 0;
```

## Security Relevance
SQL filtering is critical for security analysts to:
- Investigate login anomalies and brute force attempts
- Identify which devices need security patches
- Detect access from unauthorized locations or time windows
- Build queries for SIEM log analysis and incident investigation
