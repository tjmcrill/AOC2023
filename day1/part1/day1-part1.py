with open('input.txt', 'r') as f:
    total_sum = 0
    for line in f:
        # Find the first and last digit
        first_digit = None
        last_digit = None
        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = int(char)
                last_digit = int(char)

        # Check if both the first and last digits are found
        if first_digit is not None and last_digit is not None:
            calibration_value = int(str(first_digit) + str(last_digit))
            total_sum += calibration_value
    print(total_sum)
