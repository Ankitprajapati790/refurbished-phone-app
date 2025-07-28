# 📱 Refurbished Phone Selling App

A simple Flask-based web application that helps manage inventory and profitability of refurbished phones listed on multiple platforms (X, Y, Z). It allows inventory tracking, price calculation based on platform-specific fees, and ensures only profitable listings are shown.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How to Run](#how-to-run)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 🧩 Overview

This app is designed to assist in selling refurbished smartphones across multiple online platforms. Each platform has its own fees and profit margins, and this app calculates the best options for listing based on profitability and stock availability.

---

## ✅ Features

- 📦 Inventory Management
- 💰 Platform-specific fee deduction logic
- 📉 Profitability check per platform
- 🧮 Dynamic pricing logic
- 🔒 Basic admin login system
- 🖥️ Simple dashboard interface

---

## 💻 Tech Stack

| Layer         | Technology       |
|--------------|------------------|
| Language      | Python 3.8+      |
| Backend       | Flask            |
| Frontend      | HTML, CSS        |
| Styling       | Basic CSS        |
| Data Storage  | Python Dictionary (in-memory) |
| IDE           | VS Code          |

---

## 🗂️ Project Structure

phone_app/
│
├── app.py # Main Flask app
├── phones_data.py # Inventory and pricing data
├── utils.py # Helper functions: profitability check, platform logic
├── templates/ # HTML files (login and dashboard)
│ ├── login.html
│ └── dashboard.html
├── static/ # CSS styling
│ └── style.css
├── README.md # Project documentation



---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Ankitprajapati790/refurbished-phone-app.git
cd refurbished-phone-app
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux

Install Dependencies
pip install flask

▶️ How to Run
Open terminal in project folder

Run:

bash
Copy
Edit
python app.py
Open your browser and visit:
http://127.0.0.1:5000

Login with:

Username: admin

Password: admin


 screenshots
<img width="1920" height="1080" alt="Screenshot 2025-07-28 231806" src="https://github.com/user-attachments/assets/85b16d59-fd5e-439b-898b-2436c20f4d81" />
<img width="1920" height="1080" alt="Screenshot 2025-07-28 231830" src="https://github.com/user-attachments/assets/acd670b7-0cd0-4990-9721-a920130d2576" />

🛠️ Future Improvements
🔐 Add real authentication with hashed passwords

🧾 Connect to a real database (e.g., SQLite, PostgreSQL)

📊 Add graphs for inventory and sales

📱 Make frontend responsive

🛒 Add integration for placing orders directly

👨‍💻 Author
Ankit Prajapati
📧 ankitprajapatiofficial876@gmail.com









