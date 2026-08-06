# EC2 Deployment Guide Using Git Clone

This file explains how to deploy your chatbot project on an AWS EC2 instance using Git clone.

---

## 1. Launch an EC2 Instance

In the AWS console:

1. Go to EC2
2. Click Launch Instance
3. Choose Ubuntu 24.04 LTS
4. Select a free-tier-friendly instance type such as t2.micro
5. Create or select a key pair such as mlops-key.pem
6. Add security group rules:
   - SSH: Port 22 from your IP
   - Custom TCP: Port 8501 from 0.0.0.0/0
7. Launch the instance

---

## 2. Connect to the EC2 Instance

From your local PowerShell:

```bash
ssh -i "mlops-key.pem" ubuntu@<your-ec2-public-ip>
```

Example:

```bash
ssh -i "mlops-key.pem" ubuntu@100.53.169.74
```

---

## 3. Update the Server

Run these commands on EC2:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-venv python3-pip git -y
```

---

## 4. Clone the GitHub Repository

On EC2, create a folder and clone your project:

```bash
cd ~
git clone https://github.com/aamir490/use-case-2---Building-a-Chatbot-using-Amazon-Bedrock-Langchain-Streamlit.git
cd use-case-2---Building-a-Chatbot-using-Amazon-Bedrock-Langchain-Streamlit
```

---

## 5. Create a Python Virtual Environment

```bash
sudo apt install python3.14-venv
python3 -m venv .venv
source .venv/bin/activate
```

---

## 6. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If requirements.txt is missing, install manually:

```bash
pip install boto3 langchain langchain-aws langchain-community streamlit PyYAML
```

---

## 7. Configure AWS Credentials on EC2

You have two options:

### Option A: Use IAM Role (Recommended)

Attach an IAM role to the EC2 instance with permissions such as:

- AmazonBedrockFullAccess

This is the safest and easiest option.

### Option B: Use AWS CLI Configure

```bash
sudo apt  install awscli -y
aws configure
```

Enter:

```text
AWS Access Key ID: <YOUR_AWS_ACCESS_KEY_ID>
AWS Secret Access Key: <YOUR_AWS_SECRET_ACCESS_KEY>
Default region name: us-east-1
Default output format: json
```

Verify:

```bash
aws sts get-caller-identity
```

---

## 8. Run the App

Start the Streamlit app:

```bash
nohup streamlit run chatbot_frontend2.py --server.port 8501 --server.address 0.0.0.0 &

ps -ef | grep streamlit
```

Open this in your browser:

```text
http://<your-ec2-public-ip>:8501
```

---

## 9. Keep the App Running in the Background

Use this command:

```bash
nohup streamlit run chatbot_frontend.py --server.port 8501 --server.address 0.0.0.0 > nohup.out 2>&1 &
```

Check it:

```bash
ps aux | grep streamlit
```

---

## 10. Useful Troubleshooting Commands

### Check if port 8501 is listening

```bash
sudo ss -tulnp | grep 8501
```

### View logs

```bash
cat nohup.out
```

### Stop the app

```bash
pkill -f streamlit
```

---

## 11. Important Notes

- Make sure your GitHub repository contains requirements.txt
- Make sure your AWS credentials are configured securely
- Do not hardcode secrets in your code or GitHub files
- Prefer IAM roles over access keys for production

---

## 12. Quick Summary

```bash
ssh -i "mlops-key.pem" ubuntu@<your-ec2-public-ip>
sudo apt update && sudo apt upgrade -y
sudo apt install python3-venv python3-pip git -y
cd ~
git clone https://github.com/aamir490/use-case-2---Building-a-Chatbot-using-Amazon-Bedrock-Langchain-Streamlit.git
cd use-case-2---Building-a-Chatbot-using-Amazon-Bedrock-Langchain-Streamlit
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run chatbot_frontend.py --server.port 8501 --server.address 0.0.0.0
```
