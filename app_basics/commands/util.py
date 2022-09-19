def file_tail_or_head(f_name: str, mode: int, n_lines: int = 3):
    """
    Function to read first or last n_lines lines from a file
    f_name - the file relative path
    mode - for 1 do head mode!=1 do tail, default 1.
    n_lines - Number of lines to read
    """

    with open(f_name, "r") as file:
        if mode == 1:
            for line in (file.readlines()[:n_lines]):
                print(line, end='')
        else:
            for line in (file.readlines()[-n_lines:]):
                print(line, end='')
    print("")


def csv_tail_or_head(csv: str, mode: int = 1, n_columns: int = 3):
    """
    Method to be use on CSV line, that print the first or last column of the given line.
    csv - Is the CSV line, it is expected to be valid (caller of this method should ensue its validation)
    mode - for 1 do head mode!=1 do tail, default 1.
    n_columns - how many columns will extract from the line, default 3
    """
    columns = csv.split(',')
    if mode == 1:
        for column in columns[:n_columns]:
            print(column, end=' ')
    else:
        for column in columns[-n_columns:]:
            print(column, end=' ')
    print("")


def history(cmd_lst: list):
    print("all commands for this cli session: ")
    for ind, cmd in enumerate(cmd_lst):
        print(f" command: {ind+1} is {cmd} ")


def help_me():
    raise NotImplementedError("Method will be implemented later on (or not) 🥴")

