import csv
import matplotlib.pyplot as plt

def population_country(path, country):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)[5:13]
    # print(header)
    population_selected = {}
    for row in reader:
      if row[2] == country:
        country_data = row[5:13]
        selected = zip(header, country_data)
        population_selected = {key: value for key, value in selected}
    return population_selected

def global_percentage(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    total_percentage = {}
    for row in reader:
      if row[2] != 'Country/Territory' and row[4] == 'South America':
        country = row[2]
        country_percentage = float(row[-1])
        total_percentage.update({country: country_percentage})
    # print(total_percentage)
  return total_percentage
      
def generate_bar_chart(data, selected):
  labels = list(data.keys())
  # print(labels)
  values_str = list(data.values())
  values = [int(item) for item in values_str]
  # print(values)
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./img/bar-{selected}.png')
  plt.close()

def generate_pie_chart(data, selected):
  labels = list(data.keys())
  values = list(data.values())
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./img/pie-{selected}.png')
  plt.close()

if __name__ == '__main__':
  country = input('Type Country: ').capitalize()
  population_selected = population_country('./data.csv',
                                           country)
  # print(population_selected)
  generate_bar_chart(population_selected, country)

  total_percentage = global_percentage('./data.csv')
  generate_pie_chart(total_percentage, country)
