from operator import add, mul, sub, truediv
from typing import List, Optional, Union

ops = {"+": add, "-": sub, "*": mul, "/": truediv}


def _split_if_string(string_or_list: Union[List[str], str]) -> List[str]:
    return string_or_list.split() if isinstance(string_or_list, str) else string_or_list


def prefix_evaluate(prefix_equation: Union[List[str], str]) -> Optional[int]:
    if not prefix_equation:
        return None
    prefix_equation = _split_if_string(prefix_equation)
    value_stack = []
    while prefix_equation:
        el = prefix_equation.pop()
        if el not in ops:
            value_stack.append(int(el))
        else:
            r_val = value_stack.pop()
            l_val = value_stack.pop()
            operation = ops[el]
            value_stack.append(operation(r_val, l_val))

    return value_stack[0]


def to_prefix(equation: str) -> str:  
    prior = {'+': 1, '-': 1, '*': 2, '/': 2} 
    total = [] 
    stack = [] 
    
    for el in equation.split()[::-1]: 
        if el not in '+-*/': 
            if (el != '(') and (el != ')'): 
                total.append(el) 
            if el == '(': 
                while stack and stack[-1]!=')':  
                    total.append(stack.pop()) 
                stack.pop() 
            if el == ')':  
               stack.append(el)    
        if el in '+-*/': 
            while stack and stack[-1]!=')' and prior[el]<=prior.get(stack[-1], 0):  
                total.append(stack.pop()) 
            stack.append(el) 
            
    while stack: 
        total.append(stack.pop()) 
 
    return " ".join(total[::-1]) 

def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
