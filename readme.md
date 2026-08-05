# ☁️ Predictive Cloud Resource Optimizer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-lightgrey?style=for-the-badge&logo=flask)
![Prophet](https://img.shields.io/badge/Machine%20Learning-FB%20Prophet-orange?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/Frontend-Vanilla%20JS-yellow?style=for-the-badge&logo=javascript)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **An intelligent FinOps & MLOps orchestrator that predicts cloud server workloads, triggers proactive scaling, and terminates idle instances to optimize operational costs.**

---

## 📸 System Interface: A Visual Walkthrough
*We designed this platform to be as intuitive as a smart home dashboard, making complex AI and Cloud operations easy to understand for everyone, from developers to business stakeholders.*

### 1. Secure Access & Authentication
**What it does:** Ensures that only authorized personnel can access and control the core cloud infrastructure.
<br>
![Authentication Gateway](images/Login%20Page.png)

### 2. The Operational Hub (The Main Dashboard)
**What it does:** This is the control center. Instead of just showing what is happening *now*, it uses AI to predict what will happen in the *future*. The graphs show the AI predicting CPU, RAM, and Network Traffic spikes before they happen, allowing the system to prepare in advance.
<br>
![Operational Hub CPU](images/Operational%20Hub%20CPU.png)
![Operational Hub RAM](images/Operational%20Hub%20RAM.png)
![Operational Hub Traffic](images/Operational%20Hub%20Traffic.png)

### 3. Catching "Zombie" Servers & Saving Money
**What it does:** Sometimes servers are left running but do no actual work (costing the company money). The **Anomaly Screener** automatically acts as a security guard, finding these idle "zombie" servers and flagging them for termination. The **Watchlist** allows admins to keep a close eye on critical servers.
<br>
![Server Watchlist](images/Server%20Watchlist.png)
![Anomaly Screener](images/Anomaly%20Screener.png)

### 4. AI Intelligence & Automated Scheduling
**What it does:** Shows exactly how smart the AI is (currently at ~97.3% accuracy) and displays a clear timeline of when the system plans to automatically add or remove servers based on predictions.
<br>
![Predictive Intel](images/Predictive%20Intel.png)
![Forecast Schedule](images/Forecast%20Schedule.png)

### 5. FinOps: Tracking The Budget
**What it does:** The ultimate business dashboard. It tracks the current monthly cloud bill and calculates exactly how much money the AI is saving the company compared to traditional, manual server management.
<br>
![Cost & Billing](images/Cost%20&%20Billing.png)

### 6. Manual Overrides & PDF Reports
**What it does:** Gives human administrators the final say. If needed, they can press an "Emergency Halt" button. It also features a **Report Engine** to export all savings and server activities into clean, professional PDF reports for management meetings.
<br>
![System Control Panel](images/System%20Control%20Panel.png)
![System Logs](images/System%20Logs.png)
![PDF Export Center](images/PDF%20Export%20Center.png)

---

## 📖 Table of Contents
- [The Problem & Solution](#-the-problem--solution)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Directory Structure](#-directory-structure)
- [Deployment & Setup](#-deployment--setup)
- [Business Impact](#-business-impact)
- [Author](#-author)

---

## ⚡ The Problem & Solution

**The Problem:** Traditional cloud auto-scaling is *reactive*—it adds servers only after a traffic spike occurs, causing lag and latency. Additionally, idle VMs ("zombie servers") continue to run during low-traffic periods, inflating the cloud bill.

**The Solution:** This project introduces a *predictive* approach. By using time-series forecasting (Facebook Prophet) on historical telemetry data, the system anticipates traffic spikes hours in advance. It scales resources proactively and identifies idle nodes for termination, achieving true **FinOps optimization**.

---

## ✨ Key Features

* **🔮 Time-Series Forecasting:** High-accuracy workload prediction using Facebook Prophet to capture seasonality and traffic trends.
* **💸 Automated FinOps Screener:** Continuous monitoring of instance saturation to identify and flag zombie servers for cost-saving termination.
* **🚀 Proactive Scaling:** Replaces reactive lag with proactive provisioning by generating actionable scale-in and scale-out triggers.
* **📊 Live Telemetry Dashboard:** A Single Pane of Glass (SPOG) UI built with asynchronous JS and Chart.js for real-time visualization without UI blocking.
* **🔒 Decoupled REST API:** A secure, lightweight Flask backend using SQLAlchemy to map DB objects and prevent SQL injection.

---

## 🏗️ System Architecture

This project follows a strict **3-Tier Decoupled Architecture**:

1. **Model Layer (MLOps):** Prophet models are trained offline on Google Colab using the [Cloud Computing Performance Metrics Dataset](https://www.kaggle.com/datasets/abdurraziq01/cloud-computing-performance-metrics) from Kaggle, then serialized into binary `.pkl` files for ultra-fast, sub-millisecond inference.
2. **Controller Layer (Backend):** A Flask RESTful microservice acts as the bridge. It loads the `.pkl` files into RAM, queries the SQLite/MySQL database via SQLAlchemy, and serves JSON responses.
3. **Presentation Layer (Frontend):** The dashboard uses `fetch()` API calls asynchronously to render predictive metrics dynamically via Chart.js.

---

## 💻 Tech Stack

* **Data Science & ML:** Python, Pandas, NumPy, Scikit-learn, Facebook Prophet
* **Dataset:** [Cloud Computing Performance Metrics (Kaggle)](https://www.kaggle.com/datasets/abdurraziq01/cloud-computing-performance-metrics)
* **Backend API:** Flask, SQLAlchemy (ORM)
* **Frontend:** HTML5, CSS3, JavaScript (ES6), Chart.js
* **Database:** SQLite / MySQL
* **Tools:** Jupyter Notebook / Google Colab (for initial EDA and model training)

---

## 📂 Directory Structure

```text
📦 predictive-cloud-optimizer
 ┣ 📂 backend/
 ┃ ┣ 📜 app.py                       # Flask REST API server
 ┃ ┣ 📜 model_cpu.pkl                # Trained Prophet model for CPU utilization
 ┃ ┣ 📜 model_traffic.pkl            # Trained Prophet model for network traffic
 ┃ ┣ 📜 report_metrics.pkl           # Evaluated metrics & accuracy reports
 ┃ ┣ 📜 predictive_cloud_opt.ipynb   # Jupyter Notebook for EDA & model training
 ┃ ┗ 📜 users.db                     # SQLite Database storing user credentials
 ┣ 📂 frontend/
 ┃ ┣ 📜 index.html                   # Main telemetry & metrics dashboard UI
 ┃ ┗ 📜 login.html                   # User authentication & login view
 ┣ 📂 dataset/
 ┃ ┗ 📊 vmCloud_data.csv             # Kaggle telemetry dataset (abdurraziq01/cloud-computing-performance-metrics)
 ┣ 📂 images/
 ┃ ┣ 🖼️ Login Page.png               # System screenshots
 ┃ ┣ 🖼️ Operational Hub CPU.png
 ┃ ┗ 🖼️ ... (other UI screenshots)
 ┣ 📜 .gitignore                     # Git ignore rules (skips env/, users.db, etc.)
 ┣ 📜 LICENSE                        # MIT Open Source License
 ┣ 📜 README.md                      # Comprehensive project documentation
 ┣ 📜 final_year_ppt.pptx            # Presentation deck for project review
 ┣ 📜 registered_users.txt           # Test user records
 ┗ ⚙️ run project.bat                # Windows automation script to start application
```

---

## ⚙️ Deployment & Setup

### Prerequisites

* Python 3.8 or higher
* Git installed on the local machine

---

## 📈 Business Impact & Metrics

* **Prediction Accuracy:** Achieved **~97.3%** accuracy in forecasting historical node utilization trajectories.
* **Cost Optimization (FinOps):** Architectural design supports a theoretical **~40% reduction** in recurring cloud expenditures through aggressive zombie-node culling.
* **System Latency:** Reduced API inference response times to **<50 milliseconds** via binary model serialization, completely decoupling the UI from ML processing overhead.

---

## 👤 Author

**VArsha Tiwari**
*Data Analyst | AI & ML Developer*

* **Connect:** [LinkedIn](https://www.linkedin.com/in/varshatiwari04) | [GitHub](https://github.com/Varshat04)
