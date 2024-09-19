"""AlmostMean"""
def main():
    """main"""
    numbers = int(input().strip())
    students = []
    scores = []
    for _ in range(numbers):
        line = input().strip().split()
        student_id = line[0]
        score = float(line[1])
        students.append(student_id)
        scores.append(score)
    average_score = sum(scores) / numbers
    closest_id = None
    closest_score = -1
    for i in range(numbers):
        if scores[i] <= average_score and scores[i] > closest_score:
            closest_id = students[i]
            closest_score = scores[i]
    print(f"{closest_id}\t{closest_score}")
main()
