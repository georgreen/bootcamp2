def words(string_input):
  '''
  input : string
  output: dict{word : count}
  '''
  results = {}
  split_words = string_input.split()

  for word in split_words:
      try:
          num = int(word)
          word = num
      except ValueError:
          pass

      if word in results:
          results[word] += 1
      else:
          results[word] = 1
  return results
