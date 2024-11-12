from calc import *
calc2 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
def exec_program(input_list):
    if is_program(input_list):
        exec_statments(program_statements(input_list))
def exec_statments(input_list):
    if empty_statements(input_list):
        return None
    exec_statment(first_statement(input_list))
    exec_statments(rest_statements(input_list))
def exec_statment(input):
    if input[0] == "if":
        exec_if(input)
    if input[0] == "print":
        exec_print(input[1])
def exec_print(input):
    print(input)
def exec_if(input):
    if_statment = input[1]
    if if_statment[1] == "==" and if_statment[0] == if_statment[2]:exec_statment(input[2]) 
    elif if_statment[1] == "<" and if_statment[0] < if_statment[2]:exec_statment(input[2]) 
    elif if_statment[1] == ">" and if_statment[0] > if_statment[2]:exec_statment(input[2]) 
    else: exec_statment(input[3])


exec_program(calc2)