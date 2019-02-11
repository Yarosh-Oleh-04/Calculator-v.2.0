from typing import List, Any, Union

import stack_class

"""
>>> check('(())')
True
>>> check('(()())')
True
>>> check('(()()))')
False
>>> check('(()()))v')
False
>>> evaluate('2 2 2 * +')
6.0
>>> evaluate('9 3 3 * /')
1.0
>>> infix_to_postfix('5+3*6-3')
'5 3 6 * 3 - +'
>>> infix_to_postfix('4+2+4+2-3')
'4 2 4 2 3 - + + +'
>>> evaluate(infix_to_postfix('(637 + ((3 + 4) * 9)) / 70'))
10.0
>>> evaluate(infix_to_postfix('25 * 25 / (25 / 10)'))
250.0
>>> evaluate(infix_to_postfix('273 + 27 - 100 - 200'))
0.0
>>> evaluate(infix_to_postfix('((12 + 4 - 5 - 5) * 6 - 11) / 5'))
5.0
"""


def check(abc):
    stack = []
    for i in abc:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return stack == []


def evaluate(abc):
    try:
        stack = []
        abc = abc.split(' ')
        for i in abc:
            if i == '':
                pass
            elif i in '+-/*':
                right = float(stack.pop())
                left = float(stack.pop())
                if i == '+':
                    res = right + left
                elif i == '-':
                    res = left - right
                elif i == '*':
                    res = right * left
                elif i == '/':
                    res = left / right
                stack.append(res)
            elif i not in '+-/*':
                stack.append(i)
            else:
                raise Exception('ValueError')
        if len(stack) == 1:
            return float(stack.pop())
        else:
            raise Exception('IncorrectExpression')
    except:
        return ''


def infix_to_postfix(abc):
    stack = [' ']
    res = ''
    num = ''
    rec = ''
    t = 0
    for i in abc:
        if i == '(':
            t += 1
        if i == ')':
            t -= 1
        if t > 0:
            rec += i
        if i == ')' and t == 0:
            num = infix_to_postfix(rec[1:][:len(rec) - 1])
        if i not in '+-*/ ()' and t == 0:
            num += i
        if i in '+-*/' and t == 0:
            res += num + ' '
            if num == '' and i == '-':
                num = '-'
                i = ''
            else:
                num = ''
                if i == '-':
                    num = '-'
                    i = '+'
            while stack != [] and stack[len(stack) - 1] in '*/':
                res += stack.pop() + ' '
            stack.append(i)
    res += num + ' '
    while stack != [] and stack[len(stack) - 1] in '*/':
        res += stack.pop() + ' '
    while stack:
        res += stack.pop() + ' '
    return res[:len(res) - 3]


# if __name__ == "__main__":
#     import doctest
#
#     doctest.testmod()


def calc(abc):
    return evaluate(infix_to_postfix(abc))


# print(infix_to_postfix('((12 + 4 - 5 - 5) * 6 - 11) / 5'))
