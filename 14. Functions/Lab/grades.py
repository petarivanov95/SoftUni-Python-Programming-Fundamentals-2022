grade = float(input())

def grader(n):
    if 2.00 <= n < 3.00:
        return 'Fail'
    elif 3.00 <= n < 3.50:
        return 'Poor'
    elif 3.50 < n < 4.50:
        return 'Good'
    elif 4.50 <= n < 5.50:
        return 'Very Good'
    elif 5.50 <= n < 6.00:
        return 'Excellent'



print(grader(grade))
