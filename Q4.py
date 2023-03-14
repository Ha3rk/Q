from statistics import mean


def decoration(func):
    def decorated_func(*args, **kwargs):
        # The following code calls the inputer_a function and get the return value into result
        result = func(*args, **kwargs)
        x = 10

        mean_value = result[0]-x
        min_value = result[1] - x
        max_value = result[2] - x
        sum_value = result[3] - x * len(result[4])
        print(
            f"mean= {mean_value}, minimum value = : {min_value}, maximum value = {max_value}, and sum of filtered value is= {sum_value}")
        return result
    return decorated_func


@decoration
def inputer_a(a):
    new_list = [num for num in a if num >= 10 and num <= 100]
    mean_value = mean(new_list)
    min_value = min(new_list)
    max_value = max(new_list)
    sum_value = sum(new_list)

    print(
        f"mean is {mean_value}, minimum value is : {min_value}, maximum value is {max_value}, and sum of filtered value is: {sum_value}")
    return mean_value, min_value, max_value, sum_value, new_list


try:
    def inputer_b(l_list):
        # Now we call first function
        [inputer_a(item) for item in l_list]
        return inputer_b
except:
    print("Ensure first function is running properly!")


inputer_b([[130, 20, 45, 46, 78, 98, 32, 15], [10, 20, 30, 40, 50, 13,
          3, 4, 5, 6, 113], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]])
