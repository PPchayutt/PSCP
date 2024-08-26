"""BigFrame"""
def main():
    """main"""
    text = [input().rstrip() for _ in range(5)]
    max_length = max(len(line) for line in text)
    frame = "*" * (max_length + 4)
    print(frame)
    for line in text:
        print(f"* {line:<{max_length}} *")
    print(frame)
main()
