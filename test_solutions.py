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


def test_question_2():
    password_file_name = './data/passwords_policy.txt'
    true_sol = 643
    assert question_2(password_file_name) == true_sol


def test_question_2_bonus():
    password_file_name = './data/passwords_policy.txt'
    true_sol = 388
    assert question_2_bonus(password_file_name) == true_sol


def test_question_4():
    passport_file_name = './data/passport_data.log'
    true_sol = 200
    assert question_4(passport_file_name) == true_sol


def test_question_4_bonus():
    passport_file_name = './data/passport_data.log'
    true_sol = 116
    assert question_4_bonus(passport_file_name) == true_sol


def test_question_5():
    boarding_seq_file_name = './data/boarding_sequences.txt'
    true_sol = 938
    seat_ids = question_5(boarding_seq_file_name)
    assert max(seat_ids) == true_sol


def test_question_5_bonus():
    boarding_seq_file_name = './data/boarding_sequences.txt'
    true_sol = 696
    seat_id = question_5_bonus(boarding_seq_file_name)
    assert seat_id == true_sol