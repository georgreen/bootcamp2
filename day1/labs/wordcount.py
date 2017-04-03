def words(string_input):
  results = {}
  split_words = string_input.split()
  seen_words = []

  for word in split_words:
      try:
          num = int(word)
          word = num
      except ValueError:
          pass

      if seen_words.__contains__(word):
          results[word] = results[word] + 1
      else:
          seen_words.append(word)
          results[word] = 1
  return results
