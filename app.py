from fastapi import FastAPI
import uvicorn
import pickle
from models import Patients

app=FastAPI()
model=pickle.load(open("model.h5","rb"))

@app.get("/{name}")
def hello(name):
    return {"Hello {} and welcome to this API".format(name)}

@app.get("/")
def greet():
    return {"Hello World!"}

@app.post("/predict")
def predict(req:Patients):
    age=req.age
    anaemia=req.anaemia
    creatinine_phosphokinase=req.creatinine_phosphokinase
    diabetes=req.diabetes
    ejection_fraction=req.ejection_fraction
    high_blood_pressure=req.high_blood_pressure
    platelets=req.platelets
    serum_creatinine=req.serum_creatinine
    serum_sodium=req.serum_sodium
    smoking=req.smoking
    time=req.time
    features=list([age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,smoking, time])
    predict=model.predict([features])
    probab=model.predict_proba([features])
    if(predict==1):
        return {"ans":"You have been tested positive with {} probability. That's why you have heart failure.".format(probab[0][1])}
    else:
        return {"ans":"You have been tested negative with {} probability. That's why you don't have heart failure. ".format(probab[0][0])}
    
    
if __name__=="__main__":
    uvicorn.run(app)