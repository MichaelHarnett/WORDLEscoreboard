import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from plotly import tools
from plotly.subplots import make_subplots

st.title('WORDLE SCOREBOARD')
st.info('Have included game totals - total, wins, and losses. plans next include claning the numbers to only show one decimal place. To also have guess totals like on the actual app. Also want a pie chart on top of the site to compare total wins')

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


##############################
##### missing games info #####
##############################

#me
michael_games = sorted(michaeldf.game_num)
michael_missing = [item for item in range(michael_games[0], michael_games[-1]+1) if item not in michael_games]
michael_missing_tot = len(michael_missing)

#danielle
danielle_games = sorted(danielledf.game_num)
danielle_missing = [item for item in range(danielle_games[0], danielle_games[-1]+1) if item not in danielle_games]
danielle_missing_tot = len(danielle_missing)

#chris
chris_games = sorted(chrisdf.game_num)
chris_missing = [item for item in range(chris_games[0], chris_games[-1]+1) if item not in chris_games]
chris_missing_tot = len(chris_missing)

#dad
dad_games = sorted(daddf.game_num)
dad_missing = [item for item in range(dad_games[0], dad_games[-1]+1) if item not in dad_games]
dad_missing_tot = len(dad_missing)



##################
##### prints #####
##################
### michael's info
st.header('Michael')
st.write('Total Games Played:', michael_totalgamesplayed, 'Games Won:', michael_winnum, 'Games Lost:', michael_lossnum, 'Games Missed:', michael_missing_tot)
st.write('Win Percent:' , michael_winpercent)
st.write('Average Guess Score:', michael_avg)
with st.expander('Missing Game Numbers'):
    st.write(michael_missing)
    

### danielle's info
st.header('Danielle')
st.write('Total Games Played:', danielle_totalgamesplayed, 'Games Won:', danielle_winnum, 'Games Lost:', danielle_lossnum, 'Games Missed:', danielle_missing_tot)
st.write('Win Percent:', danielle_winpercent)
st.write('Average Guess Score:', danielle_avg)
with st.expander('Missing Game Numbers'):
    st.write(danielle_missing)

###Chris' info
st.header('Chris')
st.write('Total Games Played:', chris_totalgamesplayed, 'Games Won:', chris_winnum, 'Games Lost:', chris_lossnum, 'Games Missed:', chris_missing_tot)
st.write('Win Percent:', chris_winpercent)
st.write('Average Guess Score:', chris_avg)
with st.expander('Missing Game Numbers'):
    st.write(chris_missing)

### Dad's info
st.header('Dad')
st.write('Total Games Played:', dad_totalgamesplayed, 'Games Won:', dad_winnum, 'Games Lost:', dad_lossnum, 'Games Missed:', dad_missing_tot)
st.write('Win Percent:', dad_winpercent)
st.write('Average Guess Score:', dad_avg)
with st.expander('Missing Game Numbers'):
    st.write(dad_missing)