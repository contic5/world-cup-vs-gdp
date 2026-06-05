import pandas as pd

def main():
    df=pd.read_excel("country-gdp-data/country-gdp-data.xlsx")
    # Convert year columns to a single 'Year' column
    year_columns=[str(i) for i in range(1960,2025)]

    '''
    df_long = pd.melt(
        df, 
        id_vars=year_columns, 
        var_name='Year', 
        value_name='GDP'
    )
    '''

    df_long=pd.melt(
        df,
        id_vars=["Country Name","Country Code","Indicator Name","Indicator Code"],
        var_name='Year',
        value_name='GDP'
    )
    print(df_long.head())
    df_long.to_excel("country-gdp-by-year.xlsx")

if __name__=="__main__":
    main()