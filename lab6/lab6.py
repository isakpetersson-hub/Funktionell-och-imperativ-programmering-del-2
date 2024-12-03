from calc import *
calc2 = ['calc', ['set', 'x', 7],['set', 'y', 12],['set', 'z', ['x', '+', 'y']],['print', 'z']]

calc3 = ['calc', ['read', 'p1'],['set', 'p2', 47],['set', 'p3', 179],['set', 'result', [['p1', '*', 'p2'], '-', 'p3']],['print', 'result']]

calc4 = ['calc', ['read', 'n'],['set', 'sum', 0],['while', ['n', '>', 0],['set', 'sum', ['sum', '+', 'n']],['set', 'n', ['n', '-', 1]]],['print', 'sum']]

def exec_program(input_list):
    if is_program(input_list):
        variable_table={}
        exec_statments(program_statements(input_list),variable_table)
        return variable_table
def exec_statments(input_list,var_table):
    if not empty_statements(input_list):
        exec_statment(first_statement(input_list),var_table)
        exec_statments(rest_statements(input_list),var_table)
def exec_statment(input,var_table):
    if is_repetition(input):
        exec_while(input,var_table)
    if is_selection(input):
        exec_if(input,var_table)
    if is_output(input):
        exec_print(input_variable(input),var_table)
    if is_assignment(input):
        exec_assignments(input,var_table)
    if is_input(input):
        exec_read(input,var_table)
def exec_print(input,var_table):
    if input in var_table:
        value = exec_assignments(input,var_table)
        print(value)
    else:
        print(input)
def exec_if(input,var_table):
    input_statment = selection_condition(input)
    if_statment = selection_condition(input_statment)
    cond_left = condition_left(input_statment)
    cond_right = condition_right(input_statment)
    if if_statment == "==" and cond_left == cond_right:
        return exec_statment(selection_true_branch(input),var_table)
    if if_statment == "<" and cond_left < cond_right:
        return exec_statment(selection_true_branch(input),var_table)
    if if_statment == ">" and cond_left > cond_right:
        return exec_statment(selection_true_branch(input),var_table)
    else: return exec_statment(selection_false_branch(input),var_table)
def exec_assignments(input,var_table):
    if is_assignment(input):
        if is_binaryexpr(assignment_expression(input)):
            var_value = exec_binary_expression(assignment_expression(input),var_table)
        else:
            var_value=assignment_expression(input)
        var_name=assignment_variable(input)
        var_table[var_name]=var_value
    else:
        return var_table[input]

def exec_binary_expression(input, var_table):
    binary_op = binaryexpr_operator(input)
    left = binaryexpr_left(input)
    right = binaryexpr_right(input)
    if isinstance(left,list):
        left = exec_binary_expression(left,var_table)
    elif left in var_table:
        left = var_table[left]
    if isinstance(right,list):
        right=exec_binary_expression(right,var_table)
    elif right in var_table:
        right = var_table[right]
    if binary_op=="+":
        return left+right
    elif binary_op=="-":
        return left-right
    elif binary_op=="*":
        return left*right
    elif binary_op=="/":
        return left/right
    
def exec_read(input_list,var_table):
    user_input = input()
    try:
        var_table[input_list[1]]=int(user_input)
    finally:ValueError("Wrong input")

def exec_while(input,var_table):
    cond = repetition_condition(input)
    statement = repetition_statements(input)
    while exec_condition(cond,var_table):
        exec_statments(statement,var_table)

def exec_condition(input,var_table):
    op=condition_operator(input)
    left = condition_left(input)
    right = condition_right(input)
    if isinstance(left,list):
        left = exec_statment(left,var_table)
    elif left in var_table:
        left = var_table[left]
    if isinstance(right,list):
        right=exec_statment(right,var_table)
    elif right in var_table:
        right = var_table[right]
    if op ==">":
        return left>right
    elif op =="<":
        return left<right
    elif op=="=":
        return left==right
    else: return False
print(exec_program(calc3))