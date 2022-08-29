def file_tail_or_head(f_name: str, mode: int, n_lines: int = 3):
    """
    Function to read first or last n_lines lines from a file
    f_name - the file relative path
    mode - 1 is head, -1 is tail
    n_lines - Number of lines to read
    """

    with open(f_name, "r") as file:
        if mode == 1:
            for line in (file.readlines()[:n_lines]):
                print(line, end='')
        elif mode == -1:
            for line in (file.readlines()[-n_lines:]):
                print(line, end='')
        else:
            print("Supports only mode 1/-1")
            return -1

    print("")


def csv_tail_or_head(csv: str, mode: int, n_columns: int = 3):
    columns = csv.split(',')
    if mode == 1:
        for column in columns[:n_columns]:
            print(column, end=' ')
    elif mode == -1:
        for column in columns[-n_columns:]:
            print(column, end=' ')
    print("")


def history(cmd_lst: list):
    print("all commands for this cli session: ")
    for ind, cmd in enumerate(cmd_lst):
        print(f" command: {ind+1} is {cmd} ")


def help_me():
    raise NotImplementedError("Method will be implemented later on (or not) 🥴")

