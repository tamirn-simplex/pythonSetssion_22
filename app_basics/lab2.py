from commands.constants import msg_dic
import commands.constants as con


def get_user_input() -> tuple:
    """
    Getting from user two number for range.
    Returns:tuple of start and end numbers

    """
    is_running = True
    msg = "initial_msg"
    start_num = 0
    end_num = 0

    while is_running:
        # Getting user input
        while not (start_num := input(msg_dic[msg].format("start"))).isnumeric():
            msg = "rep_msg"
        else:
            start_num = int(start_num)

        msg = "initial_msg"
        while not (end_num := input(msg_dic[msg].format("end"))).isnumeric():
            msg = "rep_msg"
        else:
            end_num = int(end_num)
        print("start num - {} and end num is {}".format(start_num, end_num))
        if end_num <= start_num:
            print("End number must be greater than start number (you silly :-)\nDo it again")
            continue
        is_running = False
    return start_num, end_num

"""
1.
As a user, I want to input a start number and an end number.
The program should print each number with the following exceptions:
 - For multiples of three print "Fizz" instead of the number.
 - for the multiples of five print "Buzz".
 - For numbers which are multiples of both three and five print "FizzBuzz".
Otherwise, print the number
"""


def fizz_buzz():
    start, end = get_user_input()
    for x in range(start, end):
        # print(x)
        if (x % 3) == 0 and (x % 5) == 0:
            print("FizzBuzz")
            continue
        if (x % 3) == 0:
            print("Fizz")
            continue
        if (x % 5) == 0:
            print("Buzz")
            continue
        print(f"x: {x} -- ")


"""
2. 
As a user, I want to be able to get the nth item in a fibonacci sequence by inputting the number I want, and the pair 
of numbers from which to start.
The output should also include the sum-total of all values in the sequence.
Example usage: 
fibo(10, 0, 1) # means, give me the 10th member of the fibo seq, starting from 0 and 1 
fibo(50, 13, 21) # means, give me the 50th member of the fibo seq, starting from 13 and 21  
"""


def my_fibo(n_element: int, first: int, second: int):
    """
    Getting the fibo number in the {n_element} position
    {first} - The fibo first element
    {second} - The fibo second element

    Return a tuple with the fibo element in {n_element} position and the sum of all fibo (up tp {n_element} position.
    """
    a, b = first, second
    count, fib_sum = 0, 0
    while count < n_element:
        fib_sum += a
        last = a
        a, b = b, a + b
        count += 1
    print(last, fib_sum)


# print("Get from constant {} for test".format(con.msg_dic["initial_msg"]))
# my_fibo(8, 1, 2)
fizz_buzz()
"""
3. (thinking exercise)
After completing the above, think. What did you learn from the implementations? (could be nothing)
Try to articulate it into a few sentences.
"""

'''
Since done the fizz_buzz and the fibo in the past, can't say get much of it beside of redoing.
The fibo was bit different for not printing the series but only the last item and calc the total sum.
fibo do not have to be like 0,1,2,3,5,13 ... 

Learn to use the walrus := !!!!
'''


"""
4. (research exercise)
FOR THIS QUESTION, GOOGLE (and any other information source) IS ALLOWED
Think about which questions you still have (regarding what we covered thus far, either in sessions or by self-learning).
(If you have questions about more advancded topics than what we have covered, just put them aside for now and we'll get 
back to it soon)
Write down 5 questions that you dont know the answer to (yet).
Try to answer each question on your own the best way that you can.
Write down the explanation in such way that will also be clear to other people.
Repeat the process until you have 5 questions that you are unable to answer on your own.
Partial answers also applies. Which means you will still need to find another question to add to the list.
Send me your list (either privately or in this group).
We will discuss the list you prepared together.
"""

'''

1. What is the difference between Python and IPython? (know you spoke of it, but it one of the things I missed (I think)

First to start use ipython -  pip install ipython
• The ipython (Interactive Python) provide some more interactive CLI REPL (e.g. type str. and double click getting more
 auto help completion).
• Linux commands works in ipython (do not works in regular python REPL.
• 

2. 2 vs 3 did we cover this?
    Not sure it really relevant.

# TODO     
3. Virtual Environments and pipenv still need to play with!!!! 
'''