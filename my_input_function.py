def input_filter(x):
    '''
    Filters user input
    Args:
        The user defined filter criteria (x)
    Return:
        User input (y) if it passes filter.
     '''
    while True:
        y = input('Type input: ')
        if y.lower() in x:
            return y
            break
        else:
            print('\n\nInvalid input. Please try again')
def main(): #test
    x = ['a','b','c']
    input_filter(x)
if __name__== '__main__':
    main()
