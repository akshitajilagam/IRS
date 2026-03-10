def locate(sub, main):

  size_main = len(main)
  size_sub = len(sub)

  print('Given String:', main)
  print("Search string:", sub)
  print("------------------------------")

  found_any = 0

  index = 0

  while index <= size_main - size_sub:
    k = 0

    while k < size_sub:
      
      if main[index + k] != sub[k]:
        break
      k = k + 1
    if k == size_sub:
      print("Substring exits at position", index)
      found_any = 1
    
    index = index + 1

  if found_any == 0:
    print("Substring not found in given string")

# code
full_text= "AABAACAADAABAABA"
search_text = "AABA"

locate(search_text, full_text)
