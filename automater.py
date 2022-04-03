###############
### imports ###
###############


import numpy as np
import pandas as pd
import requests
import os



import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, inspect


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
wordledf = wordledf.drop(columns = ['message','date','wordle_check'])



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