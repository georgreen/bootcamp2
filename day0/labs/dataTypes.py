def data_type(data_X):

  if(type(data_X) == type('str')):
    return len(data_X)

  if(type(data_X) == type(True)):
    return data_X

  if(data_X == None):
    return 'no value'

  if(type(data_X) == type([])):
    if(len(data_X) >= 3):
      return data_X[2]
    return

  if(type(data_X) == type(1)):
    if(data_X == 100):
      return 'equal to 100'
    if(data_X > 100):
      return 'more than 100'

    if(data_X < 100):
      return 'less than 100'
  
