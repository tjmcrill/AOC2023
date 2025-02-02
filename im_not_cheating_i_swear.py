from openai import OpenAI

client = OpenAI(api_key = 'hahah you cant have my api key')
message = "The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number. For example: 1abc2 pqr3stu8vwx a1b2c3d4e5f treb7uchet. In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142. Consider your entire calibration document. What is the sum of all of the calibration values?"
message2 = "Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid digits. Equipped with this new information, you now need to find the real first and last digit on each line. For example: two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2 zoneight234 7pqrstsixteen In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281. What is the sum of all of the calibration values?"
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful coding assistant, helping me solve Advent of Code problems."},
    {"role": "user", "content": message},
    {"role": "user", "content": "This is part 2 to the above question: " + message2}
  ]
)

print(completion.choices[0].message.content)