from challenge_solutions import *


def test_question_1():
    
    # Provide test inputs and solution
    exp_report_file = './data/expense_report.txt'
    sum_val = 2020
    true_sol = 1016964
    assert question_1(exp_report_file, sum_val) == true_sol


def test_question_1_bonus():
    
    # Provide test inputs and solution
    exp_report_file = './data/expense_report.txt'
    sum_val = 2020
    true_sol = 182588480
    assert question_1_bonus(exp_report_file, sum_val) == true_sol



