# Jamie's coursework template

# Nabeel Alkindy, H00287325                           <--- so we know who you are
# F28PL Coursework 2, Python                         <--- sanity check

# Deadline is 17 October 2020 (end week 5)

# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.

# To do this coursework, FORK the repo on gitlab and work with that fork.  Any questions, don't guess: ask.

# This coursework is live exam material so KEEP YOUR ANSWERS PRIVATE.  

################################################################################
# Question 1   <--- Yes, so we know what question you think you're answering

"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice 
versa. You may use the python methods real and imag without comment, but not complex 
(use j directly instead).
"""
#  <--- always have the question under your nose

#####################################
# Question 1a


def cadd(c1, c2):
    # uses the index to retrieve the value of c1 and c2, adds them together, assigns each to a variable, and the 'add' variable outputs them as a tuple
    a = (c1[0] + c2[0])
    b = (c1[1] + c2[1])
    add = a, b
    return add
    

def cmult(c1,c2): 
    # same thing as earlier but this is the formula for multiplication of complex numbers   
    a = ((c1[0]*c2[0])-(c1[1]*c2[1]))
    b = ((c1[0]*c2[1])+(c1[1]*c2[0]))
    mult = a, b
    return mult




#####################################
# Question 1b

def tocomplex(x1, y1):
    # takes the value of x1 and adds it to y1 multiplied by 1j. this is done because we need y1 to be represented as a complex number
    tocomp = x1 + (1j*y1)
    return tocomp  
    



def fromcomplex(c):
    # takes the tuple 'c' and then specifies the left side as real and right as imaginary
    comple = (c.real, c.imag)
    # these are then assigned to their own variables to then be returned out as a tuple
    rea = c.real
    ima = c.imag
    fromcomp = rea, ima
    return fromcomp

# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2
 

"""
2a. Using def, write iterative functions 
* seqaddi and 
* seqmulti 
that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[~1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqaddlc and seqmultlc.


"""

#####################################
# Question 2a


def seqaddi(l1, l2):
#make an empty list 'addi'
    addi = []
    # 'for' loop using the zip function that takes the first element of l1 and pairs it with the first element of l2 and this repeats for the remaining elements
    for a, b in zip(l1, l2):
        #takes the list we made and appends the sum of the two elements used earlier to the list
        addi.append(a+b)
        #returns the list
    return addi
    




def seqmulti(l1, l2): #exact same thing as earlier but we multiply the pairs of elements together instead of adding
    prod = []
    for a, b in zip(l1, l2):
        prod.append(a*b)
    return prod


#####################################
# Question 2b


def seqaddr(l1, l2):
    # used to control the final result 
    if not len(l1):
        return l2
    elif not len(l2):
        return l1
    # recursively adds pairs of elements from 'l1' and 'l2'. We can see its recursion as it calls itself.
    return ([l1[0] + l2[0]] + seqaddr(l1[1:], l2[1:]))


def seqmultr(l1, l2):
    pass


#####################################
# Question 2c


def seqaddlc(l1,l2): #uses a 'for' loop along with list comprehension 
    addc = [x + i for x, i in zip(l1, l2)] # 'zip' pairs the elements of l1 with the elements of l2 and adds them together and automatically assigns it to the list 'addc'
    return addc


def seqmultlc(l1,l2):
    multc = [x * i for x, i in zip(l1, l2)] #same thing as earlier but multiply the elements instead of adding
    return multc




# END ANSWER TO Question 2
################################################################################

################################################################################
# Question 3


"""
Write functions
● ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
● matrixshape
This should input an intmatrix and return the size of the matrix, which is the number of rows and the number of columns 
(traditionally the number of rows is given first, but if you have done it the other way around that’s fine; 
just make sure to clearly explain your code). 

● matrixadd
Matrix addition, which is simply pointwise addition.
● matrixmult
Similarly for matrix multiplication.
You do not need to write error-handling code, e.g. for the cases that inputs do not represent
matrices or represent matrixes of the wrong shapes; so for instance your matrixshape may 
assume that the argument has successfully passed the test ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.  Don't use zip.
"""


def ismatrix(m):
    #assigns length of the list within the first element of 'm' to variable 'length'
    length = len(m[0]) 

    # 'if' statement to check if all the lengths the same because we need this condition to be satisfied in order for it to be a matrix
    if all(len(x) == length for x in m[1: ]):
        return True
    
def matrixshape(m): 
    # takes length of list 'm' for number of rows and assigns to variable 'mat_row'
    mat_row = len(m)

    # takes length of the first element (list) within list 'm' for number of colummns and assigns to variable 'mat_col'
    mat_col = len(m[0])

    # matrix shape is displayed as 'no. of rows, no. of columns' and assigned to variable 'shape' which returns output as tuple
    shape = mat_row, mat_col
    return shape


def matrixadd(m1,m2):
    # adds columns of matrix m1 and m2 using zip to pair them together and a 'for' loop and returns output as its own matrix (list)
    add_col1 = [a+b for a,b in zip(m1[0], m2[0])]
    add_col2 = [c+d for c,d in zip(m1[1], m2[1])]
    matrix_sum = [add_col1, add_col2]
    return matrix_sum

    



def matrixmult(m1,m2): # this one is challenging as the matrices are different dimensions
    x = 0
    ans =[[x for i in range(len(m2[0]))] for j in range(len(m1))] # we have to take the range of the column m2 and the range of the rows in m1
    for i in range(len(m1)):  # then iterate using a 'for' loop through the rows of m1
        for j in range(len(m2[0])):  # then iterate through the columns of m2
            for k in range(len(m2)):   # then iterate through the rows of m2
                ans[i][j] += m1[i][k] * m2[k][j]    #we use the shorthand '+=' to signify ans = ans + (m1*m2) (This is done with all the iterations in place of 'i, j, and k')
    return ans # returns the list 'ans'


################################################################################


###############################################################################
# Question 4


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
● Mutable vs immutable types. Give at least two examples of each, with explanation.
● Integer vs float types.
● Assignment = vs equality == vs identity is.
● The computational effects of a call to list on an element of range type, as in
list(range(5**5**5)).
● Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""

"""
Essay:

Data representation in Python is exactly what it says on the tin, it is how data is represented. When we look at all the ways that data can be represented,
one question has to be asked; "Mutable, or Immutable". Each of those two data types are uniquely useful in their own way. 'Mutable' means that the object that 
is a part this data type can be altered after being written. Whereas 'Immutable' is the inverse of that, once the object is created, the information within cannot be 
changed. A list such as [d, e, f] and a set {x, y, z} are both mutable, because once created, you are able to change any of the information within freely. A string: 
"Nabeel Alkindy" or a simple tuple such as (3, 5, 7, 9) are both immutable because the information cannot be modified. Now onto integer and float. These are also quite 
simple: an integer(int for short) is just a whole number (it can be positive or negative) with no decimal point. A float is a real number that has a decimal point.

Assignment and equality generally get mixed up but the difference is relatively easy to understand. Assignment is when you assign 'item a' to 'item b' and you use the symbol "=".
An example: If I say that 'color = blue', I gave the variable 'color' a value of 'blue'. If I were to print this variable, it would now come out as 'blue'. Equality, on the other
hand, does not assign any new value, but instead multiple values equivalent (uses the symbol '=='). What this means is that if we have 2 variables with their own respective values
'a = 10' and 'b = 12', you can use equality to do a number of things such as check if a == b (if a is equivalent to b, return true), or you could use it to make one equivalent to 
the other: a == b (a is now the same value of b). Identity is a characteristic that divides objects into their own respective categories. It can be thought of as a name tag because 
if we write '1045', Its identity is that it is an integer, "Heriot Watt" is a string, '12.5556' is a float, etc. It is used so that you can identify what type an object belong to.
The 'is' operator is another thing that gets confused with equality. 'Is' is an operator that checks if 'operand a' and 'operand b' refer to the same object. Ex: itemA is itemB, 
this will return as false because they are different loacations of memory and therefore are two different objects.

The computational efects of calling a list 'list(range(5**5**5)), it takes a large number of resources to compute such a wide range. There is also a chance that Python wont unpack the 
list which would make things even more complicated. Slicing in python is essentially like a knife that lets you separate the elements of a sequence and create a new sequence. If you 
take the string "Python" and slice it [1:5], the new string becomes "ytho" because it only takes the elements in the 1 position till the 5 position.

"""



# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5
#print()
#print('Question 5')

"""
Write a general encoding function encdat that will input an integer, float, complex number, or
string, and return it as a string.

So
• encdat(-5) should return '-5'
• encdat(5.0) should return '5.0'
• encdat(5+5j) should return '5+5j' (not '(5+5j)'; see hint below).
• encdat('5') should return '5'


"""


def encdat(dat):
        pass

# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
An encoding f of numbers in lists is as follows:
• f(0) = [] (0 maps to the empty list)
• f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.
"""


def fenc(i):
    pass


def fdec(l):
    pass


# END ANSWER TO Question 6
################################################################################


###############################################################################
# Question 7


"""
Implement a generator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code
 ...
in an endless cycle. If you can’t manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
This does not mean the whole infinite datastructure is in memory at any time (which is 
impossible for a machine with finite memory), but for any finite but unbounded number of calls 
to next your generator behaves as if it were the infinite datastructure illustrated above.
"""


def cycleoflife():      
    a = True            # This is just the value that will never change so that the 'while' loop can loop infinitely
    pattern = []        # create an empty list
    while a is True:    # infinite 'while' loop due to the constant 'True" condition
        yield "eat"     # yields the 3 things we need
        yield "sleep"
        yield "code"
        pattern.append  # appends them to our previously created empty list
    return pattern      # returns the list as an infinitely repeating list

   
    




# END ANSWER TO Question 7
################################################################################


#################################################################################
# Question 8

"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function gendat that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

Do not use str.  You may find it useful to consider isinstance or the following code fragment
   type(5) == type([]) 
"""


def gendat(datum):
   pass


# END ANSWER TO Question 8
################################################################################


##########################################################
# Question 9

"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
as a Python generator eratosthenes such that if we assign
x = eratosthenes()
then repeated calls to
next(x)
return the primes, starting from 2.
""" 

def eratosthenes():
    pass


# # For reference, here is an implementation of the sieve of Eratosthenes, 
# # whose argument acts as a bound on the returned generator (40000, by default). 
# # Your answer should take no argument, and should return an unbounded generator.
# def eratosthenes(z=40000):
#      # create an array of true values the size of z
#      A = [True] * z
#      # iterate over each value to z squared
#      for x in range(2, int(z ** 0.5)):
#          # if A[x] has a true value
#          if A[x]:
#              # iterate over a range starting from x*2 ending at z in jumps of x
#             for z in range(x * 2, z, x):
#                  # set anything in the range to false
#                 A[z] = False
#      # iterate over the array
#      for y in range(2, len(A)):
#          # if a value is true that index is a prime number
#          if A[y]:
#              # yield the current iterator location as it is a prime
#             yield y




# END ANSWER TO Question 9
################################################################################


################################################################################
# Question 10

"""
Following on from Question 3, invertible matrices are explained here:
   https://en.wikipedia.org/wiki/Invertible_matrix
   https://en.wikipedia.org/wiki/Minor_(linear_algebra)#Inverse_of_a_matrix

Write and test an algorithm to calculate the inverse of an n x n matrix (i.e. a square matrix) using Cramer's rule, for n>=1.

* Your answer should include helper functions (and tests for them) to calculate the
* *determinant*,
* *minors*,
* *cofactors*, and
* *adjoint* of a matrix, all of which are described here:
   https://en.wikipedia.org/wiki/Minor_(linear_algebra)
   https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
* Your code will be marked on clarity as well as correctness.  Code that is "correct" but unreadable, is bad code and therefore may get bad marks.

Writing, documenting, and testing helper functions is generally good practice, and you will likely find other helper functions are required, such as for matrix transpose, computing a sub-matrix, multiplying a matrix by a scalar, and perhaps others.  

Whatever you do, just make sure you explain what you're doing and why. 
"""

def matrixdeterminant(m):
    pass


def matrixminors(m):
    pass


def matrixcofactors(m):
    pass


def matrixadjoint(m):
    pass


def matrixinverse(m):
    pass


# END ANSWER TO Question 10
################################################################################


###############################################################################
# Question 11

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""


"""
Here's a very brief example answer to Q11 above where "Python" is replaced by "Eggs".  Enjoy:

A chicken is cheap to keep, can produce an egg a day, and eggs come prepackaged and naturally resist spoilage.  For instance, eggs come out of a chicken with a natural antibacterial coating on their shells so that they can be stored at room temperature, which keeps transport costs low --- in the US eggs are washed, which stops them smelling of chickens' bottoms but removes this coating, which is why US eggs require refrigeration and UK eggs don't. 
[note now this combines *factual* and *technical* elements; an awareness of the egg as a thing, but also of supply chain economics, food safety, and a nice factoid which really proves I went beyond the first page of Google results -mjg] 

Eggs are nutritious, tasty, and filling.  They are easy to cook and are culturally well-established in the UK.  A proper superfood, in fact.  

Eggs do have dangers: when improperly handled they can carry salmonella.  More information at [hyperlink].  Eggs can crack, and then spoil quickly.  Occasionally eggs go invisibly bad, or the embryo incubates prematurely (nowadays, sophisticated scanning machines eliminate these from the food chain). 

Eggs also have applications in vaccine development, and unfortunately also in biological warfare as incubators for germs, and [more stuff here -mjg].

For the future, [stuff about vegans, changes in food preferences, vat-grown protein, environmental costs of keeping chickens, etc etc].

[I could keep this up for pages, I won't: we've gone beyond the shell of an answer, we've cracked it, and if we allow our enthusiasm to egg us on then it would over-egg the pudding and we'd get egg on our faces for writing a not-eggsactly-concise answer:  we stuffed enough eggs in this basket and should stop, before the reader finds it eggscrutiating.   
Now your turn please, with "Python" instead of "Egg".  Make me proud.  -mjg]
""" 

"""
Essay:
    Python is easily one of the most popular programming languages in the world. Before I get into why, let us go into its uses. Python is a high-level programming language that is quite powerful when implemented 
to its full potential. Today, Python is used in Web development as a framework or a sort of 'back bone'  because it aids in the sites "security, scalabilty, and convenience"[1]. In the game development field,
Python is used for its ability to create prototypes quite quickly when compared to other languages, however unlike other languages, python has limitations when it comes to performance. This isn't as big of a 
hindrance as it may seem because some popular games such as Pirates of The Caribbean were created using Python, utilising many of the libraries that Python has to offer. In this area, Python doesn't excel at
making amazing games like other languages such as the industry standard that is C# or C++ but that doesn't take away from its capabilities. A third really popular use that may be surprising is the use of Python 
in Artificial Intelligence. One reason you would pick Python even though it offers a lower amount of code than its fellow competitors is: It has its own dedicated set of libraries that make computational 
tasks a breeze. You have access to NumPy for scientific and/or mathematical operations, SciPy for more advanced computational needs, and most importantly, PyBrain that is a library completely dedicated to 
machine learning and Artificial Intelligence. Other reasons include: having a huge userbase which means that its a very tightly knit community of Python developers that offer support online, as well as being
platform independent, which makes it very flexible for development across numerous platforms.

    Now that we established its uses, it is becoming more apparent as to why Python has gained such a rise in popularity. As mentioned earlier, it is a high level programming language which means its capable of 
dealing with "variables, arrays, objects, complex arithmetic or Boolean expressions"[2]. Furthermore, some people see simple as a synonym for basic, Python is an example of why this is wrong. Python's simplicity
is one of its greatest strengths as it is extremely productive, allowing the developer to create whatever they please without needing as much code as, for example, Java. Python's clear and concise coding experience 
also lends well to why it is a very beginner-friendly language. Any individual wanting to learn the language can easily understand a good portion of the code because of how similar the syntax is to English. I previously
mentioned that Python has some performance limitations, in a world where time is money, the speed that a task can get done is way more important than how complex the task is. 

    When you take a look at how Python has kept its massive popularity over the years, the future looks quite bright if the language is maintained as regularly as it has been. My speculation for the evolution, at its most 
basic level, will be that all of its current issues will be addressed. Python's game development library should be looked into as to make it on-par with the likes of the industry giants such as Unity and Unreal. 
this will enable it to dominate in yet another field. In addition to the game library, if Python were to improve its optimisation, such as fixing the performance limitations without compromising its advantage of speed,
then it would truly become a tool not to be reckoned with.


References:
[1] https://www.edureka.co/blog/python-applications/#apps
    https://gamingshift.com/is-python-good-for-game-development/
[2] https://www.cuelogic.com/blog/role-of-python-in-artificial-intelligence#:~:text=Python%20has%20Prebuilt%20Libraries%20like,the%20best%20languages%20For%20AI.&text=Python%20is%20the%20most%20flexible,between%20OOPs%20approach%20and%20scripting.
    https://medium.com/@trungluongquang/why-python-is-popular-despite-being-super-slow-83a8320412a9#:~:text=First%20and%20foremost%20reason%20why,languages%20like%20C%2B%2B%20and%20Java.&text=The%20Python%20features%20like%20one,of%20code%20in%20other%20languages.



"""

# END ANSWER TO Question 11 
###############################################################################
