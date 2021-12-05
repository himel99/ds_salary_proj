# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 01:52:40 2021

@author: ASUS
"""

import glassdoor_scraper as gs
import pandas as pd


path = "F:/Python/ds_salary_proj/chromedriver"
df = gs.get_jobs('Data Scientist',15,False, path, 15) 

df.to_csv("glassdoor_jobs.csv")