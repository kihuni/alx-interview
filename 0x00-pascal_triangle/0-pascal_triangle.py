"""Create a function def pascal_triange(n) that returns a list of lists of integers"""

def pascal_triangle(n):
    """Create an array of list"""
    lists = []

    """iterate through n numbers"""
    for row in range(n):
        """if n <=0 return an empty list"""
        if n <=0:
            lists.append([])
        else:
            """return the first row"""
            new_row = [1]
        for i in range(row-1):
            new_row.append(lists[row-1][i]+lists[row-1][i+1])
            new_row.append(1)
            lists.append(new_row)
        return lists

