import package.charts as charts
import pandas as pd

def run():
    df = pd.read_csv('..//owner_modules/data.csv') # df = dataframe
    df = df[df['Continent'] == 'Africa']

    countries = df['Country/Territory'].values
    percentage = df['World Population Percentage'].values

    charts.generate_pie_chart(countries, percentage)

if __name__ == '__main__':
    run()