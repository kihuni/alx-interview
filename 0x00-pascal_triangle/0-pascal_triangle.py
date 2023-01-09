"""Create a function def pascal_triange(n) that returns a list of lists of integers"""

def pascal_triangle(n):

    """check if the input is less than or equal to 0, if it's, empty list is returned"""
    if n<=0:
        return []

    """otherwise the function initializes a list called lists with n numbers of 0s"""
    lists = [0]*n

    """iterate through n numbers"""
    for i in range(n):

        """On each iteration, a new list is called new_row is created and initialised with `i+1 0s"""
        new_row = [0]*(i+1)

        """fill first index with 1"""
        new_row[0] = 1

        """fill last index with 1""" 
        new_row[len(new_row)-1] =1

        """Inner iteration from 1 to i-1"""
        for j in range(1, i+1):

                """Calcuate the sum of two numbers  in the previous row"""      
                a = lists[i-1][j]
                b = lists[i-1][j-1]

                """assigns the sum to the current potion in new_row"""
                new_row[j] = a+b

        """Finally assigns new_row to the current position in the lists"""
        lists[i] = new_row
        """return lists"""
    return lists

