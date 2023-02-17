#!/usr/bin/env python
# coding: utf-8

# In[74]:


def catchers(name):
    url = 'https://rhloftis-mlb-data.s3.amazonaws.com/catchers.csv'
    import pandas as pd
    from mplsoccer import Radar, FontManager, grid
    import matplotlib.pyplot as plt
    df = pd.read_csv(url)
    URL1 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
            'SourceSerifPro-Regular.ttf')
    serif_regular = FontManager(URL1)
    URL2 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
            'SourceSerifPro-ExtraLight.ttf')
    serif_extra_light = FontManager(URL2)
    URL3 = ('https://raw.githubusercontent.com/google/fonts/main/ofl/rubikmonoone/'
            'RubikMonoOne-Regular.ttf')
    rubik_regular = FontManager(URL3)
    URL4 = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf'
    robotto_thin = FontManager(URL4)
    URL5 = ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
            'RobotoSlab%5Bwght%5D.ttf')
    robotto_bold = FontManager(URL5)
    try:
        for x in range(len(df['Name'])):
            if name in df['Name'][x]:
                player = df.loc[x]
        word = player
    except:
        return("Player did not have enough at bats in this season!")
    else:
        for x in range(len(df['Name'])):
            if name in df['Name'][x]:
                player = df.loc[x]
        player_name = player[0]
        #print(df)
        dfQ = pd.read_csv('https://rhloftis-mlb-data.s3.amazonaws.com/statcast-hitters-teams.csv')
        dfQ = dfQ[dfQ['PA'] >= 505]
        #print(player)
        values = [round(z,3) for z in player[3:]]
        #print(values)
        HitHigh = [round(x,3) for x in dfQ.quantile(0.95)[1:-3]]
        #print(HitHigh)
        DefHigh = [round(x,3) for x in df.quantile(0.95)[11:]]
        #print(DefHigh)
        high = HitHigh + DefHigh
        HitLow = [round(x,3) for x in dfQ.quantile(0.05)[1:-3]]
        DefLow = [round(x,3) for x in df.quantile(0.05)[11:]]
        low = HitLow + DefLow
        HitAvg = [round(x,3) for x in dfQ.quantile(0.5)[1:-3]]
        DefAvg = [round(x,3) for x in df.quantile(0.5)[11:]]
        averages = HitAvg + DefAvg
        params = [x for x in df.columns[3:]]
        for x in range(len(df['Name'])):
            if df['Name'].loc[x] == player_name:
                team = df['Team'].loc[x]
        radar = Radar(params, low, high, round_int=[False]*len(params),lower_is_better=['K%', 'Pop Time 2B'],
              num_rings=10, ring_width=1, center_circle_radius=1)
        fig, axs = grid(figheight=14, grid_height=0.915, title_height=0.06, endnote_height=0.025,
                title_space=0, endnote_space=0, grid_key='radar', axis=False)
        radar.setup_axis(ax=axs['radar'])
        rings_inner = radar.draw_circles(ax=axs['radar'], facecolor='gainsboro', edgecolor='lightgrey')
        if team == 'Tampa Bay Rays':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#092C5C'},kwargs_rings={'facecolor': '#8FBCE6'})
        elif team == 'Baltimore Orioles':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#DF4601'},kwargs_rings={'facecolor': '#000000'})
        elif team == 'Toronto Bluejays':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#134A8E'},kwargs_rings={'facecolor': 'lightskyblue'})
        elif team == 'Boston Redsox':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#BD3039'},kwargs_rings={'facecolor': '#0C2340'})
        elif team == 'New York Yankees':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': 'white', 'hatch' : '|', 'edgecolor' : '#0C2340'},kwargs_rings={'facecolor': '#0C2340', 'edgecolor' : '#0C2340'})
        elif team == 'New York Mets':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': 'white', 'hatch' : '|', 'edgecolor' : '#002D72'},kwargs_rings={'facecolor': '#FF5910', 'edgecolor':'#002D72'})
        elif team == 'Washington Nationals':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': 'white', 'edgecolor' : '#14225A'},kwargs_rings={'facecolor': '#AB0003'})
        elif team == 'Atlanta Braves':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#CE1141', 'edgecolor':'#002855'},kwargs_rings={'facecolor': '#002855'})
        elif team == 'Miami Marlins':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#00A3E0', 'edgecolor':'#000000'},kwargs_rings={'facecolor': '#EF3340'})
        elif team == 'Philadelphia Phillies':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#E81828', 'edgecolor' : '#E81828'},kwargs_rings={'facecolor': 'white', 'hatch':'|', 'edgecolor' : '#E81828'})
        elif team == 'Detroit Tigers':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#0C2340'},kwargs_rings={'facecolor': '#FA4616'})
        elif team == 'Minnesota Twins':
            radar_output = radar.draw_radar(values, ax=axs['radar'], kwargs_radar={'facecolor': '#002B5C'},kwargs_rings={'facecolor': '#D31145'})
        elif team == 'Chicago Whitesox':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': 'black'},kwargs_rings={'facecolor': 'white', 'hatch': '|', 'edgecolor' : 'black'})
        elif team == 'Kansas City Royals':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#004687', 'edgecolor':'#004687'},kwargs_rings={'facecolor': 'white'})
        elif team == 'Cleveland Guardians':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#00385D'},kwargs_rings={'facecolor': '#E50022'})
        elif team == 'Chicago Cubs':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#0E3386', 'edgecolor' : '#CC3433'},kwargs_rings={'facecolor': 'white', 'hatch':'|', 'edgecolor':'#0E3386'})
        elif team == 'St. Louis Cardinals':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#C41E3A', 'edgecolor':'#0C2340'},kwargs_rings={'facecolor': 'white'})
        elif team == 'Pittsburgh Pirates':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#27251F'},kwargs_rings={'facecolor': '#FDB827'})
        elif team == 'Cincinnati Reds':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#C6011F'},kwargs_rings={'facecolor': 'white'})
        elif team == 'Milwaukee Brewers':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#FFC52F'},kwargs_rings={'facecolor': '#12284B'})
        elif team == 'Los Angeles Angels':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': 'white', 'edgecolor' : '#BA0021'},kwargs_rings={'facecolor': '#BA0021', 'edgecolor': '#BA0021'})
        elif team == 'Texas Rangers':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#003278'},kwargs_rings={'facecolor': '#C0111F'})
        elif team == 'Houston Astros':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#002D62', 'edgecolor':'#002D62'},kwargs_rings={'facecolor': '#EB6E1F'})
        elif team == 'Seattle Mariners':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#0C2C56'},kwargs_rings={'facecolor': '#005c5c'})
        elif team == 'Oakland Athletics':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#003831', 'edgecolor':'#003831'},kwargs_rings={'facecolor': '#EFB21E'})
        elif team == 'Los Angeles Dodgers':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': 'white', 'edgecolor':'#005A9C'},kwargs_rings={'facecolor': '#005A9C'})
        elif team == 'San Francisco Giants':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#FD5A1E', 'edgecolor':'#27251F'},kwargs_rings={'facecolor': '#27251F'})
        elif team == 'San Diego Padres':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#473729', 'edgecolor':'#2F241D'},kwargs_rings={'facecolor': '#FFC425'})
        elif team == 'Arizona Diamonbacks':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#A71930', 'edgecolor':'black'},kwargs_rings={'facecolor': '#E3D4AD'})
        elif team == 'Colorado Rockies':
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': '#24135F', 'edgecolor':'#24135F'},kwargs_rings={'facecolor': 'white', 'hatch':'|', 'edgecolor':'black'})
        elif team == "Free Agent":
            radar_output = radar.draw_radar(values, ax=axs['radar'],kwargs_radar={'facecolor': 'lightgrey', 'edgecolor':'black'},kwargs_rings={'facecolor': 'darkgrey'})
        range_labels = radar.draw_range_labels(ax=axs['radar'], fontsize=15,
                                               fontproperties=robotto_bold.prop)
        param_labels = radar.draw_param_labels(ax=axs['radar'], fontsize=15,
                                               fontproperties=robotto_bold.prop)
        endnote_text = axs['endnote'].text(0.99, 0.5, 'Inspired By: StatsBomb / Rami Moghadam \n Data provided by BaseballSavant \n By Richard Loftis', fontsize=15,
                                           fontproperties=robotto_thin.prop, ha='right', va='center')
        title1_text = axs['title'].text(0.01, 0.65, player_name, fontsize=25,
                                        fontproperties=robotto_bold.prop, ha='left', va='center')
        title2_text = axs['title'].text(0.01, 0.25, team, fontsize=20,
                                        fontproperties=robotto_thin.prop,
                                       ha='left', va='center', color='black')
        title3_text = axs['title'].text(0.99, 0.65, 'Statcast Hitting Radar Chart', fontsize=25,
                                        fontproperties=robotto_bold.prop, ha='right', va='center')


# In[85]:


name = input('Enter a catcher: ')
catchers(name)


# In[ ]:




