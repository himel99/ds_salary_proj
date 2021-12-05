# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:11:29 2021

@author: ASUS
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
#print(df[df['Salary Estimate'] == '-1'])
salary  = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
#df['max_salary'] = min_hr.apply(lambda x: 0 if  else int(x.split('-')[1]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1] if len(x.split('-'))>1 else x.split('-')[0]))
#df[["min_salary", "max_salary"]] = min_hr.split("-").apply(pd.Series)
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state filed 

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if len(x.split(','))>1 else x.split(',')[0])
print(df.job_state.value_counts())

#age of company

df['age'] = df.Founded.apply(lambda x: x if x<1 else 2021 - x)

'''
#parsing of job description

#python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python.value_counts()
#R
df['R'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower()  else 0) 
#AWS
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

'''
print(df.columns)

df_out = df.drop(['Unnamed: 0'], axis = 1)
df_out.to_csv('salary_data_cleaned.csv', index = False)

pd.read_csv('salary_data_cleaned.csv')
print(pd)
