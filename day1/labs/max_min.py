def find_max_min(list_of_integers):
  '''
  input: list of ints
  output: if min != max list[min_element, max_element] else [len(list)]
  '''
  sorted_list = sorted(list_of_integers)
  min_ele = sorted_list[0]
  max_ele = sorted_list[len(sorted_list) - 1]

  if(min_ele == max_ele):
    return [len(list_of_integers)]
  else:
    return [min_ele,max_ele]
