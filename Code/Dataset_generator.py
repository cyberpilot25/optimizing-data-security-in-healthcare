import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

#Added cancer types and relevant treatments and medications
# Initialize Faker
fake = Faker()

# Define the columns for the dataset in the requested order
columns = ['Patient ID', 'Name', 'DOB', 'Age', 'Gender', 'Patient Address', 'Ailment', 'Patient Complaint',
         'Family Medical History', 'Negative Lifestyle Factor', 'Genetic Predisposition', 'Treatment',
         'Medications', 'Lab Results', 'Physician Notes', 'Next Follow-up Date']

# Generate data for 1000 patients
num_patients = 1000

# Patient ID
patient_ids = [f'P{i:04d}' for i in range(1, num_patients + 1)]

# Age distribution skewed towards older population (more common in healthcare)
ages = np.random.choice(
  [np.random.randint(0, 18),
   np.random.randint(19, 40),
   np.random.randint(41, 65),
   np.random.randint(66, 100)],
  size=num_patients,
  p=[0.2, 0.3, 0.3, 0.2]
)

# Calculate DOB based on current date and age
today = pd.to_datetime('2024-10-05')
dobs = []
for age in ages:
  # Randomly generate month and day
  year = today.year - age
  month = random.randint(1, 12)
  # Ensure the day is valid for the month
  day = random.randint(1, 28) if month == 2 else random.randint(1, 30) if month in [4, 6, 9, 11] else random.randint(1, 31)
  dob = datetime(year, month, day).date()
  dobs.append(dob)

# Gender
genders = np.random.choice(['Male', 'Female'], size=num_patients)

# More varied and realistic conditions
conditions = [
  'Hypertension', 'Diabetes', 'High Cholesterol', 'Asthma', 'Arthritis', 'Depression', 'Anxiety', 'COPD',
  'Heart Disease', 'Breast Cancer', 'Lung Cancer', 'Prostate Cancer', 'Colorectal Cancer', 'Flu', 'Pneumonia',
  'Osteoporosis', 'GERD', 'Migraine', 'COVID-19', 'Stroke', 'Alzheimer\'s Disease', 'Parkinson\'s Disease',
  'Chronic Kidney Disease', 'Liver Cirrhosis', 'Tuberculosis', 'HIV/AIDS', 'Multiple Sclerosis', 'Epilepsy'
]

# Adjusted probabilities to ensure they are non-negative and sum to 1
condition_probabilities = [
  0.10, 0.09, 0.08, 0.07, 0.07, 0.06, 0.06, 0.05, 0.05, 0.03, 0.03, 0.03, 0.03, 0.04, 0.04, 0.03, 0.04, 0.04, 0.03, 0.02,
  0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01
]

# Normalize the probabilities to ensure they sum to 1
total_probability = sum(condition_probabilities)
condition_probabilities = [p / total_probability for p in condition_probabilities]

# Generate ailments with gender-specific conditions
ailments = []
for gender in genders:
  if gender == 'Male':
      gender_specific_conditions = ['Prostate Cancer']
  else:
      gender_specific_conditions = ['Breast Cancer']
  
  # Filter conditions and probabilities
  possible_conditions = [c for c in conditions if c not in gender_specific_conditions]
  possible_probabilities = [condition_probabilities[conditions.index(c)] for c in possible_conditions]
  
  # Normalize probabilities for the filtered conditions
  total_possible_probability = sum(possible_probabilities)
  possible_probabilities = [p / total_possible_probability for p in possible_probabilities]
  
  ailment = np.random.choice(possible_conditions, p=possible_probabilities)
  ailments.append(ailment)

# Treatments aligned with conditions
treatment_map = {
  'Hypertension': ['Medication', 'Lifestyle Changes', 'Blood Pressure Monitoring'],
  'Diabetes': ['Medication', 'Insulin Therapy', 'Dietary Management'],
  'High Cholesterol': ['Medication', 'Lifestyle Changes', 'Lipid Panel'],
  'Asthma': ['Inhaler', 'Medication', 'Pulmonary Function Test'],
  'Arthritis': ['Medication', 'Physical Therapy', 'Joint Injection'],
  'Depression': ['Therapy', 'Medication', 'Psychotherapy'],
  'Anxiety': ['Therapy', 'Medication', 'Cognitive Behavioral Therapy'],
  'COPD': ['Inhaler', 'Medication', 'Oxygen Therapy', 'Pulmonary Rehabilitation'],
  'Heart Disease': ['Medication', 'Angioplasty', 'Bypass Surgery'],
  'Breast Cancer': ['Surgery', 'Chemotherapy', 'Radiation Therapy', 'Hormone Therapy'],
  'Lung Cancer': ['Surgery', 'Chemotherapy', 'Radiation Therapy', 'Targeted Therapy'],
  'Prostate Cancer': ['Surgery', 'Radiation Therapy', 'Hormone Therapy', 'Chemotherapy'],
  'Colorectal Cancer': ['Surgery', 'Chemotherapy', 'Radiation Therapy', 'Targeted Therapy'],
  'Flu': ['Rest', 'Fluids', 'Antiviral Medication'],
  'Pneumonia': ['Antibiotics', 'Hospitalization', 'Chest X-ray'],
  'Osteoporosis': ['Medication', 'Calcium & Vitamin D Supplements', 'Bone Density Scan'],
  'GERD': ['Medication', 'Lifestyle Changes', 'Endoscopy'],
  'Migraine': ['Medication', 'Trigger Avoidance', 'Lifestyle Changes'],
  'COVID-19': ['Isolation', 'Antiviral Medication', 'Oxygen Therapy'],
  'Stroke': ['Thrombolysis', 'Rehabilitation', 'Antiplatelet Therapy'],
  'Alzheimer\'s Disease': ['Cognitive Therapy', 'Medication', 'Supportive Care'],
  'Parkinson\'s Disease': ['Medication', 'Physical Therapy', 'Deep Brain Stimulation'],
  'Chronic Kidney Disease': ['Dialysis', 'Medication', 'Dietary Management'],
  'Liver Cirrhosis': ['Medication', 'Lifestyle Changes', 'Liver Transplant'],
  'Tuberculosis': ['Antibiotics', 'Isolation', 'Nutritional Support'],
  'HIV/AIDS': ['Antiretroviral Therapy', 'Supportive Care', 'Regular Monitoring'],
  'Multiple Sclerosis': ['Immunotherapy', 'Physical Therapy', 'Symptom Management'],
  'Epilepsy': ['Anticonvulsant Medication', 'Lifestyle Changes', 'Surgery']
}

# Generate treatments based on conditions
treatments = [random.choice(treatment_map[condition]) for condition in ailments]

# Map ailments to more realistic patient complaints
ailment_to_complaint = {
  'Hypertension': ['Frequent headaches', 'Dizziness', 'Shortness of breath', 'No symptoms'],
  'Diabetes': ['Excessive thirst', 'Frequent urination', 'Unexplained weight loss', 'Blurred vision'],
  'High Cholesterol': ['No symptoms', 'Chest pain (if severe)', 'Shortness of breath (if severe)', 'None'],
  'Asthma': ['Wheezing', 'Chest tightness', 'Shortness of breath', 'Coughing'],
  'Arthritis': ['Joint pain and stiffness', 'Swelling in joints', 'Limited range of motion', 'Fatigue'],
  'Depression': ['Persistent sadness', 'Loss of interest or pleasure', 'Changes in appetite or weight', 'Sleep disturbances'],
  'Anxiety': ['Excessive worry', 'Restlessness', 'Difficulty concentrating', 'Panic attacks'],
  'COPD': ['Shortness of breath', 'Chronic cough with mucus', 'Wheezing', 'Chest tightness'],
  'Heart Disease': ['Chest pain or discomfort', 'Shortness of breath', 'Fatigue', 'Swelling in legs, ankles, or feet'],
  'Breast Cancer': ['Lump in breast', 'Change in breast shape', 'Skin changes', 'Nipple discharge'],
  'Lung Cancer': ['Persistent cough', 'Chest pain', 'Shortness of breath', 'Coughing up blood'],
  'Prostate Cancer': ['Frequent urination', 'Weak urine stream', 'Blood in urine', 'Pelvic discomfort'],
  'Colorectal Cancer': ['Change in bowel habits', 'Blood in stool', 'Abdominal discomfort', 'Unexplained weight loss'],
  'Flu': ['Fever', 'Cough', 'Sore throat', 'Muscle aches'],
  'Pneumonia': ['Cough with phlegm', 'Fever', 'Chills', 'Shortness of breath'],
  'Osteoporosis': ['Back pain', 'Loss of height', 'Stooped posture', 'Bone fracture'],
  'GERD': ['Heartburn', 'Regurgitation', 'Difficulty swallowing', 'Chest pain'],
  'Migraine': ['Throbbing headache', 'Nausea and vomiting', 'Sensitivity to light and sound', 'Aura'],
  'COVID-19': ['Fever', 'Cough', 'Loss of taste or smell', 'Shortness of breath'],
  'Stroke': ['Sudden numbness or weakness', 'Confusion', 'Trouble speaking', 'Loss of balance'],
  'Alzheimer\'s Disease': ['Memory loss', 'Difficulty completing familiar tasks', 'Confusion with time or place', 'Changes in mood'],
  'Parkinson\'s Disease': ['Tremor', 'Slowed movement', 'Rigid muscles', 'Impaired posture and balance'],
  'Chronic Kidney Disease': ['Fatigue', 'Swelling in feet and ankles', 'Frequent urination', 'Muscle cramps'],
  'Liver Cirrhosis': ['Fatigue', 'Easy bruising', 'Jaundice', 'Swelling in legs'],
  'Tuberculosis': ['Persistent cough', 'Chest pain', 'Coughing up blood', 'Night sweats'],
  'HIV/AIDS': ['Fever', 'Swollen lymph nodes', 'Chronic diarrhea', 'Weight loss'],
  'Multiple Sclerosis': ['Numbness or weakness', 'Tingling or pain', 'Electric-shock sensations', 'Tremor'],
  'Epilepsy': ['Seizures', 'Temporary confusion', 'Staring spells', 'Uncontrollable jerking movements']
}

# Generate multiple symptoms for patient complaints
patient_complaints = [
  ', '.join(random.sample(ailment_to_complaint[condition], k=random.randint(1, 3)))
  for condition in ailments
]

# Generate family medical history with more specific details
family_medical_histories = [
  'Heart disease in father',
  'Breast cancer in mother',
  'Diabetes in sibling',
  'Alzheimer\'s in grandparent',
  'High blood pressure in father',
  'Parent is HIV positive',
  'Stroke in grandparent',
  'Parkinson\'s disease in uncle',
  'Liver disease in mother',
  'Tuberculosis in grandparent',
  'Multiple sclerosis in aunt',
  'Epilepsy in sibling',
  'None'
]
# Adjust probabilities to sum to 1
family_history_probabilities = [0.05] * 12 + [0.4]
family_histories = np.random.choice(family_medical_histories, size=num_patients, p=family_history_probabilities)

# Generate negative lifestyle factors with more specific details
negative_lifestyle_factors = [
  'Smoking (1 pack/day)',
  'Heavy alcohol use',
  'Sedentary lifestyle',
  'High-fat diet',
  'Stressful life',
  'Poor sleep habits',
  'Excessive caffeine consumption',
  'Recreational drug use',
  'Irregular meal patterns',
  'High sugar intake',
  'None'
]
lifestyle_factors = np.random.choice(negative_lifestyle_factors, size=num_patients)

# Generate genetic predispositions with more specific details
genetic_predispositions = [
  'BRCA1 mutation',
  'Familial hypercholesterolemia',
  'Early-onset Alzheimer\'s',
  'Lynch syndrome',
  'Huntington\'s disease',
  'Cystic fibrosis carrier',
  'Sickle cell trait',
  'Hemophilia',
  'Tay-Sachs disease carrier',
  'Polycystic kidney disease',
  'None'
]
genetic_factors = np.random.choice(genetic_predispositions, size=num_patients)

# Map ailments to medications with dosage information
ailment_to_medication = {
  'Hypertension': ['Lisinopril 10mg daily', 'Amlodipine 5mg daily', 'Hydrochlorothiazide 25mg daily'],
  'Diabetes': ['Metformin 500mg twice daily', 'Insulin glargine 10 units at bedtime', 'Glipizide 5mg daily'],
  'High Cholesterol': ['Atorvastatin 20mg daily', 'Simvastatin 40mg daily', 'Rosuvastatin 10mg daily'],
  'Asthma': ['Albuterol inhaler 2 puffs as needed', 'Fluticasone inhaler 2 puffs twice daily', 'Montelukast 10mg daily'],
  'Arthritis': ['Ibuprofen 400mg three times daily', 'Naproxen 500mg twice daily', 'Celecoxib 200mg daily'],
  'Depression': ['Sertraline 50mg daily', 'Fluoxetine 20mg daily', 'Escitalopram 10mg daily'],
  'Anxiety': ['Alprazolam 0.25mg as needed', 'Lorazepam 1mg as needed', 'Buspirone 15mg twice daily'],
  'COPD': ['Tiotropium inhaler 1 puff daily', 'Salmeterol inhaler 2 puffs twice daily', 'Fluticasone/Salmeterol inhaler 2 puffs twice daily'],
  'Heart Disease': ['Aspirin 81mg daily', 'Clopidogrel 75mg daily', 'Atorvastatin 40mg daily'],
  'Breast Cancer': ['Tamoxifen 20mg daily', 'Anastrozole 1mg daily', 'Letrozole 2.5mg daily'],
  'Lung Cancer': ['Cisplatin 75mg/m2', 'Etoposide 100mg/m2', 'Pembrolizumab 200mg'],
  'Prostate Cancer': ['Leuprolide 7.5mg monthly', 'Bicalutamide 50mg daily', 'Docetaxel 75mg/m2'],
  'Colorectal Cancer': ['5-Fluorouracil 500mg/m2', 'Leucovorin 200mg/m2', 'Oxaliplatin 85mg/m2'],
  'Flu': ['None', 'Oseltamivir 75mg twice daily'],
  'Pneumonia': ['Amoxicillin 500mg three times daily', 'Azithromycin 500mg once daily for 3 days', 'Levofloxacin 750mg once daily'],
  'Osteoporosis': ['Alendronate 70mg weekly', 'Risedronate 35mg weekly', 'Ibandronate 150mg monthly'],
  'GERD': ['Omeprazole 20mg daily', 'Ranitidine 150mg twice daily', 'Esomeprazole 40mg daily'],
  'Migraine': ['Sumatriptan 50mg as needed', 'Rizatriptan 10mg as needed', 'Propranolol 40mg daily'],
  'COVID-19': ['Remdesivir 200mg on day 1, then 100mg daily', 'Dexamethasone 6mg daily', 'Supportive care'],
  'Stroke': ['Aspirin 325mg daily', 'Clopidogrel 75mg daily', 'Atorvastatin 80mg daily'],
  'Alzheimer\'s Disease': ['Donepezil 10mg daily', 'Memantine 10mg twice daily', 'Rivastigmine 6mg twice daily'],
  'Parkinson\'s Disease': ['Levodopa/Carbidopa 100/25mg three times daily', 'Pramipexole 0.5mg three times daily', 'Rasagiline 1mg daily'],
  'Chronic Kidney Disease': ['Erythropoietin injections', 'Calcium acetate 667mg with meals', 'Lisinopril 10mg daily'],
  'Liver Cirrhosis': ['Spironolactone 100mg daily', 'Furosemide 40mg daily', 'Lactulose 30ml three times daily'],
  'Tuberculosis': ['Isoniazid 300mg daily', 'Rifampin 600mg daily', 'Ethambutol 15mg/kg daily'],
  'HIV/AIDS': ['Tenofovir/Emtricitabine 300/200mg daily', 'Efavirenz 600mg daily', 'Dolutegravir 50mg daily'],
  'Multiple Sclerosis': ['Interferon beta-1a 44mcg three times weekly', 'Glatiramer acetate 20mg daily', 'Fingolimod 0.5mg daily'],
  'Epilepsy': ['Levetiracetam 500mg twice daily', 'Lamotrigine 100mg twice daily', 'Valproic acid 500mg twice daily']
}
medications = [random.choice(ailment_to_medication[condition]) for condition in ailments]

# Generate lab results occasionally
def generate_lab_results(condition):
  if random.random() < 0.7:  # 70% chance to provide lab results
      results = {
          "Blood Pressure": f"{random.randint(110, 160)}/{random.randint(70, 100)}",
          "Cholesterol": f"{random.randint(150, 250)} mg/dL",
          "Blood Sugar": f"{random.randint(70, 150)} mg/dL",
          "Urine Protein": f"{random.choice(['Negative', 'Trace', '1+', '2+', '3+'])}",
          "Urine Glucose": f"{random.choice(['Negative', 'Trace', '1+', '2+', '3+'])}",
          "HDL": f"{random.randint(40, 60)} mg/dL",
          "LDL": f"{random.randint(100, 160)} mg/dL",
          "Triglycerides": f"{random.randint(50, 150)} mg/dL"
      }
      # Select a few relevant results based on the condition
      relevant_tests = {
          'Hypertension': ['Blood Pressure'],
          'Diabetes': ['Blood Sugar', 'Urine Glucose'],
          'High Cholesterol': ['Cholesterol', 'HDL', 'LDL'],
          'Asthma': [],
          'Arthritis': [],
          'Depression': [],
          'Anxiety': [],
          'COPD': [],
          'Heart Disease': ['Blood Pressure', 'Cholesterol'],
          'Breast Cancer': [],
          'Lung Cancer': [],
          'Prostate Cancer': [],
          'Colorectal Cancer': [],
          'Flu': [],
          'Pneumonia': [],
          'Osteoporosis': [],
          'GERD': [],
          'Migraine': [],
          'COVID-19': [],
          'Stroke': ['Blood Pressure'],
          'Alzheimer\'s Disease': [],
          'Parkinson\'s Disease': [],
          'Chronic Kidney Disease': ['Blood Pressure', 'Urine Protein'],
          'Liver Cirrhosis': [],
          'Tuberculosis': [],
          'HIV/AIDS': [],
          'Multiple Sclerosis': [],
          'Epilepsy': []
      }
      selected_tests = relevant_tests.get(condition, [])
      if selected_tests:
          return ', '.join(f"{test}: {results[test]}" for test in selected_tests if test in results)
      else:
          return 'None'
  else:
      return 'None'

lab_results = [generate_lab_results(condition) for condition in ailments]

# Generate physician notes with names
physician_names = [fake.name() for _ in range(num_patients)]

# Create notes for each patient
notes = [
  random.choice([
      f"Patient advised to follow up in 3 months. - Dr. {physician_names[i]}",
      f"Discussed lifestyle modifications, including diet and exercise. - Dr. {physician_names[i]}",
      f"Reviewed medication adherence; patient is compliant. - Dr. {physician_names[i]}",
      f"Patient reports improvement in symptoms; continue current treatment plan. - Dr. {physician_names[i]}",
      f"Further diagnostic tests recommended to assess condition progression. - Dr. {physician_names[i]}",
      f"Patient expressed concerns about side effects; adjusted medication dosage. - Dr. {physician_names[i]}",
      f"Encouraged smoking cessation and provided resources. - Dr. {physician_names[i]}",
      f"Blood pressure readings are stable; maintain current regimen. - Dr. {physician_names[i]}",
      f"Discussed potential surgical options; patient to consider. - Dr. {physician_names[i]}",
      f"Patient advised to monitor blood sugar levels closely. - Dr. {physician_names[i]}",
      f"Patient's cholesterol levels have improved; continue with current diet. - Dr. {physician_names[i]}",
      f"Recommended physical therapy to improve joint mobility. - Dr. {physician_names[i]}",
      f"Patient is experiencing mild side effects; consider alternative medication. - Dr. {physician_names[i]}",
      f"Advised patient to increase water intake and monitor hydration levels. - Dr. {physician_names[i]}",
      f"Patient's asthma is well-controlled; continue with current inhaler. - Dr. {physician_names[i]}",
      f"Discussed mental health resources and support groups. - Dr. {physician_names[i]}",
      f"Patient's weight is stable; continue with current exercise regimen. - Dr. {physician_names[i]}",
      f"Reviewed recent lab results; no significant changes noted. - Dr. {physician_names[i]}",
      f"Patient is advised to avoid high-sodium foods to manage blood pressure. - Dr. {physician_names[i]}",
      f"Encouraged patient to maintain a sleep schedule for better health outcomes. - Dr. {physician_names[i]}"
  ])
  for i in range(num_patients)
]

# Generate next follow-up date
follow_up_dates = [(today + timedelta(days=random.randint(30, 180))).date() for _ in range(num_patients)]

# Create a DataFrame
df = pd.DataFrame({
  'Patient ID': patient_ids,
  'Name': [fake.name() for _ in range(num_patients)],
  'DOB': dobs,
  'Age': ages,
  'Gender': genders,
  'Patient Address': [fake.address().replace("\n", ", ") for _ in range(num_patients)],  # Detailed address
  'Ailment': ailments,
  'Patient Complaint': patient_complaints,
  'Family Medical History': family_histories,
  'Negative Lifestyle Factor': lifestyle_factors,
  'Genetic Predisposition': genetic_factors,
  'Treatment': treatments,
  'Medications': medications,
  'Lab Results': lab_results,
  'Physician Notes': notes,
  'Next Follow-up Date': follow_up_dates
}, columns=columns)

# Save to a CSV file
df.to_csv("patient_raw_data.csv", index=False)

# Created/Modified files during execution:
print("Data stored to patient_raw_data.csv")