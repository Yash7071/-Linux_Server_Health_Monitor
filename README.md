# ☁️ Linux Server Health Monitor (AWS Integrated)

## 📌 Project Overview
An automated **DevOps automation tool** designed to monitor the health of Linux servers in real-time. It tracks **CPU and RAM utilization** and uses **AWS SNS (Simple Notification Service)** to trigger immediate cloud-based alerts when critical thresholds (e.g., 80%) are exceeded.

This project demonstrates proficiency in **Python scripting**, **Linux system administration**, and **Cloud Infrastructure (AWS)** integration.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Cloud Services:** AWS SNS (Simple Notification Service), IAM
* **Libraries:** `boto3` (AWS SDK), `psutil` (System Monitoring)
* **Automation:** Linux `systemd` (Background Service Management)
* **OS:** Ubuntu Linux / WSL

## 🚀 Key Features
* ✅ **Real-Time Monitoring:** Continuously scans system resources every 60 seconds.
* ✅ **Cloud Alerting:** Integrated with AWS SNS to send emails/SMS directly from the cloud.
* ✅ **Resource Efficient:** Lightweight script designed to run in the background without consuming memory.
* ✅ **Secure Design:** Uses placeholder architecture for credentials to prevent sensitive data leakage.

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/Yash7071/-Linux_Server_Health_Monitor.git](https://github.com/Yash7071/-Linux_Server_Health_Monitor.git)
cd -Linux_Server_Health_Monitor
```

### 2. Install Dependencies
```bash
sudo apt install python3-pip
pip3 install boto3 psutil
```

### 3. Configuration
Open the `monitor.py` file and configure your AWS credentials and thresholds:

```python
# Configuration
CPU_THRESHOLD = 80
AWS_REGION = "us-east-1"
TOPIC_ARN = "arn:aws:sns:us-east-1:123456789:Your-Topic"
```

*(Note: For security, use Environment Variables or IAM Roles in a production environment.)*

### 4. Run the Monitor
```bash
python3 monitor.py
```

## 🧠 What I Learned
* How to interact with **AWS APIs** programmatically using **Boto3**.
* Managing Linux processes and creating background services with **Systemd**.
* Implementing **Error Handling** in Python to ensure service reliability.

---
*Created by [Yash](https://github.com/Yash7071)*
