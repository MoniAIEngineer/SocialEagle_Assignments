Delivery Agent API – README.md
Overview

This project is a Flask-based Delivery Agent API integrated with:

Swiggy 🍔
Zepto 🛒
Dunzo 🟣

The APIs are connected with an n8n AI Agent workflow and Telegram bot to simulate:

Food ordering
Grocery ordering
Parcel pickup & drop
Order confirmation
Order tracking
Features
Swiggy 🍔
Restaurant food ordering
Multi-item support
Order confirmation
Order tracking
Delivery status updates
Zepto 🛒
Grocery ordering
Multiple grocery items in one order
Fast delivery ETA simulation
Order tracking
Dunzo 🟣
Pickup & drop delivery
Grocery/pharmacy support
Parcel delivery simulation
Tracking updates
Tech Stack
Python Flask
Gunicorn
Ubuntu VPS (Hostinger)
n8n AI Agent
Telegram Bot
REST APIs
Project Structure
delivery-agent-flask-api/
│
├── app.py
├── requirements.txt
├── .env
├── venv/
API Endpoints
Health Check
GET /health

Response:

{
  "status": "healthy",
  "message": "API is working"
}
Swiggy APIs
Search Order
POST /swiggy/search
Request
{
  "item": "2 chicken biryani",
  "quantity": 2,
  "address": "Anna Nagar Chennai",
  "recipient": "Monic"
}
Response
{
  "status": "confirmation_required",
  "pending_id": "xxxx",
  "message": "Shall I place this order?"
}
Confirm Order
POST /swiggy/confirm/<pending_id>
Track Order
GET /swiggy/track/<order_id>
Zepto APIs
Search Order
POST /zepto/search
Request
{
  "item": "3 milk packets and 2 bread packets",
  "quantity": 1,
  "address": "Koramangala Bangalore",
  "recipient": "Rahul"
}
Confirm Order
POST /zepto/confirm/<pending_id>
Track Order
GET /zepto/track/<order_id>
Dunzo APIs
Search Order
POST /dunzo/search
Request
{
  "item": "documents",
  "quantity": 1,
  "address": "Velachery Chennai",
  "recipient": "Karthik"
}
Confirm Order
POST /dunzo/confirm/<pending_id>
Track Order
GET /dunzo/track/<order_id>
VPS Deployment (Hostinger)
Step 1 – SSH into VPS
ssh root@YOUR_SERVER_IP
Step 2 – Install Dependencies
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y
Step 3 – Upload Project

From local machine:

scp -r delivery-agent-flask-api root@YOUR_SERVER_IP:/root/
Step 4 – Setup Virtual Environment
cd /root/delivery-agent-flask-api

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
Step 5 – Install Gunicorn
pip install gunicorn
Create Linux Service
Create Service File
sudo nano /etc/systemd/system/delivery-api.service

Paste:

[Unit]
Description=Delivery Agent Flask API
After=network.target

[Service]
User=root
WorkingDirectory=/root/delivery-agent-flask-api
Environment="PATH=/root/delivery-agent-flask-api/venv/bin"
ExecStart=/root/delivery-agent-flask-api/venv/bin/gunicorn -w 2 -b 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
Enable Service
sudo systemctl daemon-reload

sudo systemctl enable delivery-api

sudo systemctl start delivery-api
Check Service Status
sudo systemctl status delivery-api

Expected:

Active: active (running)
Restart Service After Code Changes
sudo systemctl restart delivery-api
View Live Logs
sudo journalctl -u delivery-api -f
Common Issues & Fixes
Issue 1 – Connection Refused
Error
The service refused the connection
Cause

Flask app was not running publicly.

Fix
Hosted API on VPS
Used public IP instead of localhost
Used Gunicorn service
Issue 2 – API Stops After Closing VS Code
Cause

Used:

python app.py

which runs temporarily.

Fix

Configured Gunicorn + systemd service.

Issue 3 – Wrong Tracking Status
Fix

Updated tracking steps:

Swiggy
Restaurant is preparing your food
Zepto
Items packed
Dunzo
Pickup partner assigned
Issue 4 – Zepto Multiple Items Not Working
Cause

Only first item was being confirmed.

Fix

Implemented multi-item parsing and storage.

Issue 5 – Same Price for Every Item
Cause

Static pricing logic.

Fix

Implemented keyword-based dynamic pricing system.

Testing Scenarios
Positive Scenarios
Swiggy
Order 2 chicken biryani to Anna Nagar Chennai recipient Monic
Zepto
Order 3 milk packets and 2 bread packets to Koramangala Bangalore recipient Rahul
Dunzo
Pickup documents from T Nagar and deliver to Velachery recipient Karthik
Negative Scenarios
Invalid Quantity
Order -1 pizza

Expected:

Quantity must be greater than 0
Blocked Item
Order alcohol

Expected:

Sorry, I cannot place an order for alcohol.
Missing Address
Order pizza

Expected:

Please share the delivery address.
Important Commands
Restart API
sudo systemctl restart delivery-api
Check Status
sudo systemctl status delivery-api
Stop Service
sudo systemctl stop delivery-api
Start Service
sudo systemctl start delivery-api
Final Notes
APIs are simulated
No real Swiggy/Zepto/Dunzo integration
Built for AI Agent workflow demonstration
Telegram bot integrated through n8n
Fully deployable on VPS
