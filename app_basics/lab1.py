"""
Create a cli tool that will keep running, waiting for user input, evaluating and printing.

As a user, I want to be able to input a file path(hint, see os.path), apply head/tail on the file content,
    and see the output  (for example first 3 lines)
As a user, I want to be able to input a csv line, apply head/tail on the line content,
    and see the output(for example first 3 columns)
As a user, I want to be able to exit with a special command (for example '//exit')

As a user, I want to be able to input anything else and see only the head/tail
As a user, I want the program to output the accumulated first word of every line

The tool should print(meaningfully) the exact date and time in which it started, and in which it ended.

save current user input, while input is not exact match '//exit', keep running... (while loop with condition)

testing conditions for each line:
 test if 'exit' cmd, if true -> somehow to exit the while loop -

Tamir
=====
Expected user input in the following line format:
first word - commands:
                    breakout valid values: '//quit', '//exit'
                    head - will be followed by a number (optional default  1)
                    tail - will be followed by a number (optional default  1)
                    print - display the content of the rest of the line to the console.
Second word -   file path, only if file exist will do the head/tail command on the file.
                If not a file, see if contains commas ',' for CSV line.

Third number - optional how many lines, default 3
"""
# SEND_REQUEST_CMD
import os
from datetime import datetime
import commands.validators as valid
import commands.util as util
from commands.constants import constants

if __name__ == '__main__':
    counter: int = 0
    key = constants.keys()
    history_commands = []
    start_time = datetime.now()

    while True:
        counter += 1
        # head res/test.txt 5
        current_line = input("Please enter next command ... \n(first parm is the commands head, tail, print or "
                             "'//quit' to exit. Second param should be a file path or string to print.)")
        # print(f"the user input -> {current_line}")
        parts = current_line.split()
        while len(parts) <= 0 or (cmd := valid.is_command_valid(parts[0]))[1] is False:
            current_line = input("The command wasn't valid! please try again ")
            parts = current_line.split()

        # cmd is a tuple, first item is the command.
        # EXIT_CMDS
        if cmd[0] == list(key)[0]:
            break

        history_commands.append(parts[0])
        # FILE_CMDS
        if cmd[0] == list(key)[1]:
            action, input_file, *rest = parts
            mode = 1 if action == constants[cmd[0]][0] else -1
            try:
                num_of = int(rest[0]) if len(rest) > 0 else 3
            except ValueError:
                # the input contains spaces, need to re split
                input_file = ",".join(parts[1:-1])
                num_of = int(rest[-1]) if len(rest) > 0 else 3
            if os.path.isfile(input_file):
                util.file_tail_or_head(input_file, mode, num_of)
                # if len(rest) > 0:
                #     util.file_tail_or_head(input_file, mode, int(rest[0]))
                # else:
                #     util.file_tail_or_head(input_file, mode)
            else:
                # if not a file see if is csv line
                try:
                    input_file.index(',')
                except ValueError:
                    print("The input was not a file path and not a CSV string format !!! 😟")
                else:
                    print(" a CSV string format 😊")
                    util.csv_tail_or_head(input_file, mode, num_of)
            continue
        # general
        if cmd[0] == list(key)[2]:
            action, *rest = parts
            if action == constants[cmd[0]][1]:
                util.history(history_commands)
            else:
                gf = getattr(util, action)
                gf()

        print(f'iteration number {counter} -- last command {history_commands[-1]}')

    end_time = datetime.now()
    print(
        f"Going out YMF ...\nEntring time:{start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Exit on: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\nTotal use time is {str(end_time-start_time)}")
    # ... final seq, shutdown, clean up - stuff to do
