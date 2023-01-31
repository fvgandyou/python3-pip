import utils

countries = [
  {
    'country': 'colombia',
    'population': 50
  },
  {
    'country': 'bolivia',
    'population': 30
  },
  {
    'country': 'brasil',
    'population': 120
  }
]
print(countries)
print('*' * 30)

def run():
  country_searched = input('Type country: ').lower()
  result = utils.population_country(countries, country_searched)
  print(result)

# Script of duality to execute the programm
if __name__ == '__main__':
  run() # Entry point