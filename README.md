Here is a **version matching the style and energy of your Pokémon project README**, but tailored to your **AWS EC2 REST API project**. This style works well on GitHub and for recruiters.

---

# ☁️ AWS EC2 REST API Service

A lightweight **Python cloud API deployed on AWS EC2** and managed with Linux service infrastructure.

This project demonstrates how to deploy a **continuously running backend service in the cloud**, featuring REST endpoints, health monitoring, and automated service management using **Gunicorn and systemd**.

---

# 🧠 Overview

This project simulates a **production-style backend service deployment** on AWS.

A Python Flask API runs on an **Amazon Linux EC2 instance**, exposing public endpoints while being managed by a **Gunicorn WSGI server** and **systemd service** to ensure uptime, resilience, and automatic startup.

The system demonstrates real-world cloud infrastructure concepts including **service reliability, request handling, monitoring endpoints, and Linux process management**.

---

# ⚙️ Features

☁️ **Cloud Deployment** — REST API hosted on AWS EC2 with public endpoint access

⚡ **Production-Style Execution** — Gunicorn WSGI server handles concurrent requests

🧠 **Health Monitoring Endpoint** — `/health` endpoint reports service status and uptime

📦 **Data API** — `/records` endpoint supports message storage and retrieval

🔄 **Automated Service Management** — systemd ensures automatic startup and recovery

🛡️ **Secure Cloud Configuration** — EC2 security groups restrict access to required ports

📊 **Structured Request Handling** — input validation and predictable API responses

---

# 🧱 Project Structure

```
hpe-cloud-mini-api
│
├── app
│   └── main.py
│
├── data.json
├── requirements.txt
│
├── systemd
│   └── hpe-mini-api.service
│
└── README.md
```

---

# 🧩 Technical Highlights

**Language:** Python

**Framework:** Flask

**Cloud Platform:** AWS EC2 (Amazon Linux)

**Core Infrastructure**

• Gunicorn — WSGI production server
• systemd — Linux service manager
• EC2 Security Groups — network access control

**Key Components**

**Flask API**
Handles routing, request parsing, and response generation.

**Gunicorn Server**
Runs the application with multiple workers for reliability.

**systemd Service**
Ensures the API automatically starts and restarts if failures occur.

---

# 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jfraile05/hpe-cloud-mini-api.git
cd hpe-cloud-mini-api
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Locally

```bash
python app/main.py
```

The API will start on:

```
http://127.0.0.1:5050
```

---

# ☁️ Deploying on AWS EC2

Launch an **Amazon Linux EC2 instance** and SSH into it.

```
ssh -i key.pem ec2-user@<EC2-IP>
```

Install Python dependencies:

```
sudo dnf install python3-pip
pip3 install -r requirements.txt
```

Run using Gunicorn:

```
gunicorn -w 2 -b 0.0.0.0:5050 app.main:app
```

---

# 🔄 Running as a Linux Service

Create a systemd service file:

```
/etc/systemd/system/hpe-mini-api.service
```

Enable and start the service:

```
sudo systemctl daemon-reload
sudo systemctl start hpe-mini-api
sudo systemctl enable hpe-mini-api
```

Check service status:

```
sudo systemctl status hpe-mini-api
```

This ensures the API **automatically starts on boot and restarts if it fails**.

---

# 📡 Example API Requests

### Health Check

```
curl http://<EC2-IP>:5050/health
```

Response

```
{
  "status": "ok",
  "uptime_seconds": 39
}
```

---

### Create Record

```
curl -X POST http://<EC2-IP>:5050/records \
-H "Content-Type: application/json" \
-d '{"message":"hello"}'
```

---

### Retrieve Records

```
curl http://<EC2-IP>:5050/records
```

---

# 🧠 What This Project Demonstrates

☁️ Cloud service deployment on AWS EC2
⚙️ Linux service automation with systemd
📡 REST API development using Flask
⚡ Production-style API execution using Gunicorn
🛠 Infrastructure configuration and monitoring endpoints

---

# 🧩 Future Improvements

📊 Add persistent storage using PostgreSQL or DynamoDB

📈 Add logging and monitoring (CloudWatch integration)

🛡 Implement authentication and API security

🚀 Containerize the service with Docker

---

# 👨‍💻 Author

**Jorge Fraile**
Florida State University — Computer Science

GitHub
[https://github.com/Jfraile05](https://github.com/Jfraile05)

---

If you want, I can also help you add **two things that make GitHub projects look 10× more professional to recruiters**:

1. **Architecture diagram (AWS-style)**
2. **Badges (Python, AWS, Flask, Linux, Gunicorn)**

Those two additions make your repo look **much closer to a real cloud engineering project**.
