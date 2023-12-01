value_dict = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

with open('input.txt', 'r') as f:
  sum = 0
  for line in f:
    line.strip()

    search_terms = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    firstDigitIndex = len(line)
    firstDigit = ""
    for term in search_terms:
        if term in line:
            index = line.index(term)
            if index < firstDigitIndex:
                firstDigitIndex = index
                firstDigit = term
      
    lastDigitIndex = -1
    lastDigit = ""
    for term in search_terms:
        if term in line:
            index = line.rindex(term)
            if index > lastDigitIndex:
                lastDigitIndex = index
                lastDigit = term
    
    sum += int(value_dict[firstDigit] + value_dict[lastDigit])

  print(sum)