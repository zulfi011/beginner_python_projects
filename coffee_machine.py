resources = {
  'water':600, #ml
  'milk':400, #ml
  'coffe':300, #mg
  'suger':200 #mg
  }

coffes = {
  'espresso':{
      'ingredients' : {'water':250,'milk':0,'suger':12,'coffe':30},
      'cost' : 5
      },
  'late':{
      'ingredients' : {'water':250,'milk':150,'suger':15,'coffe':20},
      'cost' : 4
      },
  'black':{
      'ingredients' : {'water':300,'milk':100,'suger':10,'coffe':30},
      'cost': 7
      },
  'cappacino':{
      'ingredients': {'water':300,'milk':150,'suger':12,'coffe':25},
      'cost':6
      }
  }
while True:
  menu = [x for x in coffes.keys()]
  print('MENU')
  for key,val in coffes.items():
      print(f"{key} : {val['cost']} $")
  choice = ''
  while True:
      line = input('what would you like or q to quit: ').lower()
      if line=='q':
          quit()
      elif line in menu:
          choice = line
          break
      else:
          print('not a valid option')
  okay_to_go = []
  resources_check = False
  for key,val in coffes[choice]['ingredients'].items():
      if resources[key]>=coffes[choice]['ingredients'][key]:
          okay_to_go.append(True)
      else:
          okay_to_go.append(False)
  if False in okay_to_go:
      print('not enough resourses')
      for key,val in resources.items():
              print(f'{key}: {val}')
      continue
  else:
      resources_check = True
  payment_done = False
  payment = 0
  while True:
      while True:
          line = input('plz insert '+ str(coffes[choice]['cost'])+'$: ')
          if line.isdigit():
              payment += int(line)
              break
          else:
              print('plz insert payment')
      if payment==coffes[choice]['cost']:
          payment_done = True
          break
      elif payment>coffes[choice]['cost']:
          print('here is our change '+str(payment-coffes[choice]['cost'])+'$')
          payment_done = True
          break
      else:
          print('not enough payment')
          break
  if payment_done and resources_check:
      for key in coffes[choice]['ingredients'].keys():
          resources.update({key:resources[key]-coffes[choice]['ingredients'][key]})
      print(f'here is your {choice} '+"\N{HOT BEVERAGE}"+ " enjoy")