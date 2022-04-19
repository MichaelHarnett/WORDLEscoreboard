import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly import tools
from plotly.subplots import make_subplots

st.title('WORDLE SCOREBOARD')
st.info('next plan - make graphs for guesses interactive, and match the background of the site, opposed to just a white background. STill need a pie chart for total wins.')

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



#########################
##### guess counter #####
#########################

# x axis for graphs
guess_range = ['6', '5', '4', '3', '2', '1']

#michael
michael1wins = len(michaeldf[michaeldf.score == '1'])
michael2wins = len(michaeldf[michaeldf.score == '2'])
michael3wins = len(michaeldf[michaeldf.score == '3'])
michael4wins = len(michaeldf[michaeldf.score == '4'])
michael5wins = len(michaeldf[michaeldf.score == '5'])
michael6wins = len(michaeldf[michaeldf.score == '6'])
michael_guesscount = []
michael_guesscount.append(michael1wins)
michael_guesscount.append(michael2wins)
michael_guesscount.append(michael3wins)
michael_guesscount.append(michael4wins)
michael_guesscount.append(michael5wins)
michael_guesscount.append(michael6wins)
michael_guesscount = michael_guesscount[::-1]

#dad
dad1wins = len(daddf[daddf.score == '1'])
dad2wins = len(daddf[daddf.score == '2'])
dad3wins = len(daddf[daddf.score == '3'])
dad4wins = len(daddf[daddf.score == '4'])
dad5wins = len(daddf[daddf.score == '5'])
dad6wins = len(daddf[daddf.score == '6'])
dad_guesscount = []
dad_guesscount.append(dad1wins)
dad_guesscount.append(dad2wins)
dad_guesscount.append(dad3wins)
dad_guesscount.append(dad4wins)
dad_guesscount.append(dad5wins)
dad_guesscount.append(dad6wins)
dad_guesscount = dad_guesscount[::-1]


#danielle
danielle1wins = len(danielledf[danielledf.score == '1'])
danielle2wins = len(danielledf[danielledf.score == '2'])
danielle3wins = len(danielledf[danielledf.score == '3'])
danielle4wins = len(danielledf[danielledf.score == '4'])
danielle5wins = len(danielledf[danielledf.score == '5'])
danielle6wins = len(danielledf[danielledf.score == '6'])
danielle_guesscount = []
danielle_guesscount.append(danielle1wins)
danielle_guesscount.append(danielle2wins)
danielle_guesscount.append(danielle3wins)
danielle_guesscount.append(danielle4wins)
danielle_guesscount.append(danielle5wins)
danielle_guesscount.append(danielle6wins)
danielle_guesscount = danielle_guesscount[::-1]


#chris
chris1wins = len(chrisdf[chrisdf.score == '1'])
chris2wins = len(chrisdf[chrisdf.score == '2'])
chris3wins = len(chrisdf[chrisdf.score == '3'])
chris4wins = len(chrisdf[chrisdf.score == '4'])
chris5wins = len(chrisdf[chrisdf.score == '5'])
chris6wins = len(chrisdf[chrisdf.score == '6'])
chris_guesscount = []
chris_guesscount.append(chris1wins)
chris_guesscount.append(chris2wins)
chris_guesscount.append(chris3wins)
chris_guesscount.append(chris4wins)
chris_guesscount.append(chris5wins)
chris_guesscount.append(chris6wins)
chris_guesscount = chris_guesscount[::-1]






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
    
    
# guess chart 

mike_guessdict = zip(x_range, michael_guesscount)
mike_tempdf = pd.DataFrame(mike_guessdict)

st.bar_chart(mike_guessdict)

# michael_guesschart = plt.gca()
# michael_guesschart.invert_yaxis()
# michael_guesschart = michael_guesschart.barh(x_range, michael_guesscount)
#michael_guesschart.figure


#michael_chartdata = (x_range, michael_guesscount)

#plt.barh(x_range, michael_guesscount).figure

#st.bar_chart(x_range, michael_guesscount)




    

### danielle's info
st.header('Danielle')
st.write('Total Games Played:', danielle_totalgamesplayed, 'Games Won:', danielle_winnum, 'Games Lost:', danielle_lossnum, 'Games Missed:', danielle_missing_tot)
st.write('Win Percent:', danielle_winpercent)
st.write('Average Guess Score:', danielle_avg)
with st.expander('Missing Game Numbers'):
    st.write(danielle_missing)
    
#guess chart
danielle_guesschart = plt.gca()
danielle_guesschart.invert_yaxis()
danielle_guesschart = danielle_guesschart.barh(x_range, danielle_guesscount)
danielle_guesschart.figure
    

###Chris' info
st.header('Chris')
st.write('Total Games Played:', chris_totalgamesplayed, 'Games Won:', chris_winnum, 'Games Lost:', chris_lossnum, 'Games Missed:', chris_missing_tot)
st.write('Win Percent:', chris_winpercent)
st.write('Average Guess Score:', chris_avg)
with st.expander('Missing Game Numbers'):
    st.write(chris_missing)

    
#guess chart
chris_guesschart = plt.gca()
chris_guesschart.invert_yaxis()
chris_guesschart.barh(x_range, chris_guesscount)
chris_guesschart.figure
    
    
### Dad's info
st.header('Dad')
st.write('Total Games Played:', dad_totalgamesplayed, 'Games Won:', dad_winnum, 'Games Lost:', dad_lossnum, 'Games Missed:', dad_missing_tot)
st.write('Win Percent:', dad_winpercent)
st.write('Average Guess Score:', dad_avg)
with st.expander('Missing Game Numbers'):
    st.write(dad_missing)
    
# guess chart
dad_guesschart = plt.gca()
dad_guesschart.invert_yaxis()
dad_guesschart.barh(x_range, dad_guesscount)
dad_guesschart.figure