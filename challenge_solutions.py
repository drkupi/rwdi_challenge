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
    

def question_6(customs_questions_file: str):
    """This function counts and returns the number of customs questions asked.
The solutions corresponds to the puzzle given at https://adventofcode.com/2020/day/6

    Args:
        customs_questions_file (str): Customs file name

    Returns:
        tuple: distribution and sum of yes answers
    """

    with open(customs_questions_file, 'r') as f:
        q_lines = f.readlines() 
    
    yes_counts = []
    yes_answers_all = []
    yes_answers_group = ''
    for line in q_lines:
        if line == '\n':
            yes_answers_all.append(set(yes_answers_group))
            yes_counts.append(len(set(yes_answers_group)))
            yes_answers_group = ''
        else:
            yes_answers_group = yes_answers_group + line.strip()

    yes_answers_all.append(set(yes_answers_group))
    yes_counts.append(len(set(yes_answers_group)))

    return yes_counts, sum(yes_counts)


def question_10(adapter_file_name: str):
    """This function solves Day 10, Part 1 of the code challenge given in
https://adventofcode.com/2020/day/10. Given a list of adapters we find
distribution of differences.

    Args:
        adapter_file_name (str): Name of adapter file

    Returns:
        int: multiple of 1-diff count and 3-diff count
    """

    with open(adapter_file_name, 'r') as f:
        adapter_list = [int(x) for x in f.read().split()]

    sorted_adapters = sorted(adapter_list)
    sorted_adapters.insert(0,0)
    sorted_adapters.append(sorted_adapters[-1] + 3)
    diff_list = [y - x for x, y in zip(sorted_adapters, sorted_adapters[1:])]
    diff_distribution = {x:diff_list.count(x) for x in set(diff_list)}

    return diff_distribution[1]*diff_distribution[3]


def question_15(starting_numbers: list, end_turn: int):
    """This function creates a sequence as given in the challenge at
https://adventofcode.com/2020/day/15 and returns the nth number (end_turn)

    Args:
        starting_numbers (list): Starting sequence
        end_turn (int): Ending turn number

    Returns:
        int: Number in sequence at end_turn (2020)
    """

    # Note: solved both Part 1 and Part 2 through this code
    prev_number = starting_numbers[-1]
    memory_dict = {}
    i = 1
    for number in starting_numbers:
        memory_dict[number] = i
        i += 1
    
    for turn in range(len(starting_numbers)+1, end_turn+1):
        if prev_number in memory_dict.keys():
            curr_number = (turn - 1) - memory_dict[prev_number]
        else:
            curr_number = 0
        memory_dict[prev_number] = turn - 1
        prev_number = curr_number

    return curr_number   


def question_21(food_allergy_file: str):
    """Function for finding ingredients that are not associated with allergies.
Full puzzle related to question described at https://adventofcode.com/2020/day/21

    Args:
        food_allergy_file (str): Allergies file name

    Returns:
        int: Count of ingredients in food items that are without allergens (repeat count included)
    """


    # Parse file to store data in dictionary
    with open(food_allergy_file, 'r') as f:
        lines = [line.rstrip() for line in f]

    food_items = []
    for line in lines:
        ingredients = line.split('(')[0].split()
        allergens = line.split('(')[1].split(')')[0].replace('contains ', '').replace(',', '').split()
        food_item = {
            'ingredients': ingredients,
            'allergens': allergens
        }
        food_items.append(food_item)

    allergens = [x['allergens'] for x in food_items]
    allergens = set([val for sublist in allergens for val in sublist])
    ingredients =[x['ingredients'] for x in food_items]
    ingredients = [val for sublist in ingredients for val in sublist]
    ingredients_freq = {x:ingredients.count(x) for x in set(ingredients)}
    ingredients = set(ingredients)

    allergen_ingredients = {}

    for allergen in allergens:
        allergen_ingredients[allergen] = None
        for item in food_items:
            if allergen in item['allergens']:
                if allergen_ingredients[allergen] is None:
                    allergen_ingredients[allergen] = set(item['ingredients'])
                else:
                    allergen_ingredients[allergen] =  set.intersection(allergen_ingredients[allergen], set(item['ingredients']))
    
    # Find common ingredients
    common_ingredients =[list(x) for x in allergen_ingredients.values()]
    common_ingredients = set([val for sublist in common_ingredients for val in sublist])
    
    # Find ingredients without allergens (No error check done)
    ingredients_without_allergens = ingredients - common_ingredients
    count_ingredients_without_allergens = 0
    for item in ingredients_without_allergens:
        count_ingredients_without_allergens += ingredients_freq[item]
    
    return count_ingredients_without_allergens



def question_18(expression_list_file: str):
    """This function implements a basic calculator as described at
https://adventofcode.com/2020/day/18 to compute answers to a list of expressions
given from a file. Returns the sum of all expressions.

    Args:
        expression_list_file (str): File with list of expressions

    Returns:
        int: sum of expression outputs
    """
    
    # Parse expression list file to get all expressions
    with open(expression_list_file, 'r') as f:
        expressions = [line.rstrip() for line in f]

    final_sum_val = 0
    # The following loop evaluates each expression
    for expression in expressions:
        value = 0
        expression = expression.strip()
        operation = '+'
        expression_stack = []
        for i in range(len(expression)):
            s = expression[i]
            if s.isdigit():
                if operation == '+':
                    value = value + int(s)
                else:
                    value = value * int(s)
            if s == '+' or s == '*':
                operation = s
            if s == '(':
                expression_item = {
                    'value': value,
                    'operation': operation
                }
                expression_stack.append(expression_item)
                value = 0
                operation = '+'
            if s == ')':
                if expression_stack[-1]['operation'] == '+':
                    value = value + expression_stack[-1]['value']
                else:
                    value =  value * expression_stack[-1]['value']
                expression_stack = expression_stack[:-1]
        final_sum_val += value
        
    return final_sum_val


def question_13(bus_notes_file: str):
    """This function computes the bus id and wait time for the puzzle problem
given at https://adventofcode.com/2020/day/13

    Args:
        bus_notes_file (str): Bus notes as user input

    Returns:
        int: wait time * bus id
    """
    with open(bus_notes_file, 'r') as f:
        lines = f.readlines()

    start_time = int(lines[0])
    bus_ids = lines[1].split(',')
    bus_ids = [int(x) for x in bus_ids if x != 'x']
    wait_times = [x - start_time%x for x in bus_ids]
    wait_times = dict(zip(bus_ids, wait_times))
    min_bus_id = min(wait_times, key=wait_times.get)
    min_wait_time = wait_times[min_bus_id]
    
    return min_wait_time*min_bus_id


def question_25(public_key_card: int, public_key_door: int):
    """This function computes encryption key of a crypto code given public keys
keys of two interfaces and further information as provided in https://adventofcode.com/2020/day/25

    Args:
        public_key_card (int): Public key of card
        public_key_door (int): Public key of door

    Returns:
        int: Common encryption code
    """

    key_value = 1
    subject_number = 7
    loop_size_card = 0
    while key_value != public_key_card:
        key_value = key_value*subject_number
        key_value = key_value%20201227
        loop_size_card += 1

    loop_size_door = 0
    key_value = 1
    while key_value != public_key_door:
        key_value = key_value*subject_number
        key_value = key_value%20201227
        loop_size_door += 1

    encryption_key = 1
    for i in range(loop_size_card):
        encryption_key  = encryption_key * public_key_door
        encryption_key  = encryption_key%20201227

    return encryption_key


def question_12(nav_instructions_file: str):
    """Given navigation instructions, this function simulates ship navigation as
per interpretation rules. The function solves with following question in the
coding challenge: https://adventofcode.com/2020/day/12

    Args:
        nav_instructions_file (str): Navigation file

    Returns:
        int: Manhattan distance from point of origini
    """

    # Read navigation instructions
    with open(nav_instructions_file, 'r') as f:
        lines = f.readlines()
    
    horizontal_distance = 0
    vertical_distance = 0
    direction = 3 # 0 means North, 3 Means East, 6 means South, 9 means West
    # Start navigation 
    for line in lines:
        line = line.rstrip('\n')
        if line[0] == 'F':
            move_step = int(line[1:])
            if direction == 3:
                horizontal_distance += move_step
            elif direction == 6:
                vertical_distance -= move_step
            elif direction == 9:
                horizontal_distance -= move_step
            else:
                vertical_distance += move_step
        elif line[0] == 'N':
            move_step = int(line[1:])
            vertical_distance += move_step
        elif line[0] == 'S':
            move_step = int(line[1:])
            vertical_distance -= move_step
        elif line[0] == 'E':
            move_step = int(line[1:])
            horizontal_distance += move_step
        elif line[0] == 'W':
            move_step = int(line[1:])
            horizontal_distance -= move_step
        elif line[0] == 'R':
            chg_dir = int(line[1:])/90
            direction = (direction + 3*chg_dir)%12
        elif line[0] == 'L':
            chg_dir = int(line[1:])/90
            direction = (direction - 3*chg_dir)%12
    manhattan_dist = abs(horizontal_distance) + abs(vertical_distance)
    return manhattan_dist

