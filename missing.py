def find_missing(list1,list2):

  find = 0

  if len(list1) > len(list2):
    missing= set(list1).difference(list2)
    find = missing.pop()
    return find

  elif len(list1) < len(list2):
    missing = set(list2).difference(list1)
    find = missing.pop()
    return find
  else:
    return (0)
