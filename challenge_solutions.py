"""
.. module:: challenge_solutions
   :synopsis: Module that includes functions for solving the RWDI challenge
   questions. A separate function attempts to answer a single questions and
   function name is "question_X" where X is the day number number. The functions
  "question_X_bonus" solve the second parts of questions for each day, wherever applicable. 
.. moduleauthor:: Taimoor Akhtar <taimoor.akhtar@gmail.com>,
"""

import re

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


def question_2(password_list_file: str):
    """Find valid passwords given policy. The complete description of problem
given at https://adventofcode.com/2020/day/2

    Args:
        password_list_file (str): File with list of passwords and policy

    Returns:
        int: Count of valid passwords 
    """

    # Read password list from file
    with open(password_list_file, 'r') as f:
        password_list = [line.rstrip() for line in f]

    # Loop over list to count valid passwords
    valid_count = 0
    for password_item in password_list:
        temp_1 = password_item.split()
        temp_2 = temp_1[0].split('-')
        min_repeat = int(temp_2[0])
        max_repeat = int(temp_2[1])
        repeat_letter = temp_1[1][0]
        password = temp_1[2]
        actual_repeat = password.count(repeat_letter)
        if (actual_repeat >= min_repeat) and (actual_repeat <= max_repeat):
            valid_count += 1
    
    return valid_count


def question_2_bonus(password_list_file: str):
    """Find valid passwords given policy. The complete description of problem
given at https://adventofcode.com/2020/day/2

    Args:
        password_list_file (str): File with list of passwords and policy

    Returns:
        int: Count of valid passwords 
    """

    # Read password list from file
    with open(password_list_file, 'r') as f:
        password_list = [line.rstrip() for line in f]

    # Loop over list to count valid passwords
    valid_count = 0
    for password_item in password_list:
        temp_1 = password_item.split()
        temp_2 = temp_1[0].split('-')
        first_loc = int(temp_2[0]) - 1
        second_loc = int(temp_2[1]) - 1
        repeat_letter = temp_1[1][0]
        password = temp_1[2]
        if (((password[first_loc] == repeat_letter) and (password[second_loc]  != repeat_letter)) or ((password[first_loc] != repeat_letter) and (password[second_loc]  == repeat_letter))):
            valid_count += 1
    
    return valid_count


def question_4(passport_file: str):
    """This function processes a passport data batch file to count number of
valid passport entries. Exact problem solved here is described at https://adventofcode.com/2020/day/4

    Args:
        passport_file (str): Name of passport file

    Returns:
        int: Number of valid passports in file
    """

    with open(passport_file, 'r') as f:
        passport_lines = f.readlines()   
    valid_passport_count = 0
    
    passports = [] # list of passports (maybe needed later)
    passport_data = [] # data for each passport
    net_valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for line in passport_lines:
        if line == '\n':
            passports.append(dict(passport_data))
            passport_data = []
            # TODO: Check validity of fields in future
            if len(net_valid_fields) == 0:
                valid_passport_count += 1
            elif len(net_valid_fields) == 1 and net_valid_fields[0] == 'cid':
                valid_passport_count += 1
            net_valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']    
        line = line.split()
        for item in line:
            passport_field = item.split(':')
            if passport_field[0] in net_valid_fields:
                net_valid_fields.remove(passport_field[0])
            passport_data.append(passport_field)
    # Check last passport
    # TODO: Check validity of fields in future
    if len(net_valid_fields) == 0:
            valid_passport_count += 1
    elif len(net_valid_fields) == 1 and net_valid_fields[0] == 'cid':
        valid_passport_count += 1

    return valid_passport_count


def question_4_bonus(passport_file: str):
    """This function processes a passport data batch file to count number of
valid passport entries. Exact problem solved here is described at https://adventofcode.com/2020/day/4#part2

    Args:
        passport_file (str): Name of passport file

    Returns:
        int: Number of valid passports in file
    """

    with open(passport_file, 'r') as f:
        passport_lines = f.readlines()   
    valid_passport_count = 0
    
    passports = [] # list of passports 
    passport_data = [] # data for each passport
    net_valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for line in passport_lines:
        if line == '\n':
            passports.append(dict(passport_data))
            passport_data = []
            # TODO: Check validity of fields in future
            if len(net_valid_fields) == 0:
                valid_passport_count += 1
            elif len(net_valid_fields) == 1 and net_valid_fields[0] == 'cid':
                valid_passport_count += 1
            net_valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']  
        line = line.rstrip()  
        line = line.split()
        for item in line:
            passport_field = item.split(':')
             #  Check validity of fields here
            if passport_field[0] == 'byr':
                try:
                    if int(passport_field[1]) >= 1920 and int(passport_field[1]) <= 2002: 
                        net_valid_fields.remove(passport_field[0])
                except ValueError:
                    pass
            elif passport_field[0] == 'iyr':
                try:
                    if int(passport_field[1]) >= 2010 and int(passport_field[1]) <= 2020: 
                        net_valid_fields.remove(passport_field[0])
                except ValueError:
                    pass
            elif passport_field[0] == 'eyr':
                try:
                    if int(passport_field[1]) >= 2020 and int(passport_field[1]) <= 2030: 
                        net_valid_fields.remove(passport_field[0])
                except ValueError:
                    pass
            elif passport_field[0] == 'hgt': 
                height_data = re.split(r'(\d+)', passport_field[1])
                try:
                    height_data = re.split(r'(\d+)', passport_field[1])
                    height_data = list(filter(None, height_data))
                    if len(height_data) == 2:
                        if height_data[1] == 'cm':
                            if int(height_data[0]) >= 150 and int(height_data[0]) <= 193:
                                net_valid_fields.remove(passport_field[0])
                        if height_data[1] == 'in':
                            if int(height_data[0]) >= 59 and int(height_data[0]) <= 76:
                                net_valid_fields.remove(passport_field[0])  
                except ValueError:
                    pass
            elif passport_field[0] == 'hcl':
                try:
                    color = passport_field[1]
                    if color[0] == '#' and len(color) == 7:
                        valid_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
                        color_code = color[1:]
                        count_chars = 0
                        for code in color_code:
                            if code in valid_characters:
                                count_chars += 1
                        if count_chars == 6:
                            net_valid_fields.remove(passport_field[0])  
                except ValueError:
                    pass 
            elif passport_field[0] == 'ecl':
                try:
                    color = passport_field[1]
                    valid_colors = ['amb', 'blu' , 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if color in valid_colors:
                        net_valid_fields.remove(passport_field[0])
                except ValueError:
                    pass
            elif passport_field[0] == 'pid':
                try:
                    pid = passport_field[1]
                    valid_pid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    count_digits = 0
                    for id in pid:
                        if id in valid_pid_chars:
                            count_digits += 1
                    if count_digits == 9:
                        net_valid_fields.remove(passport_field[0])   
                except ValueError:
                    pass
            
            passport_data.append(passport_field)
    # Check last passport
    if len(net_valid_fields) == 0:
            valid_passport_count += 1
    elif len(net_valid_fields) == 1 and net_valid_fields[0] == 'cid':
        valid_passport_count += 1

    return valid_passport_count


def question_5(boarding_seq_file_name: str):
    """This question finds coresponding seat IDs given boarding sequences. The
sequence to id conversion is defined at https://adventofcode.com/2020/day/5

    Args:
        boarding_seq_file_name (str): Boarding sequence (10-character string)

    Returns:
        list: seat ids corresponding to given boarding sequences
    """

    # Read password list from file
    with open(boarding_seq_file_name, 'r') as f:
        boarding_seq_list = [line.rstrip() for line in f]
    
    # iterate through file to get seat ids
    seat_ids = []
    for boarding_sequence in boarding_seq_list:

        # Determine row number
        row_number = 0
        for i in range(7):
            if boarding_sequence[i] == 'B':
                row_number = row_number + 2**(6-i)
        
        # Determine column number
        col_number = 0
        for i in range(7,10):
            if boarding_sequence[i] == 'R':
                col_number = col_number + 2**(9-i)
        
        seat_id = row_number*8 + col_number
        seat_ids.append(seat_id)

    return seat_ids


def question_5_bonus(boarding_seq_file_name: str):
    """This questions finds the unknown seat id via process of elimination. The
exact question answered here is given in https://adventofcode.com/2020/day/5

    Args:
        boarding_seq_file_name (str): File with boarding sequences of others

    Returns:
        int: My seat id
    """
    # Get occupied seat ids
    seat_ids = question_5(boarding_seq_file_name)
    seat_ids = sorted(seat_ids)
    # Estimate all possible seats
    valid_seats = list(range(min(seat_ids),max(seat_ids)+1))
    possible_seats = list(set(valid_seats) - set(seat_ids))
    final_seat = possible_seats[0]
    # Find first seat that has two adjacent filled seats
    while len(possible_seats) > 2:
        if (possible_seats[1] - final_seat) == 1:
            final_seat = possible_seats[2]
            possible_seats.pop(0)
        else:
            break
    
    return final_seat
    


    #print(excluded_seats) 

boarding_seq_file_name = './data/boarding_sequences.txt'
print(question_5_bonus(boarding_seq_file_name))