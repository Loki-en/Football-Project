#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 21:17:38 2025

@author: wasif
this file reads excel files and exports them to excel
"""
import os
import pandas as pd

list_of_df = []
path="/Documents/GitHub/Football-Project/data/aggregates"
print(path)
for file_name in os.listdir(path):
    print("\n")
    print(file_name)
    print("\n")
    full_file_path = os.path.join(path, file_name)
    print(full_file_path)
    df = pd.read_csv(full_file_path)
    list_of_team_names = df['team_name'].unique().tolist()
   #change below for matches - different file types
    for value in list_of_team_names:
        print(value)
    #value = 'Melbourne Victory Football Club'
        filtered_df = df[df['team_name'] == value]
        list_of_df.append(filtered_df)
        print(value, "added to the list")
        value = value + ".xlsx"
        new_full_file_path = os.path.join(path, value)
        print(new_full_file_path)

        filtered_df.to_excel(new_full_file_path, index=False)
