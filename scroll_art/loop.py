import math, time, os, sys

os.system('cls | clear')  # Clear the screen

width = os.get_terminal_size()[0] - 1
delay = 0.1

def main():
    if len(sys.argv) > 4:
        message_1 = sys.argv[1]
        message_2 = sys.argv[2]
        step_increase_1 = float(sys.argv[3])
        step_increase_2 = float(sys.argv[4])
    elif len(sys.argv) > 3:
        message_1 = sys.argv[1]
        message_2 = sys.argv[2]
        step_increase_1 = float(sys.argv[3])
        step_increase_2 = 0.2
    elif len(sys.argv) > 2:
        message_1 = sys.argv[1]
        message_2 = sys.argv[2]
        step_increase_1 = 0.2
        step_increase_2 = 0.1
    elif len(sys.argv) > 1:
        message_1 = sys.argv[1]
        message_2 = '...'
        step_increase_1 = 0.2
        step_increase_2 = 0.1
    else:
        message_1 = '...'
        message_2 = '...'
        step_increase_1 = 0.2
        step_increase_2 = 0.1

    step_1 = 0.0
    step_2 = 0.0
    while True:  # Main program loop.
        width = os.get_terminal_size()[0] - 1
        multiplier_1 = (width - len(message_1)) / 2
        multiplier_2 = (width - len(message_2)) / 2
        sin_of_step_1 = math.sin(step_1)
        sin_of_step_2 = -math.sin(step_2)
        padding_1 = ' ' * int((sin_of_step_1 + 1) * multiplier_1)
        padding_2 = ' ' * int((sin_of_step_2 + 1) * multiplier_2)
        print(padding_1 + message_1)
        print(padding_2 + message_2)
        time.sleep(delay)
        step_1 += step_increase_1
        step_2 += step_increase_2


try:
    main()
except KeyboardInterrupt:
    print('Sine Message, by Al Sweigart al@inventwithpython.com 2021. modified by mac sanmiguel')