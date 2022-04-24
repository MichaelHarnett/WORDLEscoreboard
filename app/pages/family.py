import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly import tools
from plotly.subplots import make_subplots

from multiapp import MultiApp

def app():
    st.title('Family')
    ################
    ### read ins ###
    ################
    #michael
    michaeldf = pd.read_csv('/tables/michaeldf.csv')
    michaelwindf = pd.read_csv('/tables/michaelwindf.csv')
    #danielle
    danielledf = pd.read_csv('/tables/danielledf.csv')
    daniellewindf = pd.read_csv('/tables/daniellewindf.csv')
    #chris
    chrisdf = pd.read_csv('/tables/chrisdf.csv')
    chriswindf = pd.read_csv('/tables/chriswindf.csv')
    #dad
    daddf = pd.read_csv('/tables/daddf.csv')
    dadwindf = pd.read_csv('/tables/dadwindf.csv')



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
    michaeldf.score = michaeldf.score.astype('str')
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
    daddf.score = daddf.score.astype('str')
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
    danielledf.score = danielledf.score.astype('str')
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
    chrisdf.score = chrisdf.score.astype('str')
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



    ##########################
    ##### WIN COMPARISON #####
    ##########################

    #easiest way is to make lits of just the data we need
    players = ['Michael', 'Danielle','Chris','Dad']
    scores = [len(michaelwindf), len(daniellewindf), len(chriswindf), len(dadwindf)]

    #becaue it can be zipped into a dict
    piezip = zip(players,scores)

    #easily turned into a dataframe
    piedf = pd.DataFrame(piezip, columns = ['Player','Score'])

    #sorted so that the winner is always on top/is pulled and bordered
    piedf.sort_values('Score', ascending = False, inplace = True)



    #and then added allllll togehter into one beautiful pie chart
    total_pie = px.pie(piedf, names = 'Player', values = 'Score',
                       title = 'TOTAL WINS', template = 'plotly_dark',
                      height = 600, width = 450)
    total_pie.update_traces(textinfo = 'label + value',pull = ([.2,0,0,0]),
                            textfont = dict(size = 20), hovertemplate = [
                                'WOW YOU\'RE WINNING','OK, YAAAAS','I mean, you\'re trying','LOSER'],
                           marker = dict(line = dict(color = 'white', width = [3.5,0,0,0])))
    total_pie.update_layout(
        title={
            'text': "TOTAL WINS",
            'y':.92,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
        title_font_size = 40,
        showlegend = False
    )

    st.plotly_chart(total_pie)


    #easiest way is to make lits of just the data we need
    players = ['Michael', 'Danielle','Chris','Dad']
    loss_scores = [michael_lossnum, danielle_lossnum, chris_lossnum, dad_lossnum]

    #becaue it can be zipped into a dict
    loss_piezip = zip(players,loss_scores)

    #easily turned into a dataframe
    loss_piedf = pd.DataFrame(loss_piezip, columns = ['Player','Losses'])

    #sorted so that the winner is always on top/is pulled and bordered
    loss_piedf.sort_values('Losses', ascending = False, inplace = True)



    #and then added allllll togehter into one beautiful pie chart
    loss_pie = px.pie(loss_piedf, names = 'Player', values = 'Losses',
                       title = 'TOTAL LOSSES', template = 'plotly_dark', color_discrete_sequence=px.colors.sequential.RdBu,
                      height = 600, width = 450)
    loss_pie.update_traces(textinfo = 'label + value',pull = ([.1,0,0,0]),
                            textfont = dict(size = 20), hovertemplate = [
                                'WOW YOU SUUUUUCK','BOOOO','maybe read a bit more?','you got this'],
                           marker = dict(line = dict(color = 'black', width = [6,0,0,0])))
    loss_pie.update_layout(#autosize = True,
        title={
            'text': "TOTAL LOSSES",
            'y':.92,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
        title_font_size = 40,
        showlegend = False
    )
    st.plotly_chart(loss_pie)


    ###############################
    ##### combined guesschart #####
    ###############################

    #reorganzing the data to low>high for combined chart
    grouped_xlabels = ['player','1','2','3','4','5','6']

    michael_guesscount2 = (michael_guesscount[::-1])
    michael_guesscount2.insert(0, 'Michael')

    danielle_guesscount2 = (danielle_guesscount[::-1])
    danielle_guesscount2.insert(0, 'Danielle')

    chris_guesscount2 = (chris_guesscount[::-1])
    chris_guesscount2.insert(0, 'Chris')

    dad_guesscount2 = (dad_guesscount[::-1])
    dad_guesscount2.insert(0, 'Dad')


    #creating combined df
    windf = pd.DataFrame([(michael_guesscount2),
                           (danielle_guesscount2),
                           (chris_guesscount2),
                           (dad_guesscount2)], columns = grouped_xlabels)


    #melting into single columns 
    melted_wins = pd.melt(windf, id_vars = ['player'], var_name = 'guesses', value_vars = ['1','2','3',
                                                                 '4','5','6'])


    #combined chart graph
    combined_chart = px.bar(melted_wins, x = 'guesses', y = 'value', color = 'player',
                             barmode= 'group', template = 'plotly_dark', title = 'COMBINED GUESS COUNTS',
                            labels = {'variable':'Guesses', 'value':'Games'})
    combined_chart.update_layout(title = {'text': 'COMBINED GUESS COUNTS',
                                           'y' : .92,
                                           'x' : .5,
                                           'xanchor' : 'center',
                                           'yanchor' : 'top'},
                                  title_font_size = 40)

    st.plotly_chart(combined_chart)






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

    michael_guesschart = px.bar(x = michael_guesscount, y = guess_range, orientation = 'h',labels = {
                    'x' : 'Number of Games',
                    'y' : 'Guess Count'
                })
    michael_guesschart.update_traces(hovertemplate=None)
    michael_guesschart.update_layout(hovermode="y")
    st.plotly_chart(michael_guesschart)





    ### danielle's info
    st.header('Danielle')
    st.write('Total Games Played:', danielle_totalgamesplayed, 'Games Won:', danielle_winnum, 'Games Lost:', danielle_lossnum, 'Games Missed:', danielle_missing_tot)
    st.write('Win Percent:', danielle_winpercent)
    st.write('Average Guess Score:', danielle_avg)
    with st.expander('Missing Game Numbers'):
        st.write(danielle_missing)

    #guess chart
    danielle_guesschart = px.bar(x = danielle_guesscount, y = guess_range, orientation = 'h', labels = {
                    'x' : 'Number of Games',
                    'y' : 'Guess Count'
                })
    danielle_guesschart.update_traces(hovertemplate=None)
    danielle_guesschart.update_layout(hovermode="y")
    st.plotly_chart(danielle_guesschart)


    ###Chris' info
    st.header('Chris')
    st.write('Total Games Played:', chris_totalgamesplayed, 'Games Won:', chris_winnum, 'Games Lost:', chris_lossnum, 'Games Missed:', chris_missing_tot)
    st.write('Win Percent:', chris_winpercent)
    st.write('Average Guess Score:', chris_avg)
    with st.expander('Missing Game Numbers'):
        st.write(chris_missing)


    #guess chart
    chris_guesschart = px.bar(x = chris_guesscount, y = guess_range, orientation = 'h', labels = {
                    'x' : 'Number of Games',
                    'y' : 'Guess Count'
                })
    chris_guesschart.update_traces(hovertemplate=None)
    chris_guesschart.update_layout(hovermode="y")
    st.plotly_chart(chris_guesschart)



    ### Dad's info
    st.header('Dad')
    st.write('Total Games Played:', dad_totalgamesplayed, 'Games Won:', dad_winnum, 'Games Lost:', dad_lossnum, 'Games Missed:', dad_missing_tot)
    st.write('Win Percent:', dad_winpercent)
    st.write('Average Guess Score:', dad_avg)
    with st.expander('Missing Game Numbers'):
        st.write(dad_missing)

    # guess chart
    dad_guesschart = px.bar(x = dad_guesscount, y = guess_range, orientation = 'h', labels = {
                    'x' : 'Number of Games',
                    'y' : 'Guess Count'
                })
    dad_guesschart.update_traces(hovertemplate=None)
    dad_guesschart.update_layout(hovermode="y")
    st.plotly_chart(dad_guesschart)