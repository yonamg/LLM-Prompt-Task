import missingno as msno
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.cluster import KMeans
import streamlit as st

import os
import sys
import logging
import numpy as np
import pandas as pd


def data_preparing(df: pd.DataFrame):

    df = pd.read_csv('../data/Example_data2.csv')
    st.write('# Promt Design')
    st.write('## Prompt Desigin for the Scoring')
    st.write('Get the news data')
    st.dataframe(df)
    st.write('### Generate prompt from the dataframe')

    dpart = st.selectbox(
        'Select Document Part', ('Title', 'Description', 'Body'))
    st.write('## Prompt Design for the Entity Extraction')
    
    df = pd.read_json(
            '/data/relations_training.txt')
    st.dataframe(df)
    st.write('### Generate prompt from job description')