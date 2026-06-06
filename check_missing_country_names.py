import pandas as pd

def main():
    gdp_df=pd.read_excel("data/country-gdp-by-year.xlsx")
    world_cup_df=pd.read_excel("data/world-cup-results.xlsx")

    # Check condition (Returns True/False mask)
    mask = ~world_cup_df['home_team'].isin(gdp_df['Country Name'])

    # Filter df1 to get the unique rows
    unique_rows = world_cup_df[mask]
    print(unique_rows["home_team"].unique())

if __name__=="__main__":
    main()