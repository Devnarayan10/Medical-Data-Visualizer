import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
#Reading data from the csv file
df = pd.read_csv(r"D:\Code\freecodecamp\Medical\medical_examination.csv")

# 2
#Creating an overweight column (Divide weight in kg by square of height in metre, hence divided by 100) checking greater than 25 as per the task given
df['overweight'] = ((df['weight'])/(df['height']/100)**2) > 25

# 3
#Normalizing values as per given task
#Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1
to_assign = {1:0,2:1,3:1}
df['cholesterol'] = df['cholesterol'].map(to_assign)
df['gluc'] = df['gluc'].map(to_assign)

# 4
def draw_cat_plot():
    # 5
    #Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df,id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])


    # 6
    df_cat['total'] = 1
    df_cat = df_cat.groupby(["cardio","variable","value"],as_index=False).count()
    

    # 7
    graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
    fig = graph.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
      (df['ap_lo'] <= df['ap_hi'])
      & (df['height'] >= df['height'].quantile(0.025))
      & (df['height'] <= df['height'].quantile(0.975))
      & (df['weight'] >= df['weight'].quantile(0.025))
      & (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(16, 9))

    # 15
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")

    # 16
    fig.savefig('heatmap.png')
    return fig
