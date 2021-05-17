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
    passport_file_name = './data/passport_data.txt'
    true_sol = 200
    assert question_4(passport_file_name) == true_sol


def test_question_4_bonus():
    passport_file_name = './data/passport_data.txt'
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


def test_question_6():
    file_name = './data/customs_questions.txt'
    true_sol = 6532
    distr, sol = question_6(file_name)
    assert sol == true_sol


def test_question_10():
    file_name = './data/adapter_list.txt'
    true_sol = 2100
    sol = question_10(file_name)
    assert sol == true_sol


def test_question_15():
    seq = [1, 20, 11, 6, 12, 0]
    end_turn = 2020
    true_sol = 1085
    # Note: Have not added test for question 15 part 2 but its solved
    sol = question_15(seq, end_turn)
    assert sol == true_sol


def test_question_21():
    file_name = './data/food_allergies.txt'
    true_sol = 2635
    sol = question_21(file_name)
    assert sol == true_sol


def test_question_18():
    file_name = './data/expressions_list.txt'
    true_sol = 3885386961962
    sol = question_18(file_name)
    assert sol == true_sol

    
def test_question_13():
    file_name = './data/bus_notes.txt'
    true_sol = 2305
    sol = question_13(file_name)
    assert sol == true_sol


def test_question_25():
    public_key_card = 10705932
    public_key_door = 12301431
    true_sol = 11328376
    sol = question_25(public_key_card, public_key_door)
    assert sol == true_sol


def test_question_12():
    file_name = './data/navigation_instructions.txt'
    true_sol = 1710
    sol = question_12(file_name)
    assert sol == true_sol
