import streamlit as st
import logging
import os,sys,io
import pandas as pd

def streamlit_app(app,data_pre,entity, news_scor):
    # Add all your application her

    app.add_app("Prompt Design",data_pre.data_preparation,pd.DataFrame)
    app.add_app("Entity Extraction", entity.entity_extraction,pd.DataFrame)
    app.add_app('News Artifact Scoring', news_scor.news_scoring, pd.DataFrame)

    # The main app
    app.run()