# define the main function
def main():
    i = int(0)              # declare an integer i
    x = float(119.0)        # declare a float x

    for i in range(120):    # loop starting from zero to 119, which is 120 terms
        if(i % 2) == 0:       # if i is even (when dividing by 2 leaves no remainder)
            x += 3.             # add 3 to x
        else:               # otherwise, if i is odd
            x -= 5.             # subtract 5 from x

    s = "%3.2e" % x         # make a string containing x with
                            # sci. notation w/ 2 decimal places

    print(s)                # print s to the screen

# now the rest of the program continues

if __name__ == "__main__":  # if the main() function exists, run it
    main()
