import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from plotly import tools
from plotly.subplots import make_subplots

st.title('WORDLE')

################
### read ins ###
################
#michael
michaeldf = pd.read_csv('tables/michaeldf.csv')
michaelwindf = pd.read_csv('tables/michaelwindf.csv')
#danielle
danielledf = pd.read_csv('tables/danielledf.csv')
daniellewindf = pd.read_csv('tables/daniellewindf.csv')
#chris
chrisdf = pd.read_csv('tables/chrisdf.csv')
chriswindf = pd.read_csv('tables/chriswindf.csv')
#dad
daddf = pd.read_csv('tables/daddf.csv')
dadwindf = pd.read_csv('tables/dadwindf.csv')


michael_winpercent = (len(michaelwindf)/len(michaeldf)*100)
dad_winpercent = (len(dadwindf)/len(daddf)*100)
danielle_winpercent = (len(daniellewindf)/len(danielledf)*100)
chris_winpercent = (len(chriswindf)/len(chrisdf)*100)


st.header('Michael')
st.write('Win percent:' , michael_winpercent)

st.header('Danielle')
st.write('Win percent:', danielle_winpercent)

st.header('Chris')
st.write('Win percent:', chris_winpercent)

st.header('Dad')
st.write('Win percent:', dad_winpercent)