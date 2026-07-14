<div align="center">

# Loan Approval Prediction System

### AI-Powered Loan Approval Prediction using Machine Learning & FastAPI

A modern end-to-end Machine Learning web application that predicts loan approval decisions using an optimized **Random Forest Classifier**, delivering fast, accurate, and probability-backed predictions through a responsive multi-step interface.

<br>

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/Random%20Forest-228B22?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/>

<br><br>

> **FastAPI • Machine Learning • Random Forest • Responsive UI • Production Ready**

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

<div align="center">

<img src="https://media.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="180"/>

# Features

Explore the key capabilities of the **Loan Approval Prediction System**, designed for accurate predictions, seamless user experience, and high-performance machine learning inference.

</div>

<br>

<table>

<tr>

<td width="50%" valign="top">

### Intelligent Prediction

Predicts loan approval using an optimized **Random Forest Classifier**, delivering accurate results with confidence probabilities.

</td>

<td width="50%" valign="top">

### Multi-Step Application

Guides users through a clean, responsive, and intuitive multi-step loan application process.

</td>

</tr>

<tr>

<td width="50%" valign="top">

### Automated Data Processing

Handles missing values, categorical encoding, feature scaling, and preprocessing before inference.

</td>

<td width="50%" valign="top">

### High-Performance FastAPI Backend

Provides fast, asynchronous prediction APIs with interactive Swagger documentation.

</td>

</tr>

<tr>

<td width="50%" valign="top">

### Dynamic Result Dashboard

Displays approval or rejection results along with prediction confidence in a modern interface.

</td>

<td width="50%" valign="top">

### Responsive User Experience

Optimized for desktops, tablets, and mobile devices with a clean and consistent interface.

</td>

</tr>

</table>

<br>

<div align="center">

### Feature Workflow

```text
User Input
     │
     ▼
Data Validation
     │
     ▼
Preprocessing Pipeline
     │
     ▼
Random Forest Prediction
     │
     ▼
Confidence Score
     │
     ▼
Result Dashboard
```

</div>


------

<div align="center">

<img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="180"/>

# Architecture

The Loan Approval Prediction System follows a modular architecture that separates the presentation layer, backend services, preprocessing pipeline, and machine learning model to ensure scalability, maintainability, and efficient inference.

</div>

<br>

```mermaid
flowchart TD

    A[User]

    B[Multi-Step Web Interface<br/>HTML • CSS • JavaScript]

    C[FastAPI Backend]

    D[Data Preprocessing<br/>Encoding • Scaling • Validation]

    E[Random Forest Classifier]

    F[Prediction Probability]

    G[Loan Decision]

    H[Result Dashboard]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
```

<div align="center">

### System Workflow

```text
User
 │
 ▼
Multi-Step Application Form
 │
 ▼
FastAPI Backend
 │
 ▼
Data Preprocessing
 │
 ▼
Random Forest Classifier
 │
 ▼
Probability Prediction
 │
 ▼
Approval / Rejection
 │
 ▼
Result Dashboard
```

</div>

<div align="center">

> **The architecture cleanly separates the user interface, API layer, preprocessing pipeline, and machine learning model, resulting in a scalable, maintainable, and production-ready application.**

</div>

---

<div align="center">

<img src="https://media.giphy.com/media/juua9i2c2fA0AIp2iq/giphy.gif" width="180"/>

# Tech Stack

The project is built using a modern technology stack for **Machine Learning**, **Backend Development**, and **Frontend Engineering**.

<br>

### Languages & Frameworks

<img src="https://skillicons.dev/icons?i=python,fastapi,html,css,js" />

<br><br>

### Machine Learning

<img src="https://skillicons.dev/icons?i=sklearn" />

<br><br>

### Tools & Development

<img src="https://skillicons.dev/icons?i=git,github,vscode" />

</div>

<br>

| Category | Technology |
|:---------|:-----------|
| **Programming Language** | Python 3.10+ |
| **Backend Framework** | FastAPI |
| **Machine Learning** | Random Forest Classifier (Scikit-Learn) |
| **Data Processing** | Pandas, NumPy |
| **Model Serialization** | Joblib |
| **Template Engine** | Jinja2 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Version Control** | Git & GitHub |
| **IDE** | Visual Studio Code |

<div align="center">

### Technology Workflow

```text
Python
   │
   ▼
FastAPI
   │
   ▼
Data Preprocessing
   │
   ▼
Random Forest Model
   │
   ▼
Prediction API
   │
   ▼
Responsive Web Interface
```

</div>


---

<div align="center">

<img src="https://media.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="180"/>

# Dataset

The predictive model is trained on carefully selected financial and credit-risk features to make accurate loan approval predictions. Each feature is preprocessed before being passed to the Random Forest Classifier.

</div>

<br>

| Feature | Type | Description |
|:--------|:----:|:------------|
| **Age** | Numerical | Age of the loan applicant |
| **Income** | Numerical | Annual income of the applicant |
| **Home Ownership** | Categorical | Housing status (Own, Rent, Mortgage) |
| **Employment Length** | Numerical | Total years of employment |
| **Loan Intent** | Categorical | Purpose of the loan |
| **Loan Amount** | Numerical | Requested loan amount |
| **Interest Rate** | Numerical | Interest rate offered |
| **Loan Grade** | Categorical | Internal risk grade (A–G) |
| **Credit History Length** | Numerical | Years of active credit history |
| **Historical Default** | Categorical | Previous loan default (Yes/No) |

<br>

<div align="center">

### Data Processing Pipeline

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
 Random Forest Model
        │
        ▼
 Loan Approval Prediction
```

</div>

<div align="center">

> **Well-preprocessed data is the foundation of accurate, reliable, and consistent machine learning predictions.**

</div>

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
