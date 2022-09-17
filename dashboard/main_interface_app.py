import streamlit as st
import logging
import os,sys,io
import pandas as pd


def streamlit_app(app,entity,news_score,data_prep):
    # Add all your application her

    app.add_app("Prompt Design",data_prep.data_preparing,pd.DataFrame)
    app.add_app("Entity Extraction", entity.entity_extraction,pd.DataFrame)
    app.add_app('News Artifact Scoring', news_score.news_scoring, pd.DataFrame)

    # The main app
    app.run()