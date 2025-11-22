#1: Area of a circle
print("This is the circle area calculator!")
radius = input("What is the radius of the circle? ")
radius_str = float(radius)
area = 3.14 * (radius_str ** 2)
area_str = str(area)
answer = "This is the area of your circle: " + area_str
print(answer)

#2:Expression solver
def solve_expression(a:int, b:int):
    result = (a-b) + (a*b)
    return result
def main():
    print("This is the expression solver for (a-b)+(a*b)!")
a_str = input("What is the value for a?")
b_str = input("What is the value for b?")
a = int(a_str)
b = int(b_str)
final_answer = solve_expression(a,b)
resulting_string = str(final_answer)
print("The answer is: " + resulting_string)

#3:ASCII art
image_a = """
      /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
"""
image_b = """
 _________         .    .
(..       \_    ,  |\  /|
 \       O  \  /|  \ \/ /
  \______    \/ |   \  / 
     vvvv\    \ |   /  |
     \^^^^  ==   \_/   |
      `\_   ===    \.  |
      / /\_   \ /      |
      |/   \_  \|      /
 snd         \________/
"""
print("Welcome to my ASCII museum!")
picture = input("Do you want to see image a or b? ")
if picture == 'a':
    print("Here is a picture of a fish" + image_a)
elif picture == 'b':
    print("Here is a picture of a shark" + image_b)