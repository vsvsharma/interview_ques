"""
Problems URL(https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)
"""
def gradingStudents(grades):
    # Write your code here
    res=[]
    for grade in grades:
        if grade>=38:
            mod5= grade % 5
            
            if mod5>=3:
                grade += (5-mod5)
        res.append(grade)
    return res