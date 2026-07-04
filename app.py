from fastapi import FastAPI

from pydantic import BaseModel

import pandas as pd
import joblib


from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from fastapi import Request
from fastapi import Form
# =========================================
# CREATE FASTAPI APP
# =========================================

app = FastAPI()

# templates

templates = Jinja2Templates(
    directory="templates"
)

# =========================================
# LOAD MODEL
# =========================================

model = joblib.load("model/loan_model.pkl")

# =========================================
# LOAD ENCODERS
# =========================================

home_encoder = joblib.load(
    "model/home_encoder.pkl"
)

intent_encoder = joblib.load(
    "model/intent_encoder.pkl"
)

grade_encoder = joblib.load(
    "model/grade_encoder.pkl"
)

# =========================================
# INPUT DATA MODEL
# =========================================


class LoanData(BaseModel):

    id: int

    person_age: int

    person_income: float

    person_home_ownership: str

    person_emp_length: float

    loan_intent: str

    loan_grade: str

    loan_amnt: float

    loan_int_rate: float

    loan_percent_income: float

    cb_person_cred_hist_length: int

# =========================================
# HOME ROUTE
# =========================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

# =========================================
# PREDICTION ROUTE
# =========================================

@app.post("/predict")
def predict_loan(data: LoanData):

    # Convert input into dictionary
    input_data = data.dict()

    # =====================================
    # ENCODE CATEGORICAL DATA
    # =====================================

    input_data["person_home_ownership"] = (
        home_encoder.transform(
            [input_data["person_home_ownership"]]
        )[0]
    )

    input_data["loan_intent"] = (
        intent_encoder.transform(
            [input_data["loan_intent"]]
        )[0]
    )

    input_data["loan_grade"] = (
        grade_encoder.transform(
            [input_data["loan_grade"]]
        )[0]
    )

    # =====================================
    # CONVERT TO DATAFRAME
    # =====================================

    input_df = pd.DataFrame([input_data])

    # =====================================
    # PREDICTION
    # =====================================

    prediction = model.predict(input_df)

    probability = model.predict_proba(
        input_df
    )[0][1]

    # =====================================
    # RETURN RESULT
    # =====================================

    if prediction[0] == 1:

        result = "Loan Approved"

    else:

        result = "Loan Rejected"

    return {

        "prediction": result,

        "approval_probability": float(probability)
    }
@app.post("/predict_form")
def predict_form(
    request: Request, # <-- Added request to render template
    person_age: int = Form(...),
    person_income: float = Form(...),
    person_home_ownership: str = Form(...),
    person_emp_length: float = Form(...),
    loan_intent: str = Form(...),
    loan_grade: str = Form(...),
    loan_amnt: float = Form(...),
    loan_int_rate: float = Form(...),
    loan_percent_income: float = Form(...),
    cb_person_cred_hist_length: int = Form(...)
):
    # =====================================
    # CREATE INPUT DATA
    # =====================================
    input_data = {
        "id": 11111,
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_cred_hist_length": cb_person_cred_hist_length
    }

    # =====================================
    # ENCODE CATEGORICAL DATA
    # =====================================
    input_data["person_home_ownership"] = (
        home_encoder.transform([input_data["person_home_ownership"]])[0]
    )
    input_data["loan_intent"] = (
        intent_encoder.transform([input_data["loan_intent"]])[0]
    )
    input_data["loan_grade"] = (
        grade_encoder.transform([input_data["loan_grade"]])[0]
    )

    # =====================================
    # DATAFRAME
    # =====================================
    input_df = pd.DataFrame([input_data])

    # =====================================
    # PREDICTION
    # =====================================
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1]

    # =====================================
    # RESULT
    # =====================================
    if prediction[0] == 1:
        result = "Loan Approved"
        status_color = "#10b981" # Emerald Green
    else:
        result = "Loan Rejected"
        status_color = "#f43f5e" # Rose Red
        
    prob_percentage = round(float(probability) * 100, 2)

    # Return the beautifully styled HTML template
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "prediction": result,
            "probability": prob_percentage,
            "status_color": status_color,
            "loan_amnt": loan_amnt
        }
    )