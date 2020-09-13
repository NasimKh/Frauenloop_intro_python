# leap year
def is_leap(year):
  leap = False

  if (year % 4 == 0) and (year % 100 != 0):
      # Note that in your code the condition will be true if it is not..
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):
      # For some reason here you had False twice
      leap = True
  else:
      leap = False

  return leap
