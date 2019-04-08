#########################
#待优化
#1. 处理空格
#2. 处理二位以上数字
#3. 处理负数
######################
def str_to_list(input_string):
    
    #完成:
    #1.去除字符串中的空格
    #2.将输入字符串转化成列表
    
    no_space_string = int_string.replace(' ', '') # 去除空格
    input_list = str(no_space_string)
    return input_list
        
'''


def strip_parentheses(expression):
    """
    递归地取出括号中的表达式,并计算出结果
    """
    left_index, right_index = expression.index('('), expression.index(')')
    expression = expression[left_index: right_index+1]
    
    #print(expression)
    if expression.count('(') > 1:
      
        return strip_parentheses(expression[1:])
    else:
        #print(right_index)
        #print(expression.index(')'))
        return expression[1: len(expression)-1]
        


#def compute_expression(expression):
    '''
    使用第一版中无符号计算器来计算结果
    '''
    #retur n result 返回值是个字符串
#    pass 


def result_replace(input_string):
    rep = strip_parentheses(input_string)
    res = compute_expression(rep)
    a = input_string.replace('(' + rep + ')', res)
    if a.count('(') >= 1:
        return result_replace(a)
    else:
        for i in a:
            if i in ['+', '-', '*', '/']:
                return compute_expression(a)
        return a   
                
                
        
 
# 第一版计算器
class Stack:

  def __init__(self):
    self.data = []

  def push(self, ele): # add
    self.data.append(ele)

  def pop(self): # remove
    return self.data.pop()

  def __len__(self):
    return len(self.data)


class Add:
  def compute(self, left, right):
    return left + right

class Sub:
  def compute(self, left, right):
    return left - right

class Mul:
  def compute(self, left, right):
    return left * right

class Div:
  def compute(self, left, right):
    return left // right
    

def compute_expression(string):
  '''
  1 + 1 * 2

  operant_stack  1, 1, 2
  operator_stack +, *           A a =int("1") B "+" if +  A int("1")   A

  operant_stack  2 2
  operator_stack *

  operant_stack  4
  operator_stack
  '''

  operant_stack = Stack()  # 算子
  operator_stack = Stack() # 运算符
  
  operators = {
    "+": Add(),
    "-": Sub(),
    "*": Mul(),
    "/": Div()
  }

#解析 parsing
  for char in string[::-1]:
    if char in operators:
      operator_stack.push(operators[char])
    elif char != " ":
      operant_stack.push(int(char))

# 解释 interpretation
  while len(operator_stack) > 0:
    a1 = operant_stack.pop()
    a2 = operant_stack.pop()
    operator = operator_stack.pop()
    operant_stack.push(operator.compute(a1, a2))

  if len(operant_stack) != 1:
    raise Exception("operant stack is not empty:"+str(operant_stack))

  result = operant_stack.pop()
  return str(result)   
    
    
    




if __name__ == '__main__':
    string = '(1+(2*3))'
    string_1 = '1+((2*1)-(1+2)+3)'
    string_2 = '(3+(2*2)-(7/5))'
    print(result_replace(string))
    print(result_replace(string_1))
    print(result_replace(string_2))
