"""
# Summer Olympics Data Analysis Assignment
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/Aneeshcoder/ETG_Intern_Olympics/main/summer.csv")

df.head(6)

"""### 1. In how many cities Summer Olympics is held so far?"""

#Unique Cities in the dataset
d1 = df['City'].unique()
d1

#type of the d1 array
type(d1)

#Total number of cities where Summer Olympics held
len(d1)

"""###Total number of cities where Summer Olympics held were 22.

### 2. Which sport is having most number of Gold Medals so far? (Top 5)
"""

#Creating a smaller dataframe
d21 = df['Sport']
d22 = df['Medal']
d20 = pd.concat([d21, d22], axis=1)
d20.head(5)

#Creating a sorted dataframe for number of gold
d2 = []

for sport in d20['Sport'].unique():
    d2.append([sport , len(d20[(d20['Medal']  == 'Gold') & (d20['Sport'] == sport)])])

d2 = pd.DataFrame(d2,columns = ['sport','gold'])
d2 = d2.sort_values(by = ['gold'], ascending = False)
d2.head(5)

#Plotting the graph
d2.plot(x = 'sport',y = 'gold',kind = 'bar',figsize = (20,30))

"""###Sports having most number of Gold medals:
1. Aquatics (1421 gold)
2. Athletics (1215 gold)
3. Rowing (890 gold)
4. Gymnastics (820 gold)
5. Fencing (552 gold)

### 3. Which sport is having most number of medals so far? (Top 5)
"""

#Creating a smaller dataframe
d30 = df['Sport']
d30.head(5)

#Creating a sorted dataframe as number of occurence is equal to number of medals
d3 = []

for sport in d30.unique():
    d3.append([sport , len(d30[d30 == sport])])

d3 = pd.DataFrame(d3,columns = ['sport','medal'])
d3 = d3.sort_values(by = ['medal'], ascending = False)
d3.head(5)

#Plotting the graph
d3.plot(x = 'sport',y = 'medal',kind = 'bar',figsize = (20,30))

"""###Sports having most number of medals:
1. Aquatics (4170 medals)
2. Athletics (3638 medals)
3. Rowing (2667 medals)
4. Gymnastics (2307 medals)
5. Fencing (1613 medals)

### 4. Which player has won most number of medals? (Top 5)
"""

#Creating a smaller dataframe
d40 = df['Athlete']
d40.head(5)

#Creating a sorted dataframe as every occurance represents a medal
d4 = []

for player in d40.unique():
    d4.append([player , len(d40[d40 == player])])

d4 = pd.DataFrame(d4,columns = ['Player','medal'])
d4 = d4.sort_values(by = ['medal'], ascending = False)
d4.head(5)

#Plotting the graph for top 10 players
d4.head(10).plot(x = 'Player',y = 'medal',kind = 'bar')

"""###Players with most number of medals:
1. PHELPS, Michael (22 medals)
2. LATYNINA, Larisa	(18 medals)
3. ANDRIANOV, Nikolay	(15 medals)
4. ONO, Takashi	(13 medals)
5. MANGIAROTTI, Edoardo	(13 medals)

### 5. Which player has won most number Gold Medals of medals? (Top 5)
"""

#Creating a smaller dataframe
d51 = df['Athlete']
d52 = df['Medal']
d50 = pd.concat([d51, d52], axis=1)
d50.head(5)

#Creating a sorted dataframe as number of occurence is equal to number of medals
d5 = []

for player in d50['Athlete'].unique():
    d5.append([player , len(d50[(d50['Athlete'] == player) & (d50['Medal'] == 'Gold')])])

d5 = pd.DataFrame(d5,columns = ['Player','gold'])
d5 = d5.sort_values(by = ['gold'], ascending = False)
d5.head(5)

#Plotting the graph for top 10 players
d5.head(10).plot(x = 'Player',y = 'gold',kind = 'bar')

"""### Players with most number of gold medals:
1. PHELPS, Michael (18 gold)
2. LEWIS, Carl (9 gold)
3. SPITZ, Mark (9 gold)
4. NURMI, Paavo (9 gold)
5. LATYNINA, Larisa (9 gold)

### 6. In which year India won first Gold Medal in Summer Olympics?
"""

#Defining a small dataframe for question
d61 = df['Year']
d62 = df['Country']
d63 = df['Medal']
d60 = pd.concat([d61, d62, d63], axis=1)
d60.head(5)

#Defining small dataframe continues 
d60 = d60[(d60['Country']=='IND') & (d60['Medal']=='Gold')]
d60.head(5)

#Deleting extra columns
del d60['Country']
del d60['Medal']
d60.head(5)

#Creating a small dataframe for number of golds by IND
d6 = []

for year in d60['Year'].unique():
    d6.append([year , len(d60[d60['Year'] == year])])

d6 = pd.DataFrame(d6,columns = ['Year','gold'])
d6 = d6.sort_values(by = ['Year'], ascending = True)
d6.head(5)

#Plotting the graph for year vs number of golds
d6.plot(x = 'Year',y = 'gold',kind = 'bar')

"""###India won the first gold medal in 1928

### 7. Which event is most popular in terms on number of players? (Top 5)
"""

#Creating a smaller dataframe
d71 = df['Event']
d72 = df['Athlete']
d70 = pd.concat([d71, d72], axis=1)
d70.head(5)

#dropping duplicate values according to name of the Athlete
d70 = d70.drop_duplicates(subset = 'Athlete')

#Creating a sorted dataframe as number of occurence is equal to number of Athlete
d7 = []

for event in d70['Event'].unique():
    d7.append([event , len(d70[d70['Event'] == event])])

d7 = pd.DataFrame(d7,columns = ['Event','Athlete'])
d7 = d7.sort_values(by = ['Athlete'], ascending = False)
d7.head(5)

#Checking whether Athletes are distict or not
len(df['Athlete'].unique()) == sum(d7['Athlete'])

#Plotting the graph for top 10 Events
d7.head(10).plot(x = 'Event',y = 'Athlete',kind = 'bar',)

"""### Most popular event in terms of number of players:
1. Football (1353 players)
2. Hockey	(1152 players)
3. Basketball	(814 players)
4. Handball	(788 players)
5. Team Competition	(780 players)

### 8. Which sport is having most female Gold Medalists? (Top 5)
"""

#Creating a smaller dataframe
d81 = df['Sport']
d82 = df['Gender']
d83 = df['Medal']
d80 = pd.concat([d81, d82, d83], axis=1)
d80.head(5)

#Creating a sorted dataframe according to number of female participation
d8 = []

for sport in d80['Sport'].unique():
    d8.append([sport , len(d80[(d80['Sport'] == sport) & (d80['Gender'] == 'Women') & (d80['Medal'] == 'Gold')])])

d8 = pd.DataFrame(d8,columns = ['Sport','Num_Women'])
d8 = d8.sort_values(by = ['Num_Women'], ascending = False)
d8.head(5)

#Plotting the graph for top 10 sports
d8.plot(x = 'Sport',y = 'Num_Women',kind = 'bar',figsize = (20,30))

"""###Sport with most female gold medalists:
1. Aquatics (589 female gold medalists)
2. Athletics (389 female gold medalists)
3. Gymnastics (268 female gold medalists)
4. Rowing (217 female gold medalists)
5. Volleyball (166 female gold medalists)
"""
