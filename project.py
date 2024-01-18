q1 = 'What is the capital of France ?'
a1 = input(q1)
point = 0
if a1 == 'Paris':
  print('Correct answer')
  point = point + 1
  print('points:', point)
else:
  print('Wrong answer')
  point = point - 1
  print('points:', point)

q2 = 'When did the WW2 ended ?'
a2 = input(q2)
if a2 == '1945':
  print('Correct answer')
  point = point + 1
  print('points:', point)
else:
  print('Wrong answer')
  point = point - 1
  print('points:', point)

q3 = 'Which is the largest country in the world ?'
a3 = input(q3)
if a3 == 'Russia':
  print('Correct answer')
  point = point + 1
  print('points:', point)
else:
  print('Wrong answer')
  point = point - 1
  print('points;', point)

q4 = 'In which country would you find the Leaning Tower of Pisa ?'
a4 = input(q4)
if a4 == 'Italy':
  print('Correct answer')
  point = point + 1
  print('points:', point)
else:
  print('Wrong answer')
  point = point - 1
  print('points;', point)