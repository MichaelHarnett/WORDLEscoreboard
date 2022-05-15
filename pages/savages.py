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
    st.title('savages')
    ################
    ### read ins ###
    ################
    #michael
    michaelSAVdf = pd.read_csv('./tables/michaelSAVdf.csv')
    michaelSAVwindf = pd.read_csv('./tables/michaelSAVwindf.csv')
    #kelly
    kelldf = pd.read_csv('./tables/kelldf.csv')
    kellwindf = pd.read_csv('./tables/kellwindf.csv')
    #nick
    nickdf = pd.read_csv('./tables/nickdf.csv')
    nickwindf = pd.read_csv('./tables/nickwindf.csv')
    #jose
    josedf = pd.read_csv('./tables/josedf.csv')
    josewindf = pd.read_csv('./tables/josewindf.csv')
    #savagesdf
    savagesdf = pd.read_csv('./tables/savagesdf.csv')



    ########################
    ##### calculations #####
    ########################

    ### win percents
    michaelSAV_winpercent = (len(michaelSAVwindf)/len(michaelSAVdf)*100)
    kell_winpercent = (len(kellwindf)/len(kelldf)*100)
    nick_winpercent = (len(nickwindf)/len(nickdf)*100)
    jose_winpercent = (len(josewindf)/len(josedf)*100)

    ### average guesses
    michaelSAVwindf.score = michaelSAVwindf.score.astype(int)
    michaelSAV_avg = michaelSAVwindf.score.sum()/len(michaelSAVwindf)

    kellwindf.score = kellwindf.score.astype(int)
    kell_avg = kellwindf.score.sum()/len(kellwindf)

    nickwindf.score = nickwindf.score.astype(int)
    nick_avg = nickwindf.score.sum()/len(nickwindf)

    josewindf.score = josewindf.score.astype(int)
    jose_avg = josewindf.score.sum()/len(josewindf)

    ################################
    ##### games played numbers #####
    ################################
    #michael
    michaelSAV_totalgamesplayed = len(michaelSAVdf)
    michaelSAV_winnum = len(michaelSAVwindf)
    michaelSAV_lossnum = len(michaelSAVdf)-len(michaelSAVwindf)

    #kell
    kell_totalgamesplayed = len(kelldf)
    kell_winnum = len(kellwindf)
    kell_lossnum = len(kelldf)-len(kellwindf)

    #nick
    nick_totalgamesplayed = len(nickdf)
    nick_winnum = len(nickwindf)
    nick_lossnum = len(nickdf)-len(nickwindf)

    #jose
    jose_totalgamesplayed = len(josedf)
    jose_winnum = len(josewindf)
    jose_lossnum = len(josedf)-len(josewindf)


    ##############################
    ##### missing games info #####
    ##############################

    #me
    michaelSAV_games = sorted(michaelSAVdf.game_num)
    michaelSAV_missing = [item for item in range(michaelSAV_games[0], michaelSAV_games[-1]+1) if item not in michaelSAV_games]
    michaelSAV_missing_tot = len(michaelSAV_missing)

    #kell
    kell_games = sorted(kelldf.game_num)
    kell_missing = [item for item in range(kell_games[0], kell_games[-1]+1) if item not in kell_games]
    kell_missing_tot = len(kell_missing)

    #nick
    nick_games = sorted(nickdf.game_num)
    nick_missing = [item for item in range(nick_games[0], nick_games[-1]+1) if item not in nick_games]
    nick_missing_tot = len(nick_missing)

    #jose
    jose_games = sorted(josedf.game_num)
    jose_missing = [item for item in range(jose_games[0], jose_games[-1]+1) if item not in jose_games]
    jose_missing_tot = len(jose_missing)



    #########################
    ##### guess counter #####
    #########################

    # x axis for graphs
    guess_range = ['6', '5', '4', '3', '2', '1']

    #michael
    michaelSAVdf.score = michaelSAVdf.score.astype('str')
    michaelSAV1wins = len(michaelSAVdf[michaelSAVdf.score == '1'])
    michaelSAV2wins = len(michaelSAVdf[michaelSAVdf.score == '2'])
    michaelSAV3wins = len(michaelSAVdf[michaelSAVdf.score == '3'])
    michaelSAV4wins = len(michaelSAVdf[michaelSAVdf.score == '4'])
    michaelSAV5wins = len(michaelSAVdf[michaelSAVdf.score == '5'])
    michaelSAV6wins = len(michaelSAVdf[michaelSAVdf.score == '6'])
    michaelSAV_guesscount = []
    michaelSAV_guesscount.append(michaelSAV1wins)
    michaelSAV_guesscount.append(michaelSAV2wins)
    michaelSAV_guesscount.append(michaelSAV3wins)
    michaelSAV_guesscount.append(michaelSAV4wins)
    michaelSAV_guesscount.append(michaelSAV5wins)
    michaelSAV_guesscount.append(michaelSAV6wins)
    michaelSAV_guesscount = michaelSAV_guesscount[::-1]

    #kell
    kelldf.score = kelldf.score.astype('str')
    kell1wins = len(kelldf[kelldf.score == '1'])
    kell2wins = len(kelldf[kelldf.score == '2'])
    kell3wins = len(kelldf[kelldf.score == '3'])
    kell4wins = len(kelldf[kelldf.score == '4'])
    kell5wins = len(kelldf[kelldf.score == '5'])
    kell6wins = len(kelldf[kelldf.score == '6'])
    kell_guesscount = []
    kell_guesscount.append(kell1wins)
    kell_guesscount.append(kell2wins)
    kell_guesscount.append(kell3wins)
    kell_guesscount.append(kell4wins)
    kell_guesscount.append(kell5wins)
    kell_guesscount.append(kell6wins)
    kell_guesscount = kell_guesscount[::-1]


    #nick
    nickdf.score = nickdf.score.astype('str')
    nick1wins = len(nickdf[nickdf.score == '1'])
    nick2wins = len(nickdf[nickdf.score == '2'])
    nick3wins = len(nickdf[nickdf.score == '3'])
    nick4wins = len(nickdf[nickdf.score == '4'])
    nick5wins = len(nickdf[nickdf.score == '5'])
    nick6wins = len(nickdf[nickdf.score == '6'])
    nick_guesscount = []
    nick_guesscount.append(nick1wins)
    nick_guesscount.append(nick2wins)
    nick_guesscount.append(nick3wins)
    nick_guesscount.append(nick4wins)
    nick_guesscount.append(nick5wins)
    nick_guesscount.append(nick6wins)
    nick_guesscount = nick_guesscount[::-1]


    #jose
    josedf.score = josedf.score.astype('str')
    jose1wins = len(josedf[josedf.score == '1'])
    jose2wins = len(josedf[josedf.score == '2'])
    jose3wins = len(josedf[josedf.score == '3'])
    jose4wins = len(josedf[josedf.score == '4'])
    jose5wins = len(josedf[josedf.score == '5'])
    jose6wins = len(josedf[josedf.score == '6'])
    jose_guesscount = []
    jose_guesscount.append(jose1wins)
    jose_guesscount.append(jose2wins)
    jose_guesscount.append(jose3wins)
    jose_guesscount.append(jose4wins)
    jose_guesscount.append(jose5wins)
    jose_guesscount.append(jose6wins)
    jose_guesscount = jose_guesscount[::-1]
    
    
    ########################
    ###### TEXT COUNT ######
    ########################
    
    txt_chart = px.bar(savagesdf,
                   x = list(savagesdf.player.value_counts().keys().str.capitalize()),
                   y = savagesdf.player.value_counts().values,
                   color = list(savagesdf.player.value_counts().keys()),
                   title = 'TOTAL TEXTS SENT',
                   template = 'plotly_dark',
                   labels = {'x':'Savage', 'y':'Texts Sent'},
                   text = savagesdf.player.value_counts().values
                  )
    txt_chart.update_traces(hovertext = 'values',
                           showlegend = False,)

    txt_chart.update_layout(
            title={
            'text': "TOTAL TEXTS SENT",
            'y':.92,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        title_font_size = 40
    )
    
    st.plotly_chart(txt_chart)
    



    ##########################
    ##### WIN COMPARISON #####
    ##########################

    #easiest way is to make lits of just the data we need
    sav_players = ['Michael Michaelson', 'Killa Kells','Nick Cosby','HOEsay']
    sav_scores = [len(michaelSAVwindf), len(kellwindf), len(nickwindf), len(josewindf)]

    #becaue it can be zipped into a dict
    sav_piezip = zip(sav_players,sav_scores)

    #easily turned into a dataframe
    sav_piedf = pd.DataFrame(sav_piezip, columns = ['Player','Score'])

    #sorted so that the winner is always on top/is pulled and bordered
    sav_piedf.sort_values('Score', ascending = False, inplace = True)



    #and then added allllll togehter into one beautiful pie chart
    sav_total_pie = px.pie(sav_piedf, names = 'Player', values = 'Score',
                       title = 'TOTAL WINS', template = 'plotly_dark',
                      height = 600, width = 450)
    sav_total_pie.update_traces(textinfo = 'label + value',pull = ([.2,0,0,0]),
                            textfont = dict(size = 20), hovertemplate = [
                                'WOW YOU\'RE WINNING','OK, YAAAAS','I mean, you\'re trying','LOSER'],
                           marker = dict(line = dict(color = 'white', width = [3.5,0,0,0])))
    sav_total_pie.update_layout(
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

    st.plotly_chart(sav_total_pie)
    
    #############################
    ##### LOSSES COMPARISON #####
    #############################

    #easiest way is to make lits of just the data we need
    sav_loss_scores = [michaelSAV_lossnum, kell_lossnum, nick_lossnum, jose_lossnum]

    #becaue it can be zipped into a dict
    sav_loss_piezip = zip(sav_players,sav_loss_scores)

    #easily turned into a dataframe
    sav_loss_piedf = pd.DataFrame(sav_loss_piezip, columns = ['Player','Losses'])

    #sorted so that the winner is always on top/is pulled and bordered
    sav_loss_piedf.sort_values('Losses', ascending = False, inplace = True)



    #and then added allllll togehter into one beautiful pie chart
    sav_loss_pie = px.pie(sav_loss_piedf, names = 'Player', values = 'Losses',
                          title = 'TOTAL LOSSES', template = 'plotly_dark',
                          color_discrete_sequence=px.colors.sequential.RdBu,
                          height = 600, width = 450)
    sav_loss_pie.update_traces(textinfo = 'label + value',pull = ([.1,0,0,0]),
                            textfont = dict(size = 20), hovertemplate = [
                                'WOW YOU SUUUUUCK','BOOOO','maybe read a bit more?','you got this'],
                           marker = dict(line = dict(color = 'black', width = [6,0,0,0])))
    sav_loss_pie.update_layout(#autosize = True,
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
    st.plotly_chart(sav_loss_pie)


    ###############################
    ##### combined guesschart #####
    ###############################

    #reorganzing the data to low>high for combined chart
    grouped_xlabels = ['player','1','2','3','4','5','6']

    michaelSAV_guesscount2 = (michaelSAV_guesscount[::-1])
    michaelSAV_guesscount2.insert(0, 'Michael Michaelson')

    kell_guesscount2 = (kell_guesscount[::-1])
    kell_guesscount2.insert(0, 'Killa Kells')

    nick_guesscount2 = (nick_guesscount[::-1])
    nick_guesscount2.insert(0, 'Nick Cosby')

    jose_guesscount2 = (jose_guesscount[::-1])
    jose_guesscount2.insert(0, 'HOEsay')


    #creating combined df
    sav_windf = pd.DataFrame([(michaelSAV_guesscount2),
                           (kell_guesscount2),
                           (nick_guesscount2),
                           (jose_guesscount2)], columns = grouped_xlabels)


    #melting into single columns 
    sav_melted_wins = pd.melt(sav_windf, id_vars = ['player'], var_name = 'guesses', value_vars = ['1','2','3',
                                                                 '4','5','6'])


    #combined chart graph
    sav_combined_chart = px.bar(sav_melted_wins, x = 'guesses', y = 'value', color = 'player',
                             barmode= 'group', template = 'plotly_dark', title = 'COMBINED GUESS COUNTS',
                            labels = {'variable':'Guesses', 'value':'Games'})
    sav_combined_chart.update_layout(title = {'text': 'COMBINED GUESS COUNTS',
                                           'y' : .92,
                                           'x' : .5,
                                           'xanchor' : 'center',
                                           'yanchor' : 'top'},
                                  title_font_size = 40)

    st.plotly_chart(sav_combined_chart)






    ##################
    ##### prints #####
    ##################
    ### michael's info
    st.header('Michael Michaelson')
    st.write('Total Games Played:', michaelSAV_totalgamesplayed, 'Games Won:', michaelSAV_winnum, 'Games Lost:',
             michaelSAV_lossnum, 'Games Missed:', michaelSAV_missing_tot)
    st.write('Win Percent:' , michaelSAV_winpercent)
    st.write('Average Guess Score:', michaelSAV_avg)
    with st.expander('Missing Game Numbers'):
        st.write(michaelSAV_missing)


    # guess chart 

    michaelSAV_guesschart = px.bar(x = michaelSAV_guesscount, y = guess_range, orientation = 'h',labels = {
                    'x' : 'Number of Games',
                    'y' : 'Guess Count'
                })
    michaelSAV_guesschart.update_traces(hovertemplate=None)
    michaelSAV_guesschart.update_layout(hovermode="y")
    st.plotly_chart(michaelSAV_guesschart)





    ### kell's info
    st.header('Killa Kells')
    st.write('Total Games Played:', kell_totalgamesplayed, 'Games Won:', kell_winnum, 'Games Lost:',
             kell_lossnum, 'Games Missed:', kell_missing_tot)
    st.write('Win Percent:', kell_winpercent)
    st.write('Average Guess Score:', kell_avg)
    with st.expander('Missing Game Numbers'):
        st.write(kell_missing)

    #guess chart
    kell_guesschart = px.bar(x = kell_guesscount, y = guess_range, orientation = 'h', labels = {
                    'x' : 'Number of Games',
                    'y' : 'Guess Count'
                })
    kell_guesschart.update_traces(hovertemplate=None)
    kell_guesschart.update_layout(hovermode="y")
    st.plotly_chart(kell_guesschart)


    ###nick' info
    st.header('Nick Cosby')
    st.write('Total Games Played:', nick_totalgamesplayed, 'Games Won:', nick_winnum, 'Games Lost:', nick_lossnum, 'Games Missed:', nick_missing_tot)
    st.write('Win Percent:', nick_winpercent)
    st.write('Average Guess Score:', nick_avg)
    with st.expander('Missing Game Numbers'):
        st.write(nick_missing)


    #guess chart
    nick_guesschart = px.bar(x = nick_guesscount, y = guess_range, orientation = 'h', labels = {
                    'x' : 'Number of Games',
                    'y' : 'Guess Count'
                })
    nick_guesschart.update_traces(hovertemplate=None)
    nick_guesschart.update_layout(hovermode="y")
    st.plotly_chart(nick_guesschart)



    ### jose's info
    st.header('HOEsay')
    st.write('Total Games Played:', jose_totalgamesplayed, 'Games Won:', jose_winnum, 'Games Lost:', jose_lossnum, 'Games Missed:', jose_missing_tot)
    st.write('Win Percent:', jose_winpercent)
    st.write('Average Guess Score:', jose_avg)
    with st.expander('Missing Game Numbers'):
        st.write(jose_missing)

    # guess chart
    jose_guesschart = px.bar(x = jose_guesscount, y = guess_range, orientation = 'h', labels = {
                    'x' : 'Number of Games',
                    'y' : 'Guess Count'
                })
    jose_guesschart.update_traces(hovertemplate=None)
    jose_guesschart.update_layout(hovermode="y")
    st.plotly_chart(jose_guesschart)