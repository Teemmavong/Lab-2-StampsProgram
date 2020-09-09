"""
start
get number of sheets
sheets / 5
round answer to next number
output the result
end
"""
import math

# input: sheet
def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer)
    print("sheet is : ", sheet)
    print("the answer is: ", answer)
    print("rounded is : ", rounded)
    print("========================")
    return rounded

output = calculate(1000)
print("the return statement is: ", output)
