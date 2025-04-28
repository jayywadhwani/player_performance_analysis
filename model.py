import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns 
import re
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
import io
import base64

def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close(fig)
    return img_base64
    
df_odi = pd.read_csv("static/virat_kohli_odi_innings_data.csv")
df_t20 = pd.read_csv("static/virat_kohli_t20i_innings_data.csv")
df_test = pd.read_csv("static/virat_kohli_test_innings_data.csv")

#Dropping unecessary rows and columns

df_odi.drop(columns=["Odi No"],inplace=True)
df_t20.drop(columns=["T20I No"],inplace=True)
df_test.drop(columns=["Test No"],inplace=True)

df_odi = df_odi[df_odi['SR'] != "-"]
df_t20 = df_t20[df_t20['SR'] != "-"]
df_test = df_test[df_test['SR'] != "-"]

# Data Formatting 

# Date Formatting
splited_text = []
for i in df_odi.Date:
    splited_text.append(i[6:])
df_odi.Date = splited_text

splited_text = []
for i in df_test.Date:
    splited_text.append(i[6:])    
df_test.Date = splited_text
    
splited_text = []
for i in df_t20.Date:
    splited_text.append(i[6:])    
df_t20.Date = splited_text

# Type Formatting
df_odi.SR = df_odi["SR"].astype(float)
df_t20.SR = df_t20["SR"].astype(float)
df_test.SR = df_test["SR"].astype(float)
df_odi.BF = df_odi["BF"].astype(int)
df_t20.BF = df_t20["BF"].astype(int)
df_test.BF = df_test["BF"].astype(int)
df_odi.Inns = df_odi["Inns"].astype(int)
df_t20.Inns = df_t20["Inns"].astype(int)
df_test.Inns = df_test["Inns"].astype(int)

#Runs Formatting
splited_text = []
for i in df_odi.Runs:
    run = re.search(r"\d+", i)
    if run:
        number = int(run.group())
        splited_text.append(number)
df_odi.Runs = splited_text

splited_text = []
for i in df_t20.Runs:
    run = re.search(r"\d+", i)
    if run:
        number = int(run.group())
        splited_text.append(number)
df_t20.Runs = splited_text

splited_text = []
for i in df_test.Runs:
    run = re.search(r"\d+", i)
    if run:
        number = int(run.group())
        splited_text.append(number)
df_test.Runs = splited_text

#team name formatting
splited_text = []
for i in df_odi.Opposition:
    splited_text.append(i.lower())
df_odi.Opposition = splited_text

splited_text = []
for i in df_t20.Opposition:
    splited_text.append(i.lower())
df_t20.Opposition = splited_text

splited_text = []
for i in df_test.Opposition:
    splited_text.append(i.lower())
df_test.Opposition = splited_text

def player_performance_analysis_total():
    #Analysis Charts 
    test_performance = plt.figure(figsize=(10,5),facecolor='black') 
    ax = test_performance.add_subplot(111)  # Create axis (plot area)
    ax.set_facecolor('black') 
    ax.set_xlabel('Date', color='white', fontsize=14)
    ax.set_ylabel('Runs', color='white', fontsize=14)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.plot(df_test.Date.unique(), df_test.groupby(["Date"])["Runs"].sum())
    fig_test = fig_to_base64(test_performance)
    plt.close(test_performance)

    odi_performance = plt.figure(figsize=(10,5),facecolor='black')
    ax = odi_performance.add_subplot(111)  # Create axis (plot area)
    ax.set_facecolor('black') 
    ax.set_xlabel('Date', color='white', fontsize=14)
    ax.set_ylabel('Runs', color='white', fontsize=14)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.plot(df_odi.Date.unique(), df_odi.groupby(["Date"])["Runs"].sum())
    fig_odi = fig_to_base64(odi_performance)
    plt.close(odi_performance)
        
    t20_performance = plt.figure(figsize=(10,5),facecolor='black')
    ax = t20_performance.add_subplot(111)  # Create axis (plot area)
    ax.set_facecolor('black') 
    ax.set_xlabel('Date', color='white', fontsize=14)
    ax.set_ylabel('Runs', color='white', fontsize=14)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.plot(df_t20.Date.unique(), df_t20.groupby(["Date"])["Runs"].sum())
    fig_t20 = fig_to_base64(t20_performance)
    plt.close(t20_performance)

    #runs Scored Against different oppositions 
    test_opposition_performance = plt.figure(figsize=(10,8),facecolor='black')
    plt.pie(df_test.groupby(["Opposition"])["Runs"].sum(), labels=df_test.Opposition.unique(), autopct='%1.1f%%',startangle=140,textprops={'color': 'white'})
    plt.title("Runs Scored Against Each Opposition")
    plt.axis("equal")  
    fig_test_pie = fig_to_base64(test_opposition_performance)
    plt.close(test_opposition_performance)
    # print(dict(df_test.Opposition.value_counts()))
    odi_opposition_performance = plt.figure(figsize=(10,8),facecolor='black')
    plt.pie(df_odi.groupby(["Opposition"])["Runs"].sum(), labels=df_odi.Opposition.unique(), autopct='%1.1f%%', startangle=140, textprops={'color': 'white'})
    plt.title("Runs Scored Against Each Opposition")
    plt.axis("equal") 
    fig_odi_pie= fig_to_base64(odi_opposition_performance)
    plt.close(odi_opposition_performance)
    # print(dict(df_odi.Opposition.value_counts()))

    t20_opposition_performance = plt.figure(figsize=(10,8),facecolor='black')
    plt.pie(df_t20.groupby(["Opposition"])["Runs"].sum(), labels=df_t20.Opposition.unique(), autopct='%1.1f%%', startangle=140,textprops={'color': 'white'})
    plt.title("Runs Scored Against Each Opposition")
    plt.axis("equal")
    fig_t20_pie = fig_to_base64(t20_opposition_performance)
    plt.close(t20_opposition_performance)
    # print(dict(df_t20.Opposition.value_counts()))

    return(#Average runs 
    float(round(df_test.Runs.sum()/df_test.Runs.count(),2)),
    float(round(df_odi.Runs.sum()/df_odi.Runs.count(),2)),
    float(round(df_t20.Runs.sum()/df_t20.Runs.count(),2)),
    #Average Strike Rate
    float(round(df_test.SR.sum()/df_test.SR.count(),2)),
    float(round(df_odi.SR.sum()/df_odi.SR.count(),2)),
    float(round(df_t20.SR.sum()/df_t20.SR.count(),2)),
    #last three years
    list(df_test.groupby(["Date"])["Runs"].sum()[-3:]),
    list(df_odi.groupby(["Date"])["Runs"].sum()[-3:]),
    list(df_t20.groupby(["Date"])["Runs"].sum()[-3:]),
    #Analysis Charts
    fig_test,
    fig_odi,
    fig_t20,
    fig_test_pie,
    fig_odi_pie,
    fig_t20_pie
    )

def player_performance_analysis_teamwise(match_opposition_arg=""):
    #team wise analysis
    match_opposition = match_opposition_arg
    df_odi_copy = df_odi[df_odi["Opposition"]==match_opposition]
    df_test_copy = df_test[df_test["Opposition"]==match_opposition]
    df_t20_copy = df_t20[df_t20["Opposition"]==match_opposition]

    teamwise_test_preformance = plt.figure(figsize=(10,5),facecolor='black')
    ax = teamwise_test_preformance.add_subplot(111)  # Create axis (plot area)
    ax.set_facecolor('black') 
    ax.set_xlabel('Date', color='white', fontsize=14)
    ax.set_ylabel('Runs', color='white', fontsize=14)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.plot(df_test_copy.Date.unique(), df_test_copy.groupby(["Date"])["Runs"].sum())
    fig_test_teamwise = fig_to_base64(teamwise_test_preformance)
    plt.close(teamwise_test_preformance)

    teamwise_odi_preformance = plt.figure(figsize=(10,5),facecolor='black') 
    ax = teamwise_odi_preformance.add_subplot(111)  # Create axis (plot area)
    ax.set_facecolor('black') 
    ax.set_xlabel('Date', color='white', fontsize=14)
    ax.set_ylabel('Runs', color='white', fontsize=14)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.plot(df_odi_copy.Date.unique(), df_odi_copy.groupby(["Date"])["Runs"].sum())
    fig_odi_teamwise = fig_to_base64(teamwise_odi_preformance)
    plt.close(teamwise_odi_preformance)
        
    teamwise_t20_preformance = plt.figure(figsize=(10,5),facecolor='black')
    ax = teamwise_t20_preformance.add_subplot(111)  # Create axis (plot area)
    ax.set_facecolor('black') 
    ax.set_xlabel('Date', color='white', fontsize=14)
    ax.set_ylabel('Runs', color='white', fontsize=14)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.plot(df_t20_copy.Date.unique(), df_t20_copy.groupby(["Date"])["Runs"].sum())
    fig_t20_teamwise = fig_to_base64(teamwise_t20_preformance)
    plt.close(teamwise_t20_preformance)

    return(
        fig_test_teamwise,
        fig_odi_teamwise,
        fig_t20_teamwise
    )

def player_performance_analysis_prediction(match_format_func="odi",ball_faced=0,strike_rate=0,innings=0):
    # Model For Prediction 
    match_format = match_format_func

    if match_format == "odi":
        xtrain,xtest,ytrain,ytest = train_test_split(df_odi[["BF","SR","Inns"]],df_odi["Runs"],test_size=0.3,
                                                 random_state=42,shuffle=False)    
        model= LinearRegression()
        model.fit(xtrain,ytrain)
        ypred = model.predict(np.array([ball_faced,strike_rate,innings]).reshape(1,-1))
        xpred = model.predict(xtest)
        mse = mean_squared_error(xpred,ytest)
        r2 = r2_score(xpred,ytest)
        mae = mean_absolute_error(xpred,ytest)
        return (round(ypred[0],2),round(mse,2),round(r2,2),round(mae,2))
    elif match_format== "t20":
        xtrain,xtest,ytrain,ytest = train_test_split(df_t20[["BF","SR","Inns"]],df_t20["Runs"],test_size=0.3,
                                                    random_state=42,shuffle=False)
        model= LinearRegression()
        model.fit(xtrain,ytrain)
        ypred = model.predict(np.array([ball_faced,strike_rate,innings]).reshape(1,-1))
        xpred = model.predict(xtest)
        mse = mean_squared_error(xpred,ytest)
        r2 = r2_score(xpred,ytest)
        mae = mean_absolute_error(xpred,ytest)
        return (round(ypred[0],2),round(mse,2),round(r2,2),round(mae,2))
    elif match_format == "test":
        xtrain,xtest,ytrain,ytest = train_test_split(df_test[["BF","SR","Inns"]],df_test["Runs"],test_size=0.3,
                                                    random_state=42,shuffle=False)
        model= LinearRegression()
        model.fit(xtrain,ytrain)
        ypred = model.predict(np.array([ball_faced,strike_rate,innings]).reshape(1,-1))
        xpred = model.predict(xtest)
        mse = mean_squared_error(xpred,ytest)
        r2 = r2_score(xpred,ytest)
        mae = mean_absolute_error(xpred,ytest)
        return (round(ypred[0],2),round(mse,2),round(r2,2),round(mae,2))

