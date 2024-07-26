"""MyMath"""
import math
def main():
    """main"""
    result1 = (math.sin(math.radians(90)) + math.sin(math.radians(60))**2) /\
    (math.cos(math.radians(245**2)) + math.cos(math.radians(45 + 135)))
    result2 =  (math.factorial(16) * math.factorial(4)) / math.factorial(8)
    result3 = (15 + 25) / (math.sqrt((25 - 12)**2 + (12 - 15)**2))
    result4 = math.log10(1234**4)
    result5 = (math.log(4234, 5) + math.log(8191, 2) + 71 * math.log10(156154)) /\
    (math.log(777, 7) - math.log(888, 8) - math.log(999, 9))
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
main()
