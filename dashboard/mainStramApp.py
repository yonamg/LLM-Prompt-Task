from main_interface_app import streamlit_app
from multiple_app import MultipleApp
import  entity_extraction as entity
import news_scoring as news_score
import data_preparing as data_prep

app = MultipleApp()
streamlit_app(app,entity,news_score,data_prep)