import random
def primary():
  #print("Keep it logically awesome.")

  #add quotes programmaticaly
  f = open ("quotes.txt", "a")
  text = "Keep it simple, stupid\n"
  f.write (text)
  f.close

  #open and read after appending
  f = open ("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len (quotes) - 1
  rnd = random.randint (0, last)
  rnd2 = random.randint (0, last)
  print(quotes[rnd].rstrip ('\n'))
  print(quotes[rnd2].rstrip ('\n'))

if __name__== "__main__":
  primary()
