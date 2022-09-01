from typing import Tuple
from .constants import valid_cmds_dic as valid_cmds


def is_command_valid(raw_cmd: str) -> Tuple[str, bool]:
    """
    slug - the category the cmd relates to.

    Args:
        raw_cmd: The command that is to be search if exist in the command dictionary.
    """
    for slug, cmd in valid_cmds.items():
        if type(cmd) is not tuple:
            print("The constants value must be in tuple format !!!")
            return "", False

        if raw_cmd in cmd:
            return slug, True
    print(f"In is_command_valid, the {raw_cmd} is not a supported command")
    return "", False


def is_cmd(raw_cmd: str, cmd: str) -> bool:
    return is_command_valid(raw_cmd) and raw_cmd == cmd


def is_exit_cmd(raw_cmd: str):
    return is_cmd(raw_cmd, valid_cmds["EXIT_CMDS"])


# usr_input = '//quit'
# cmd_slug, is_valid_as_cmd = is_command_valid(usr_input)
# print()
#
# print("Going to exit - {} !".format(is_exit_cmd(usr_input)))
