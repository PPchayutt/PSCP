"""EuclideanDistance2D"""
import math
def euclideandistance(q1, q2, p1, p2):
    """euclideandistance"""
    distance = math.sqrt((q1 - p1)**2 + (q2 - p2)**2)
    return distance

def main():
    """main"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    result = euclideandistance(q1, q2, p1, p2)
    print(result)
main()
