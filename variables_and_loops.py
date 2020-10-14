import numpy as np          # imports the numpy module

def main():
    i = 0                   # assign integer value 0 to variable i
    n = 10                  # assign integer value 10 to variable n
    x = 119.0               # assign float value 119.0 to variable x

    # we can use numpy to declare arrays quickly

    y = np.zeros(n, dtype=float)    # declares 10 zeroes (referenced by variable n)

    # we can use for loops to iterate with a variable

    for i in range(n):      # runs the loop 10 times
        y[i] = 2.0 * float(i) + 1.  # set y = 2i + 1 as floats

    # we can also simply iterate through a variable
    for y_element in y:
        print(y_element)

# execute the main function
if __name__ == "__main__":
    main()
