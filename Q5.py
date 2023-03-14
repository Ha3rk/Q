
# Python3 program to compress a text
# give how many consecutive times it repeats itself
def compress(text):

    n = len(text)
    i = 0
    while i < n - 1:

        # Count consecutive occurrences of current character

        count = 1
        while (i < n - 1 and text[i] == text[i + 1]):
            count += 1
            i += 1
        i += 1

        # Print character and its count
        print(text[i - 1] + str(count), end="")


# Driver code
if __name__ == "__main__":

    text = "ggekkllrrro"
    compress(text)
