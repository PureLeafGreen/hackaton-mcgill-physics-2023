import pandas as pd
import plotly.express as px
per_game = pd.read_html('https://www.basketball-reference.com/players/s/siakapa01.html')[0]
draft_class = pd.read_html('https://www.basketball-reference.com/draft/NBA_2016.html')[0]

draft_class = draft_class.fillna(0)
draft_class = draft_class.drop([30, 31]).reset_index(drop=True)
draft_class.columns = draft_class.columns.droplevel()
draft_class.columns = ['Rk', 'Pk', 'Tm','Player','Pos','Yrs','G','MP','PTS','TRB','AST','FG%','3P','FT%','MPPG','PTSPG','TRBPG','ASTPG','WS','WS/48','BPM','VORP']
# # Remove everyone from the draft all players who aren't Pascal Siakam
draft_class = draft_class.get(draft_class['Player'] == 'Pascal Siakam')

YearsPlayedByPascal = draft_class['Yrs'].values[0]

print(per_game)

print()

print(draft_class)

print()

print(YearsPlayedByPascal)

for column in draft_class.columns:
    draft_class[column] = pd.to_numeric(draft_class[column], errors='ignore')
draft_class.dtypes

# draft_class['WORP'] = draft_class['VORP'] * 2.70

scatter_plot = px.scatter(per_game, x='MP', y='3P%', labels={'Year': 'Season'}, title='MP, 2P%, 3P% by Season')

scatter_plot.write_image("2016NBA_DraftClass_Points_vs_MinutesPlayed.png")