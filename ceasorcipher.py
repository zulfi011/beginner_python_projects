while True:
  message = input('input value or enter to quit: ')
  if message == '':
      quit()
  while True:
      shift = input("how many times to move the value: ")
      if shift.isdigit():
          break
      elif int(shift)<0:
          break
      else:
          print('must be an integer')
  new_message = ""
  for ch in message:
      if ch >= "a" and ch <= "z":
  # Process a lowercase letter by determining its
  # position in the alphabet (0 - 25), computing its
  # new position, and adding it to the new message
          pos = ord(ch) - ord("a")
          pos = (pos + int(shift)) % 26
          new_char = chr(pos + ord("a"))
          new_message = new_message + new_char
      elif ch >= "A" and ch <= "Z":
  # Process an uppercase letter by determining its position in the alphabet (0 - 25),
  # computing its new position, and adding it to the new message
          pos = ord(ch) - ord("A")
          pos = (pos + int(shift)) % 26
          new_char = chr(pos + ord("A"))
          new_message = new_message + new_char
      else:
  # If the character is not a letter then copy it into the new message
          new_message = new_message + ch
  print(new_message)