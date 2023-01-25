import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  # plt.show() only create a figure in environment, for this uses plt.savefit('name with extension')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['Aguadas', 'Pereira', 'Manizales']
  values = [20, 50, 100]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)