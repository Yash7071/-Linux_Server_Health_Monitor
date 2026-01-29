import psutil
import time
import boto3

CPU_THRESHOLD = 50
RAM_THRESHOLD = 80
CHECK_INTERVAL = 60

AWS_REGION = "us-east-1"
TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:Server-Health-Alerts"

AWS_ACCESS_KEY = "PASTE_YOUR_ACCESS_KEY_HERE"
AWS_SECRET_KEY = "PASTE_YOUR_SECRET_KEY_HERE"

sns_client = boto3.client(
    'sns',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def send_alert(subject, message):
    """Sends an alert via AWS SNS."""
    try:
        response = sns_client.publish(
            TopicArn=TOPIC_ARN,
            Message=message,
            Subject=subject
        )
        print(f"✅ Alert sent to AWS! Message ID: {response['MessageId']}")
    except Exception as e:
        print(f"❌ Failed to send to AWS: {e}")

def monitor_system():
    print(f"🔍 Monitoring started (Targeting AWS SNS)...")
    
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        print(f"CPU: {cpu_usage}% | RAM: {ram_usage}%")

        if cpu_usage > CPU_THRESHOLD:
            send_alert("CPU CRITICAL ALERT", f"Warning! CPU usage is at {cpu_usage}%")
        
        if ram_usage > RAM_THRESHOLD:
            send_alert("RAM CRITICAL ALERT", f"Warning! RAM usage is at {ram_usage}%")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_system()
