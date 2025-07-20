def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:  # stop when length drops to 0
        draw_interval(center_length - 1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')  # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  # draw interior ticks for inch
        draw_line(major_length, str(j))  # draw inch j line and label


#draw_ruler(5,3)




def calc_factorial(number):
    if number == 1:
        return number
    else:
        return number*calc_factorial(number-1)
    


# function that finds the minimum and maximum
#values in a sequence without using any loops.
def recursive_find_minmax(sequence,tempmax = None,tempmin=None):
    if tempmax is None or sequence[0] > tempmax:
        tempmax = sequence[0]
    if tempmin is None or sequence[0] < tempmin:
        tempmin = sequence[0]
    if len(sequence[1:])==0:
        return tempmax,tempmin
    else:
        rest_of_sequence = sequence[1:]        
        return recursive_find_minmax(rest_of_sequence,tempmax,tempmin)        

print(recursive_find_minmax([1,66,-1]))         