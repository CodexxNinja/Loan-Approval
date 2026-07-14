
<div align="center">

# Loan Approval Prediction System

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXN4d2s0Y2M0d2NtbTR2MnJwMWl6bHhlbHplNmN5b3I2eXo2OG1oYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/coxQHKASG60HrHtvkt/giphy.gif" width="220"/>

### AI-Powered Loan Approval Prediction using Machine Learning & FastAPI

A modern, end-to-end Machine Learning web application that predicts loan approval decisions with **high accuracy** using an optimized **Random Forest Classifier**. The application combines an elegant multi-step interface with a blazing-fast FastAPI backend to provide instant, probability-backed loan approval decisions.

<p>

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/Random%20Forest-228B22?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/>

</p>

</div>

---

<table>
<tr>

<td width="58%">

# Project Overview

The **Loan Approval Prediction System** is an intelligent machine learning web application designed to automate loan eligibility prediction based on applicant financial and personal information.

Instead of relying solely on manual assessment, the application leverages a trained **Random Forest Classifier** to evaluate multiple credit-risk indicators and instantly predict whether a loan should be **Approved** or **Rejected**, complete with confidence probabilities.

Key Highlights:

- End-to-End ML Workflow
- FastAPI REST Backend
- Interactive Multi-Step Form
- Glassmorphism UI
- Real-Time Prediction
- Probability-Based Decision
- Responsive Design
- Production Ready Architecture

</td>

<td align="center">

<img src="https://media.giphy.com/media/l46Cy1rHbQ92uuLXa/giphy.gif" width="320">

</td>

</tr>
</table>

---

<table>
<tr>

<td align="center">

<img src="https://media.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="280">

</td>

<td width="60%">

# Features

<table>

<tr>

<td align="center" width="33%">

<img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" width="120"><br>

## Intelligent Prediction

Optimized Random Forest model predicts loan approvals with confidence probability.

</td>

<td align="center" width="33%">

<img src="https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif" width="120"><br>

## Multi-Step Application

Smooth and responsive loan application workflow with validation.

</td>

<td align="center" width="33%">

<img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="120"><br>

## Real-Time Processing

Automatic preprocessing, encoding, scaling and instant inference.

</td>

</tr>

<tr>

<td align="center">

<img src="https://media.giphy.com/media/kH1DBkPNyZPOk0BxrM/giphy.gif" width="120"><br>

## FastAPI Backend

High-performance asynchronous REST API with Swagger documentation.

</td>

<td align="center">

<img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="120"><br>

## Beautiful Result Screen

Animated approval and rejection dashboard with contextual recommendations.

</td>

<td align="center">

<img src="https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif" width="120"><br>

## Responsive UI

Works seamlessly across desktops, tablets and mobile devices.

</td>

</tr>

</table>

</td>

</tr>

</table>

---

<table>

<tr>

<td width="58%">

# Architecture

```mermaid
flowchart LR

A[User Browser]

B[Multi-Step HTML Interface]

C[JavaScript Validation]

D[FastAPI Backend]

E[Preprocessing Pipeline]

F[Random Forest Model]

G[Prediction]

H[Result Dashboard]

A --> B

B --> C

C --> D

D --> E

E --> F

F --> G

G --> H
````

The architecture separates presentation, preprocessing, machine learning inference and result rendering, making the application scalable and maintainable.

</td>

<td align="center">

<img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="320">

</td>

</tr>

</table>

---

<table>

<tr>

<td align="center">

<img src="https://media.giphy.com/media/juua9i2c2fA0AIp2iq/giphy.gif" width="320">

</td>

<td>

# Tech Stack

<div align="center">

### Languages & Frameworks

<img src="https://skillicons.dev/icons?i=python,fastapi,html,css,js"/>

### Machine Learning

<img src="https://skillicons.dev/icons?i=sklearn"/>

### Tools

<img src="https://skillicons.dev/icons?i=git,github,vscode"/>

</div>

| Component           | Technology               |
| ------------------- | ------------------------ |
| Backend             | FastAPI                  |
| Machine Learning    | Random Forest Classifier |
| Data Processing     | Pandas, NumPy            |
| Model Serialization | Joblib                   |
| Templates           | Jinja2                   |
| Frontend            | HTML5, CSS3, JavaScript  |

</td>

</tr>

</table>

---

---

<div align="center">

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2x4cnI5b2Q4dXd2aTR6MWh5aHZlYmx2bTR3YWg4bTFzcDR2aDVhYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LmNwrBhejkK9EFP504/giphy.gif" width="180"/>

# Dataset

The machine learning model is trained on carefully selected financial and credit-risk attributes to accurately determine an applicant's loan eligibility.

</div>

<br>

| Feature | Data Type | Description |
|:--------|:---------:|:------------|
| **Age** | Numerical | Applicant's age |
| **Income** | Numerical | Annual income |
| **Home Ownership** | Categorical | Housing status (Own, Rent, Mortgage) |
| **Employment Length** | Numerical | Years of employment |
| **Loan Intent** | Categorical | Purpose of the loan |
| **Loan Amount** | Numerical | Requested loan amount |
| **Interest Rate** | Numerical | Loan interest rate |
| **Loan Grade** | Categorical | Risk grade (A–G) |
| **Credit History Length** | Numerical | Years of credit history |
| **Historical Default** | Categorical | Previous loan default (Yes/No) |

<br>

<div align="center">

### Data Preprocessing Pipeline

```text
Raw Dataset
      │
      ▼
Missing Value Handling
      │
      ▼
Categorical Encoding
      │
      ▼
Feature Scaling
      │
      ▼
Feature Selection
      │
      ▼
Random Forest Classifier
```

</div>

<div align="center">

> **High-quality preprocessing ensures accurate, consistent, and reliable loan approval predictions.**

</div>

---

---

<div align="center">

<img src="https://media.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif" width="180"/>

# Installation

Follow the steps below to set up the **Loan Approval Prediction System** on your local machine.

</div>

<br>

### 1. Clone the Repository

```bash
git clone https://github.com/CodexxNinja/Loan-Approval.git

cd Loan-Approval
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Train the Machine Learning Model

```bash
python train_model.py
```

### 6. Start the FastAPI Server

```bash
uvicorn app:app --reload
```

<div align="center">

### Installation Flow

```text
Clone Repository
        │
        ▼
Create Virtual Environment
        │
        ▼
Activate Environment
        │
        ▼
Install Dependencies
        │
        ▼
Train ML Model
        │
        ▼
Run FastAPI Server
        │
        ▼
Open in Browser 🚀
```

</div>

---


<div align="center">

<img src="https://media.giphy.com/media/f3iwJFOVOwuy7K6FFw/giphy.gif" width="180"/>

# Usage

Run the application locally and access the following resources.

<br>

| Resource | URL |
|:---------|:----|
| **Web Interface** | `http://127.0.0.1:8000` |
| **Swagger UI** | `http://127.0.0.1:8000/docs` |
| **ReDoc** | `http://127.0.0.1:8000/redoc` |

</div>

<br>

<div align="center">

### Application Workflow

```text
Start Application
        │
        ▼
Open Web Interface
        │
        ▼
Fill Loan Application
        │
        ▼
Submit Details
        │
        ▼
Data Preprocessing
        │
        ▼
Random Forest Prediction
        │
        ▼
Generate Probability Score
        │
        ▼
Display Approval / Rejection Result
```

</div>

---
---

<div align="center">

<img src="https://media.giphy.com/media/juua9i2c2fA0AIp2iq/giphy.gif" width="180"/>

# API Endpoints

Interact with the **FastAPI** backend through the following endpoints.

<br>

| Method | Endpoint | Description |
|:------:|:--------:|-------------|
| **GET** | `/` | Serves the Loan Application interface |
| **POST** | `/predict` | Predicts loan approval using the trained ML model |
| **GET** | `/docs` | Interactive Swagger API Documentation |
| **GET** | `/redoc` | Alternative ReDoc API Documentation |

<br>

### API Workflow

```text
Client
   │
   ▼
POST /predict
   │
   ▼
FastAPI Backend
   │
   ▼
Preprocessing Pipeline
   │
   ▼
Random Forest Model
   │
   ▼
Prediction + Probability
   │
   ▼
JSON Response
```

</div>


---

<div align="center">

<img src="https://media.giphy.com/media/juua9i2c2fA0AIp2iq/giphy.gif" width="180"/>

# Project Structure

Explore the organized folder hierarchy of the Loan Approval Prediction System.

</div>

<br>

```text
Loan-Approval/
│
├── dataset/
│   └── loan_data.csv
│
├── models/
│   └── random_forest_model.joblib
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── result.css
│   │
│   └── js/
│       ├── form.js
│       └── validation.js
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```
<div align="center">

<img src="https://media.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="180"/>

# Authors

Meet the developers behind the **Loan Approval Prediction System**.

<br>

<table>
<tr>

<td align="center" width="50%">

### Varad Paradkar

AIML Engineer

<a href="https://github.com/CodexxNinja">
<img src="https://img.shields.io/badge/GitHub-CodexxNinja-181717?style=for-the-badge&logo=github"/>
</a>

</td>

<td align="center" width="50%">

### Durgesh Padwal

AIML Developer

<a href="https://github.com/Durgesh729">
<img src="https://img.shields.io/badge/GitHub-Durgesh729-181717?style=for-the-badge&logo=github"/>
</a>

</td>

</tr>
</table>

</div>

---
