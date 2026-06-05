import pandas as pd
from collections import defaultdict
def blank():
    return 0

def calculate_more_expensive_winner(row):
    if row["Home_GDP"]==row["Away_GDP"] or row["home_score"]==row["away_score"]:
        return 0
    elif row["Home_GDP"]>row["Away_GDP"]:
        if row["home_score"]>row["away_score"]:
            return 1
        else:
            return -1
    elif row["Home_GDP"]<row["Away_GDP"]:
        if row["home_score"]<row["away_score"]:
            return 1
        else:
            return -1
    return 0
        
def main():
    gdp_df=pd.read_excel("country-gdp-by-year.xlsx")
    world_cup_df=pd.read_excel("world-cup-results.xlsx")
    world_cup_df["year"]=world_cup_df["date"].dt.year

    gdp_dict=defaultdict(blank)
    for index,row in gdp_df.iterrows():
        dictionary_key=f"{row['Country Name']}-{row['Year']}"
        gdp_dict[dictionary_key]=row["GDP"]
    print(gdp_df["Year"].describe())
    print(gdp_dict)

    world_cup_df["Home_GDP"]=-1
    world_cup_df["Away_GDP"]=-1
    for index,row in world_cup_df.iterrows():
        home_key=f"{row['home_team']}-{row['year']}"
        world_cup_df.at[index,"Home_GDP"]=gdp_dict[home_key]
        away_key=f"{row['away_team']}-{row['year']}"
        world_cup_df.at[index,"Away_GDP"]=gdp_dict[away_key]

        #print(f"{home_key} {home_key in world_cup_df} | {away_key} {away_key in world_cup_df}")
    

    print(world_cup_df["Home_GDP"].describe())
    world_cup_df=world_cup_df[world_cup_df["Home_GDP"]!=-1]
    world_cup_df=world_cup_df[world_cup_df["Away_GDP"]!=-1]
    world_cup_df=world_cup_df[world_cup_df["Home_GDP"]!=0]
    world_cup_df=world_cup_df[world_cup_df["Away_GDP"]!=0]
    world_cup_df=world_cup_df[world_cup_df["Home_GDP"].notna()]
    world_cup_df=world_cup_df[world_cup_df["Away_GDP"].notna()]

    world_cup_df["Wealthier_Winner"]=world_cup_df.apply(calculate_more_expensive_winner,axis=1)
    print(world_cup_df["Wealthier_Winner"].describe())
    print(world_cup_df.head())
    world_cup_df.to_excel("world-cup-results-gdp.xlsx")

if __name__=="__main__":
    main()