# Linux Commands for Security Analysts
**Google Cybersecurity Certificate | Portfolio Activity**
**Analyst:** Mario Galarza

---

## File System Navigation
```bash
pwd           # Print working directory
ls            # List files
ls -la        # List all files with permissions and hidden files
cd /path      # Change directory
cd ..         # Go up one level
find / -name "filename"  # Search for files
```

## File Permissions
```bash
ls -la        # View permissions (rwxrwxrwx format)
chmod 644 file.txt     # Owner: read/write | Group: read | Others: read
chmod 755 script.sh    # Owner: all | Group: read/execute | Others: read/execute
chmod u+x file         # Add execute permission for owner
chown user:group file  # Change file owner and group
```

## Permission Structure
## User & Group Management
```bash
whoami           # Current user
id               # User ID and group memberships
sudo command     # Run as superuser
su - username    # Switch user
adduser username # Add new user
usermod -aG group user  # Add user to group
```

## Process Management
```bash
ps aux           # List all running processes
top              # Real-time process monitor
kill PID         # Terminate process by ID
grep "term" file # Search for pattern in file
```

## Network Commands
```bash
ifconfig         # Network interface info
ping host        # Test connectivity
netstat -an      # Active connections
ss -tulnp        # Listening ports and services
```

## Log Analysis (Security Relevant)
```bash
cat /var/log/auth.log     # Authentication logs
tail -f /var/log/syslog   # Real-time system log
grep "Failed" /var/log/auth.log  # Filter failed login attempts
journalctl -u ssh         # SSH service logs
```

## Security Relevance
These commands are essential for Blue Team operations:
- File permissions → prevent unauthorized access to sensitive files
- Log analysis → detect suspicious activity and failed login attempts
- Process management → identify malicious processes
- Network commands → detect unauthorized connections
