"""Safe"""
def rotate_down(correct_text, lock_text):
    """rotate down"""
    rotations = 0
    while lock_text != correct_text:
        if lock_text >= 25:
            lock_text = -1
        rotations += 1
        lock_text += 1
    return rotations

def rotate_up(correct_text, lock_text):
    """rotate up"""
    rotations = 0
    while lock_text != correct_text:
        if lock_text <= 0:
            lock_text = 26
        rotations += 1
        lock_text -= 1
    return rotations

def main(correct, lock):
    """main"""
    total_rotations = 0
    for correct_char, lock_char in zip(correct, lock):
        correct_num = ord(correct_char) - 65
        lock_num = ord(lock_char) - 65
        if correct_num != lock_num:
            down_rotations = rotate_down(correct_num, lock_num)
            up_rotations = rotate_up(correct_num, lock_num)
            total_rotations += min(up_rotations, down_rotations)
    print(total_rotations)
main(input().upper(), input().upper())
