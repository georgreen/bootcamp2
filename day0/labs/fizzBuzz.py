
def fizz_buzz(some_input):
  if(some_input % 3 == 0 and some_input % 5 == 0):
    return 'FizzBuzz'

  if(some_input % 5 == 0):
    return 'Buzz'

  if(some_input % 3 == 0):
    return 'Fizz'

  return some_input
