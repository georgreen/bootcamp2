def find_max_min(list_of_integers):
  sorted_list = sorted(list_of_integers)
  min_ele = sorted_list[0]
  max_ele = sorted_list[len(sorted_list) - 1]

  if(min_ele == max_ele):
    return [min_ele]
  else:
    return [min_ele,max_ele]
