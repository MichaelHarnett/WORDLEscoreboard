###############
### imports ###
###############


import numpy as np
import pandas as pd
import requests
import os



import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, inspect


####################################################################
########################## FAMILY SECTION ##########################
####################################################################

###########################
### pulling fresh texts ###
###########################


engine = db.create_engine('sqlite:////Users/michaelharnett/Library/Messages/chat.db')
connection = engine.connect()
metadata = db.MetaData()

orig_df = pd.read_sql("select distinct m.rowid ,m.is_from_me IsFromMe ,case when m.is_from_me = 1 then m.account else h.id end as FromPhoneNumber ,datetime((m.date / 1000000000) + 978307200, 'unixepoch', 'localtime') as TextDate, m.text MessageText,c.display_name RoomName from message as m left join handle as h on m.handle_id = h.rowid left join chat as c on m.cache_roomnames = c.room_name left join chat_handle_join as ch on c.rowid = ch.chat_id left join handle as h2 on ch.handle_id = h2.rowid where RoomName LIKE 'Wordle Fam%' order by m.date desc;", engine)






#############################
### making correct tables ###
#############################


df = orig_df[['FromPhoneNumber','TextDate','MessageText']] # taking only the fields I need
df = df.rename(columns = {'FromPhoneNumber':'player', 'TextDate':'date', 'MessageText':'message'}) #fixing names


# Renaming changing the Id from phone number to our names
df.loc[df.player == '+12014523662', 'player'] = 'Danielle'
df.loc[df.player == '+12017253072', 'player'] = 'Dad'
df.loc[df.player == '+15514868670', 'player'] = 'Chris'
df.loc[df.player == 'E:michaelcharnett@gmail.com', 'player'] = 'Michael'


# Creating columns
df['wordle_check'] = ''
df['game_num'] = ''
df['score'] = ''

# fixing indexes
df = df.dropna()
df = df.reset_index()
df =df.drop(columns = ['index'])

#updating values
for i in range(1,len(df)):
    df.loc[i,'wordle_check'] = df.loc[i,'message'][:6]
    df.loc[i,'game_num'] = df.loc[i,'message'][7:10]
    df.loc[i,'score'] = df.loc[i,'message'][11:14]
    

    
# creating wordledf, df of just wordle messages
wordledf = df    
wordledf = df[df.wordle_check == 'Wordle']
wordledf = wordledf.drop(columns = ['message','wordle_check'])



# changing scores to remove the denominator, a they're all out of 6
wordledf = wordledf.reset_index()
wordledf = wordledf.drop(columns = ['index'])   ##for some reason, it works if I keep resetting index

for i in range(len(wordledf)):
    wordledf.loc[i, 'score'] = wordledf.loc[i, 'score'][0]




#######################
### cleaneingtables ###
#######################


## for some reason was erroring..not needed these columns were dropped elsewhere
# # removing unneeded columns
# wordledf = wordledf.drop(columns = ['message', 'date'])
# wordledf = wordledf.drop(columns = ['wordle_check'])

# changing data types
wordledf.player = wordledf.player.astype('str')
wordledf.game_num = wordledf.game_num.astype('int')
wordledf.score = wordledf.score.astype('str')




# setting wins/loss in new column    -----------------MAY BE UNNECCESRY 
wordledf[wordledf.score == 'x']
wordledf[wordledf.score == 'X']    #there seems to be case inconsistencies 

wordledf.loc[wordledf.score == 'x','LOSS'] = 1
wordledf.loc[wordledf.score != 'x','LOSS'] = 0

wordledf.loc[wordledf.score == 'X','LOSS'] = 1
wordledf.loc[wordledf.score != 'X','LOSS'] = 0




# individualized tables
michaeldf = wordledf[wordledf.player == 'Michael']
danielledf = wordledf[wordledf.player == 'Danielle']
chrisdf = wordledf[wordledf.player == 'Chris']
daddf = wordledf[wordledf.player == 'Dad']


# ordering the tables
michaeldf = michaeldf.sort_values(by='game_num', ascending = False)
danielledf = danielledf.sort_values(by='game_num', ascending = False)
chrisdf = chrisdf.sort_values(by='game_num', ascending = False)
daddf = daddf.sort_values(by='game_num', ascending = False)

# making a df of just wins to compare against
michaelwindf = michaeldf[michaeldf['score'].astype(str).str.isnumeric()]
dadwindf = daddf[daddf['score'].astype(str).str.isnumeric()]
daniellewindf = danielledf[danielledf['score'].astype(str).str.isnumeric()]
chriswindf = chrisdf[chrisdf['score'].astype(str).str.isnumeric()]



#######################################################################################
########    REALIZING, tables should be made and exprted. thsi can be dane after ######
########################################################################################
#### Win percentages 
#### michael_winpercent = (len(michaelwindf)/len(michaeldf)*100)
#### dad_winpercent = (len(dadwindf)/len(daddf)*100)
#### danielle_winpercent = (len(daniellewindf)/len(danielledf)*100)
#### chris_winpercent = (len(chriswindf)/len(chrisdf)*100)


##############################
#### saving dfs to folder ####
##############################

# michael
michaeldf.to_csv('tables/michaeldf.csv', index = False)
michaelwindf.to_csv('tables/michaelwindf.csv', index = False)

# danielle
danielledf.to_csv('tables/danielledf.csv', index = False)
daniellewindf.to_csv('tables/daniellewindf.csv', index = False)

#chris
chrisdf.to_csv('tables/chrisdf.csv', index = False)
chriswindf.to_csv('tables/chriswindf.csv', index = False)

#dad
daddf.to_csv('tables/daddf.csv', index = False)
dadwindf.to_csv('tables/dadwindf.csv', index = False)

#wordledf
wordledf.to_csv('tables/wordledf.csv', index = False)





#####################################################################
########################## SAVAGES SECTION ##########################
#####################################################################


###########################
### pulling fresh texts ###
###########################

savagesdf = pd.read_sql("select distinct m.rowid ,m.is_from_me IsFromMe ,case when m.is_from_me = 1 then m.account else h.id end as FromPhoneNumber ,datetime((m.date / 1000000000) + 978307200, 'unixepoch', 'localtime') as TextDate, m.text MessageText,c.display_name RoomName from message as m left join handle as h on m.handle_id = h.rowid left join chat as c on m.cache_roomnames = c.room_name left join chat_handle_join as ch on c.rowid = ch.chat_id left join handle as h2 on ch.handle_id = h2.rowid where RoomName LIKE 'Savages%' order by m.date desc;", engine)



#############################
### making correct tables ###
#############################


savagesdf = savagesdf[['FromPhoneNumber','TextDate','MessageText']] # taking only the fields I need
savagesdf = savagesdf.rename(columns = {'FromPhoneNumber':'player', 'TextDate':'date', 'MessageText':'message'}) #fixing names



# Renaming changing the Id from phone number to our names
savagesdf.loc[savagesdf.player == '+12017248296', 'player'] = 'kell'
savagesdf.loc[savagesdf.player == '+12017447544', 'player'] = 'd'
savagesdf.loc[savagesdf.player == '+18456083263', 'player'] = 'drie'
savagesdf.loc[savagesdf.player == '+12017554735', 'player'] = 'jose'
savagesdf.loc[savagesdf.player == '+12012706619', 'player'] = 'nick'
savagesdf.loc[savagesdf.player == 'E:michaelcharnett@gmail.com', 'player'] = 'michael'
savagesdf.loc[savagesdf.player == 'e:michaelcharnett@gmail.com', 'player'] = 'michael'



# Creating columns
savagesdf['wordle_check'] = ''
savagesdf['game_num'] = ''
savagesdf['score'] = ''

# fixing indexes
savagesdf = savagesdf.dropna()
savagesdf = savagesdf.reset_index()
savagesdf =savagesdf.drop(columns = ['index'])

#updating values
for i in range(1,len(savagesdf)):
    savagesdf.loc[i,'wordle_check'] = savagesdf.loc[i,'message'][:6]
    savagesdf.loc[i,'game_num'] = savagesdf.loc[i,'message'][7:10]
    savagesdf.loc[i,'score'] = savagesdf.loc[i,'message'][11:14]
    


# creating wordledf, df of just wordle messages
savages_wordledf = savagesdf[savagesdf.wordle_check == 'Wordle']
savages_wordledf = savages_wordledf.drop(columns = ['message','wordle_check'])



# changing scores to remove the denominator, a they're all out of 6
savages_wordledf = savages_wordledf.reset_index()
savages_wordledf = savages_wordledf.drop(columns = ['index'])   ##for some reason, it works if I keep resetting index

# there was a blank space in nick's first entry, he must have started a text with 'wordle' ON 2/7
savages_wordledf = savages_wordledf[savages_wordledf.game_num != '']


for i in range(len(savages_wordledf)):
    savages_wordledf.loc[i, 'score'] = savages_wordledf.loc[i, 'score'][0]



#######################
### cleaneingtables ###
#######################


# changing data types
savages_wordledf.player = savages_wordledf.player.astype('str')
savages_wordledf.game_num = savages_wordledf.game_num.astype('int')
savages_wordledf.score = savages_wordledf.score.astype('str')


#individualized tables
michaelSAVdf = savages_wordledf[savages_wordledf.player == 'michael']
kelldf = savages_wordledf[savages_wordledf.player == 'kell']
#ddf = savages_wordledf[savages_wordledf.player == 'd'] # realized not playing
#driedf = savages_wordledf[savages_wordledf.player == 'drie'] # realized not playing 
nickdf = savages_wordledf[savages_wordledf.player == 'nick']
josedf = savages_wordledf[savages_wordledf.player == 'jose']


# ordering the tables
michaelSAVdf = michaelSAVdf.sort_values(by='game_num', ascending = False)
kelldf = kelldf.sort_values(by='game_num', ascending = False)
#ddf = ddf.sort_values(by='game_num', ascending = False)    #not playing
#driedf = driedf.sort_values(by='game_num', ascending = False)    #not playing
josedf = josedf.sort_values(by='game_num', ascending = False)
# nick sent a copule of cheat texts, all before 3/8 so tailoring his to look only after that
nickdf = nickdf.sort_values(by='game_num', ascending = False)
nickdf = nickdf[nickdf.date > '2022-03-09']


# making a df of just wins to compare against
michaelSAVwindf = michaelSAVdf[michaelSAVdf['score'].astype(str).str.isnumeric()]
kellwindf = kelldf[kelldf['score'].astype(str).str.isnumeric()]
josewindf = josedf[josedf['score'].astype(str).str.isnumeric()]
nickwindf = nickdf[nickdf['score'].astype(str).str.isnumeric()]


##############################
#### saving dfs to folder ####
##############################

# michael - savages version
michaelSAVdf.to_csv('tables/michaelSAVdf.csv', index = False)
michaelSAVwindf.to_csv('tables/michaelSAVwindf.csv', index = False)

#Kell
kelldf.to_csv('tables/kelldf.csv', index = False)
kellwindf.to_csv('tables/kellwindf.csv', index = False)

#Nick
nickdf.to_csv('tables/nickdf.csv', index = False)
nickwindf.to_csv('tables/nickwindf.csv', index = False)

#Jose
josedf.to_csv('tables/josedf.csv', index = False)
josewindf.to_csv('tables/josewindf.csv', index = False)