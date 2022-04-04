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



########################
##### calculations #####
########################

### win percents
michael_winpercent = (len(michaelwindf)/len(michaeldf)*100)
dad_winpercent = (len(dadwindf)/len(daddf)*100)
danielle_winpercent = (len(daniellewindf)/len(danielledf)*100)
chris_winpercent = (len(chriswindf)/len(chrisdf)*100)

### average guesses
michaelwindf.score = michaelwindf.score.astype(int)
michael_avg = michaelwindf.score.sum()/len(michaelwindf)

daniellewindf.score = daniellewindf.score.astype(int)
danielle_avg = daniellewindf.score.sum()/len(daniellewindf)

chriswindf.score = chriswindf.score.astype(int)
chris_avg = chriswindf.score.sum()/len(chriswindf)

dadwindf.score = dadwindf.score.astype(int)
dad_avg = dadwindf.score.sum()/len(dadwindf)

################################
##### games played numbers #####
################################
#michael
michael_totalgamesplayed = len(michaeldf)
michael_winnum = len(michaelwindf)
michael_lossnum = len(michaeldf)-len(michaelwindf)

#danielle
danielle_totalgamesplayed = len(danielledf)
danielle_winnum = len(daniellewindf)
danielle_lossnum = len(danielledf)-len(daniellewindf)

#chris
chris_totalgamesplayed = len(chrisdf)
chris_winnum = len(chriswindf)
chris_lossnum = len(chrisdf)-len(chriswindf)

#dad
dad_totalgamesplayed = len(daddf)
dad_winnum = len(dadwindf)
dad_lossnum = len(daddf)-len(dadwindf)


##################
##### prints #####
##################
### michael's info
st.header('Michael')
st.write('Total games played:', michael_totalgamesplayed, 'Games won:', michael_winnum, 'Games lost:', michael_lossnum)
st.write('Win percent:' , michael_winpercent)
st.write('Average guess score:', michael_avg)

### danielle's info
st.header('Danielle')
st.write('Total games played:', danielle_totalgamesplayed, 'Games won:', danielle_winnum, 'Games lost:', danielle_lossnum)
st.write('Win percent:', danielle_winpercent)
st.write('Average guess score:', danielle_avg)

###Chris' info
st.header('Chris')
st.write('Total games played:', chris_totalgamesplayed, 'Games won:', chris_winnum, 'Games lost:', chris_lossnum)
st.write('Win percent:', chris_winpercent)
st.write('Average guess score:', chris_avg)

### Dad's info
st.header('Dad')
st.write('Total games played:', dad_totalgamesplayed, 'Games won:', dad_winnum, 'Games lost:', dad_lossnum)
st.write('Win percent:', dad_winpercent)
st.write('Average guess score:', dad_avg)