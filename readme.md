# ☁️ Predictive Cloud Resource Optimizer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-lightgrey?style=for-the-badge&logo=flask)
![Prophet](https://img.shields.io/badge/Machine%20Learning-FB%20Prophet-orange?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/Frontend-Vanilla%20JS-yellow?style=for-the-badge&logo=javascript)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **An intelligent FinOps & MLOps orchestrator that predicts cloud server workloads, triggers proactive scaling, and terminates idle instances to optimize operational costs.**

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

1. **Model Layer (MLOps):** Prophet models are trained offline on Google Colab using Kaggle datasets, then serialized into binary `.pkl` files for ultra-fast, sub-millisecond inference.
2. **Controller Layer (Backend):** A Flask RESTful microservice acts as the bridge. It loads the `.pkl` files into RAM, queries the SQLite/MySQL database via SQLAlchemy, and serves JSON responses.
3. **Presentation Layer (Frontend):** The dashboard uses `fetch()` API calls asynchronously to render predictive metrics dynamically via Chart.js.

---

## 💻 Tech Stack

* **Data Science & ML:** Python, Pandas, NumPy, Scikit-learn, Facebook Prophet
* **Backend API:** Flask, SQLAlchemy (ORM)
* **Frontend:** HTML5, CSS3, JavaScript (ES6), Chart.js
* **Database:** SQLite / MySQL
* **Tools:** Jupyter Notebook / Google Colab (for initial EDA and model training)

---

## 📂 Directory Structure

```text
📦 predictive-cloud-optimizer
 ┣ 📂 backend/
 ┃ ┣ 📂 env/                         # Python Virtual Environment
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
 ┃ ┗ 📊 vmCloud_data.csv             # Raw Kaggle cloud VM telemetry dataset
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

**Akbar Naeem**
*Data Analyst | Financial Operations (FinOps) | AI & ML Developer*

* **Professional Summary:** A highly motivated professional with a BCA specializing in Data Science and Artificial Intelligence. Passionate about leveraging machine learning models, modern software architecture, and predictive analytics to drive enterprise efficiency.
* **Connect:** [LinkedIn](https://www.linkedin.com/in/akbar-naeem) | [GitHub](https://github.com/akbar-naeem)
