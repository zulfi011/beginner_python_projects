def convertion(num):
  ones = ['one','two','three','four','five','six','seven'\
          ,'eight','nine']
  twos = ['ten','eleven','twelve','thirteen','fourteen','fifteen',\
          'sixteen','seventeen','eighteen','nineteen']
  tens = [
      '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty',
      'ninety'
  ]

  def convert(num):
    if num == 0:
      return ''
    if num <= 9:
      return ones[num - 1]
    elif num >= 9 and num <= 19:
      return twos[num % 10]
    elif num >= 19 and num <= 99:
      return tens[(num // 10) - 1] + ' ' + convert(num % 10)
    elif num >= 100 and num <= 999:
      return str(ones[(num // 100) - 1]) + ' hundred ' + convert(num % 100)
    elif num >= 1000 and num <= 19999:
      new = ones + twos
      return str(new[(num // 1000) - 1]) + ' thousand ' + convert(num % 1000)
    elif num >= 20000 and num <= 99999:
      value = str(tens[(num // 10000) - 1]) + convert(num % 10000)
      if value in tens:
        return value + ' thousand'
      else:
        return value

  eng_form = convert(num)
  return eng_form.strip()


num = input('input the number: ')
while True:
  if num.isdigit():
    break
  else:
    print('must be a valid input')

result = convertion(int(num))
print(f"{num} in English: {result}")
