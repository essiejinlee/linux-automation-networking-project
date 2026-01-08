# Linux-automation-networking-project

## Project Overview
This project focuses on deploying and operating a web service on a Linux server, with an emphasis on automation and operational stability.  
It was designed to gain hands-on experience with real-world server management tasks commonly required in junior DevOps and backend engineering roles.

The project covers application deployment, reverse proxy configuration, automated maintenance tasks, and basic server monitoring with alerting.

---

## Tech Stack
- **OS:** Ubuntu 22.04 (AWS EC2)
- **Web Server:** Nginx
- **Application:** Java Spring Boot
- **Automation:** Bash, Python
- **Monitoring & Alerts:** Python (`psutil`, `requests`), Slack Incoming Webhooks
- **Service Management:** systemd, cron

---

## System Architecture
- An AWS EC2 instance running Ubuntu hosts the application
- Nginx is configured as a reverse proxy to forward external HTTP traffic to the application
- The Spring Boot application runs as a `systemd` service to ensure availability after reboot or failure
- Repetitive operational tasks are automated using cron jobs

[User Browser]
→ HTTP/HTTPS (80/443)
→ [Nginx Reverse Proxy]
→ [Spring Boot Application :8080]

---

## Application Deployment
- Built and packaged a Spring Boot application using Gradle
- Deployed the application to an AWS EC2 instance
- Configured the application as a `systemd` service:
  - Automatically starts on server boot
  - Automatically restarts if the process stops
- Verified successful deployment via the EC2 public IP address and domain access

---

## Nginx Reverse Proxy & HTTPS
- Installed and configured Nginx as a reverse proxy
- Forwarded incoming requests from port **80** to the Spring Boot application on port **8080**
- Secured the service using **HTTPS** with Let’s Encrypt and Certbot
- Validated external access and SSL configuration through browser testing

---

## Automation Scripts

### 1. Log Backup Automation (Bash)
- Created a Bash script to automate log maintenance:
  - Compresses application and Nginx logs into date-based archive files
  - Stores backups in a dedicated backup directory
  - Automatically deletes old backups after a defined retention period
- Registered the script as a cron job to run daily without manual intervention

**Location:** `scripts/log_backup.sh`

---

### 2. Server Monitoring & Slack Alerts (Python)
- Implemented a Python-based monitoring script using `psutil`
- Periodically checks:
  - CPU usage
  - Memory usage
  - Disk usage
- Sends automatic alert messages to a Slack channel via Incoming Webhooks when usage exceeds predefined thresholds
- Tested both normal and alert-triggering scenarios to verify reliability

**Location:** `scripts/monitor.py`

---

## Troubleshooting & Operational Experience
- Diagnosed and resolved Linux file permission issues affecting script execution
- Fixed Nginx configuration and port-binding problems
- Investigated cron job execution issues and verified scheduled task reliability
- Debugged Slack webhook integrations by isolating configuration, logic, and runtime causes

---

## Project Structure
".
├── README.md
├── scripts
│ ├── log_backup.sh
│ └── monitor.py
├── configs
│ └── nginx.conf
└── docs
└── project-summary.pdf"

---

## What I Learned
- How production-like Linux servers are deployed and operated
- The role of reverse proxies in web service architectures
- Practical automation techniques to reduce manual operational work
- The importance of monitoring and alerting for system reliability

---

## Future Improvements
- DNS and DHCP configuration in a virtualized network environment
- Network traffic analysis using Wireshark
- Database integration (e.g. PostgreSQL or MySQL)
- CI/CD pipeline automation for application deployment
