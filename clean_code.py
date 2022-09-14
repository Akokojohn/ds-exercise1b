from typing import List, Optional, Union   #for hinting a list. use optional
"""
Clean code rules
-correct function names that describe what the function does
-documentation
-type annotation: type hinting
  Union= a or b or c
  Optional = a or None
-single responsibility  
"""

def convert_to_celcius(farheit: Union[float, int]) -> float:  #for Union
#def convert_to_celcius(farheit: float) ->:    #to use hint we use farheit: int. type int
    return (farheit-32)*5/9

convert_to_celcius(4)

def welcome_to_class(name : string) -> None:
    print("welcome")

class StudentCase
    pass

class calculator:
    """
        A class that simulates the scientific calculator

        :parameter
        number - an integer that you want to perform action on. DEFAULT = 0
    """
    def __init__(self, number:float = 0) ->None:#-> IS CALLED TYPE HINTING
        self.number = number
        self.rst = 0

    def add(self, num = 0):
        self.rst+=num

    def multiply(self,num:int = 0):



class AWSConnection:
    pass

cal = Calculator()

def get_active_account(user_id:str = None) -> List:
    if user_id == None:
        return [] # return list of all active accts
    acct.append(user_id)

    return acct

    return [user_id]# return just 1 user active acct

def get_account_info(user_id):
