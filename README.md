# Assignment2
This assignment is a programming exercise and you will need to create file called assignment2.py and upload it to Gradescope for grading. Each of the following tasks needs to be implemented as methods in the class Assignment2. You are free to implement other methods in the class and/or use secondary .py file(s) for additional implementations. If you do so, you will need to submit them to Gradescope as well.

Note that there are strict requirements how class and methods should be named. If you fail to follow the requirement, your work will not be graded. Each task is worth 1 point.

You don't need to implement validation of the input parameters, we will always supply legitimate values in our testing scripts.

Make sure you implement each requested function as a class method! Unless it is explicitly asking for a static method, you must include self as a first special argument. For example, if asking to create a method foobar taking two arguments, you should write something like

class Assignment2:
    def foobar(self, first_argument, second_argument):
        # body of the method
Task 1 (Constructor)
Implement a constructor that accepts one parameter: year (type int). This parameter should initialize the similarly named class instance variable (hint: these would start with self.)

Task 2 (Age)
Implement method named tellAge. This method should accept a single argument: currentYear (type int).

The result of this method should be printing on the standard output the following line:

Your age is XXXX
Where XXXX is calculated birth year, based on the supplied currentYear argument and year from the class instance variable.

Task 3 (List)
Write a method named listAnniversaries that doesn't accepts arguments.

This method should return a list (note, unlike task 2, not to print, but return a list!) containing all 10-year anniversaries, assuming today is year 2022. For example, when running the following code

a = Assignment2(2000)
ret = a.listAnniversaries()
print(ret)
The output should be [10, 20].

And when running the following:

a = Assignment2(1991)
ret = a.listAnniversaries()
print(ret)
The output should be [10, 20, 30].

Task 4 (String Manipulation)
Write a method named modifyYear with the following specification:

Input parameters:

variable named n, type int: number to adjust list size
Return value should be a string, containing:

n times the first two characters in the text representation of the year (e.g., if year 2000 and n=5, then this part should be "2020202020")
odd positioned characters of text representation of year multiplied by n (if year is 2000 and n=5, then text representation is "10000" and you seelct odd characters, which is "100"; if year 1782 and n=3, then text representation is "5346" and you select "54".
For example,

a = Assignment2(1782)
ret = a.modifyYear(3)
print(ret)
should print 17171754.

Task 5 (Loop and Conditional statements)
Write a static method named checkGoodString with the following specification.  Note that static methods don't have self but must be annotated with @staticmethod.

Input parameters:

variable named string, type str
Return Value:

type bool: True if string has the following requirements

Is at least 9 characters long
Starts with lower case letter a-z
Contains only one number 0-9
For example,

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

ret = Assignment2.checkGoodString("foobar0more")
print(ret)
should print

False
True
Task 6 (Socket)
Write a static method named connectTcp that will create TCP IPv4 socket (AF_INET, SOCK_STREAM), connect to the specified host/port, closes the connection, and returns True if the connection was established correctly.

Input parameters:

variable named host: type str
variable named port: type int
Return value

type bool: True if TCP connection successfully established, otherwise False
You can test this method with any Internet service, for example:

retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
Note that Python 3 by default will throw an exception if you trying to connect and connection cannot be established. You will need to handle this case to return False as required by this task.
