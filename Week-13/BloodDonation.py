"""Blood"""
def main(age,weight,times,doc):
    """blood"""
    if age > 70 or age < 17:
        return "No"
    if weight < 45:
        return "No"
    if not times and age>55:
        return "No"
    if age==17 and doc=="False":
        return "No"
    if 60<=age<=70 and doc=="False":
        return "No"
    return "Yes"
def ans():
    """Find Ans"""
    age = int(input())
    weight = int(input())
    times = int(input())
    doc=""
    if age==17 or 60<=age<=70:
        doc=input()
        print(main(age,weight,times,doc))
    else:
        print(main(age,weight,times,doc))
ans()
