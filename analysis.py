import pandas as pd
import numpy as np

df = pd.read_csv('covid19.csv',sep=',',
                 usecols=['PATIENT_TYPE','SEX','AGE','PNEUMONIA','COPD','ASTHMA','INMSUPR',
                          'HIPERTENSION','OTHER_DISEASE','CARDIOVASCULAR','DIABETES','OBESITY','RENAL_CHRONIC',
                          'TOBACCO','CLASIFFICATION_FINAL','ICU'],dtype=int)
df.head(5)


