import joblib
import sklearn 

def detect_hypertension(features):
    model = joblib.load('hypertension_model.pkl')  # Load trained model
    result = model.predict(features)[0]  # get first prediction
    if result == 1:
        print("You have Hypertension problem")
        print("You have to take Care")
    else:
        print("No, you are Negative for Hypertension problem")

def input_data():
    print("\t  Hypertension Detection   \t")
    print("Enter the Details about you .....")
    # Age	Salt_Intake 	Stress_Score	BP_History	Sleep_Duration	BMI	Medication	Family_History	Exercise_Level	Smoking_Status
    Age = int(input("Enter Your Age: "))
    Salt_Intake = float(input('Enter The Salt Intake: '))
    Stress_Score = int(input('Enter the Stress Score: '))
    print('0 : Hypertension , 1 : Normal , 2 : Prehypertension')
    BP_History = int(input('Enter BP History: '))
    Sleep_Duration = int(input('Enter the Sleep Duration: '))
    BMI = int(input("Enter the Body mass index :"))
    print("Enter the values between 1-4")    
    Medication = int(input('Enter the BMI Medication: '))
    print("If family member has Hypertension \n Yes : 1 \n No : 0 ")
    Family_History = int(input("Enter your answer: "))
    print("Exercise Details :-  low : 1 , moderate : 2 , high : 3")    
    Exercise_Level = int(input("Enter the Exercise Level: ")) 
    print('Enter the Smoking status  \n Non-Smoker : 0 \n Smoker : 1')
    Smoking_Status = int(input("Enter the Smoking Status: "))
    
    return [[Age, Salt_Intake, Stress_Score, BP_History, Sleep_Duration,
             BMI,Medication, Family_History, Exercise_Level, Smoking_Status]]

try : 
  data = input_data() 
  detect_hypertension(data)
except ValueError : 
   print("Input the data properly ")