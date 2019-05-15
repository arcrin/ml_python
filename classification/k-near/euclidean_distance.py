from math import sqrt

plot1 = [1, 3]
plot2 = [2, 5]

def euclidean_distance(p1, p2):
  sum_of_square = 0
  for element in zip(p1, p2):
    sum_of_square += (element[1] - element[0])**2
  return sqrt(sum_of_square)

print(euclidean_distance(plot1, plot2))