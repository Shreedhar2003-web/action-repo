# GitHub Webhook Receiver Project

This project is a simple GitHub webhook receiver built using **Flask**, **MongoDB**, and **HTML/JavaScript frontend**.

It receives GitHub webhook events (like `push`, `pull request`) and displays them in a UI that updates every 15 seconds.

---

## 🔧 Tech Stack
- Python 3
- Flask
- MongoDB
- HTML, CSS, JavaScript

---

## 🚀 Features

- Receives webhook events from a GitHub repo (like push or pull request)
- Stores the event messages in MongoDB
- Frontend fetches the latest messages every 15 seconds and displays them
- Simple and clean UI

---

## 🧪 Local Testing (without GitHub Webhooks)

If you don’t use GitHub webhook + ngrok, you can test locally using `test.py`:

```bash
python test.py
