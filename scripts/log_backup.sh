#!/bin/bash

# ======================================
# Spring Boot Log Backup Script
# ======================================

# Log directory (Spring Boot log path)
LOG_DIR="/home/ubuntu/linux-automation-networking-project/logs"

# Backup destination directory
BACKUP_DIR="/home/ubuntu/backup"

# Today's date (DDMMYYYY format)
DATE=$(date +%d%m%Y)

# Create backup directory if it does not exist
mkdir -p $BACKUP_DIR

# Compress and back up log files
tar -czf $BACKUP_DIR/backup-$DATE.tar.gz $LOG_DIR

# Remove backup files older than 7 days
find $BACKUP_DIR -type f -mtime +7 -delete

# Print completion message (append to backup log)
echo "[$(date '+%d-%m-%Y %H:%M:%S')] Backup completed for $DATE" >> /var/log/log_backup.log