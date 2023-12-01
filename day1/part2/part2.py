def find_calibration_value(line):
    first_digit = ''
    last_part = ''

    # Find the first numeric part
    for char in line:
        if char.isdigit():
            first_digit += char
        elif first_digit:
            break

    # Find the last alphanumeric part
    for char in reversed(line):
        if char.isalnum():
            last_part = char + last_part
        elif last_part:
            break

    # Convert spelled-out numbers in the last part
    number_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    last_part_lower = last_part.lower()
    last_digit = number_mapping.get(last_part_lower, None)

    if last_digit is None:
        last_digit = int(''.join(filter(str.isdigit, last_part)))

    # Handle cases where first or last parts are empty
    if not first_digit:
        first_digit = 0

    # Calculate the calibration value
    calibration_value = int(str(first_digit) + str(last_digit))
    return calibration_value

with open('input.txt', 'r') as f:
    total = 0
    for line in f:
        calibration_value = find_calibration_value(line)
        total += calibration_value
    print(total)
