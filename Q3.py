
# take sequence and digit input from user
x = input('Enter sequence of characters: ')
y = input('Enter a single digit: ')
char_size = len(x)

# check if y is a digit
if y.isdigit() and 0 < int(y):
    y = int(y)

    # check if character size is divided by y into equal parts
    if char_size % y == 0:

        # divide character into equal parts from length set by y
        parts = [x[i:i+y] for i in range(0, char_size, y)]

        # print unique characters in order which they appear
        for part in parts:
            unique_char = []
            for char in part:
                if char not in unique_char:
                    unique_char.append(char)
            print(''.join(unique_char))

    else:
        print(f'Sequence length ({char_size}) cannot be divided by {y}')
else:
    print('Not valid input digit. Please enter a digit greater than 0')
