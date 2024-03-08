from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from joblib import load
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")
model = load("models/Random_Forest.joblib")

def map_prediction(prediction):
    if prediction == 0:
        return "Spam"
    elif prediction == 1:
        return "Phishing Attack"
    elif prediction == 2:
        return "Malware"
    elif prediction == 3:
        return "Benign"
    else:
        return "Unknown"

@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict(request: Request,
                  sld: int = Form(...),
                  puny_coded: int = Form(...),
                  Alexa_Rank: float = Form(...),
                  distance_from_bad_words: float = Form(...),
                  Country: int = Form(...),
                  State: int = Form(...),
                  obfuscate_at_sign: int = Form(...),
                  entropy: float = Form(...),
                  numeric_percentage: float = Form(...),
                  subdomain: float = Form(...),
                  shortened: int = Form(...),
                  longest_word: int = Form(...),
                  Name_Server_Count: int = Form(...),
                  tld: int = Form(...),
                  Domain_Age_in_days: int = Form(...),
                  Creation_year: float = Form(...),
                  Creation_month: float = Form(...),
                  Creation_day: float = Form(...),
                  Creation_hour: float = Form(...),
                  Creation_minute: float = Form(...),
                  Creation_second: float = Form(...)
                  ):
    
    # Prepare input features as numpy array
    features = np.array([
        [sld, puny_coded, Alexa_Rank, distance_from_bad_words, Country, State, obfuscate_at_sign, entropy, numeric_percentage, subdomain,
        shortened, longest_word, Name_Server_Count, tld, Domain_Age_in_days, Creation_year, Creation_month, Creation_day, Creation_hour, Creation_minute, Creation_second]
    ])
    
    # Make prediction
    prediction = model.predict(features)
    
    # Map prediction to corresponding label
    prediction_label = map_prediction(prediction[0])
    
    # Prepare response
    return templates.TemplateResponse("prediction.html", {"request": request, "prediction": prediction_label})
