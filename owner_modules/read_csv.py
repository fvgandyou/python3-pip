import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # header creates to make a dictionary
    header = next(reader)
    data = []
    for row in reader:
      # iterable creates a tupla with header and each row of list created in reader
      iterable = zip(header, row)
      # applying dictionary comprehension
      country_dict = {key: value for key, value in iterable}
      # another solution
      # country_dict = dict(iterable)
      # print('*'*10)
      # print(country_dict)
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./owner_modules/data.csv')
  print(data[0])