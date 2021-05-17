"""
.. module:: challenge_solutions
   :synopsis: Module that includes functions for solving the RWDI challenge
   questions. A separate function attempts to answer a single questions and
   function name is "question_X" where X is the question number
.. moduleauthor:: Taimoor Akhtar <akhtart@uoguelph.ca>,
"""


def question_1(exp_report_file: str, sum_val: int):
    """Find two numbers in expense report array that sum to a given number

    Args:
        exp_report_file (str): Name of expense report file / path
        sum_val (int): The sum value

    Returns:
        [int]: Multiple of items that sum to sum_val
    """

    # Load expense report
    with open(exp_report_file, 'r') as f:
        exp_report = [int(x) for x in f.read().split()]

    if len(exp_report) < 2: # Some basic error checking
        return None
    else:
        while len(exp_report) > 0: 
            item = sum_val - exp_report.pop(0)
            if item in exp_report:
                return item*(sum_val - item)
        return None


def question_1_bonus(exp_report_file: str, sum_val: int):
    """Find three numbers in expense report array that sum to a given number

    Args:
        exp_report_file (str): Name of expense report file / path
        sum_val (int): The sum value

    Returns:
        [int]: Multiple of items that sum to sum_val
    """
    # NOTE: The general solution would use recursion or maybe dynamic
    # programming for improving efficiency 
    # Load expense report
    with open(exp_report_file, 'r') as f:
        exp_report = [int(x) for x in f.read().split()]

    if len(exp_report) < 3: # Some basic error checking
        return None
    else:
        while len(exp_report) > 0: 
            item_1 = exp_report.pop(0)
            sum_val_rem = sum_val - item_1
            remaining_items = exp_report.copy()
            while len(remaining_items) > 0:
                item_2 = remaining_items.pop(0)
                item_3 = sum_val_rem - item_2
                if item_3 in remaining_items:
                    return item_1*item_2*item_3
        return None


