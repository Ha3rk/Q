
# The following code has the return type specified with ()->, as allowed by Python 3.5,
# ..as a error handling technique.
def inputer() -> int:
    # The inputs n,a,b are type cast as string, so it is inconsequential that we may have other input types
    n = str(input("here: "))
    a = str(input("here: "))
    b = str(input("here: "))
    # Error handling
    try:
        totalcount = 0
        for char in n:
            if char in a:
                totalcount += 1
            elif char in b:
                totalcount -= 1
        print(totalcount)
        return totalcount
    except:
        print("Ensure you input the expected types!")


inputer()
