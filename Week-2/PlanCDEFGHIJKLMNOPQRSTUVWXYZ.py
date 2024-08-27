""""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """main"""
    order = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if order == "Ascend":
        # เรียงตัวเลขจากน้อยไปมาก
        if num1 > num2:
            num1, num2 = num2, num1  # สลับ num1 กับ num2 ถ้า num1 มากกว่า num2
        if num2 > num3:
            num2, num3 = num3, num2  # สลับ num2 กับ num3 ถ้า num2 มากกว่า num3
        if num1 > num2:
            num1, num2 = num2, num1  # ตรวจสอบอีกครั้งแล้วสลับ num1 กับ num2 ถ้าจำเป็น
    elif order == "Descend":
        # เรียงตัวเลขจากมากไปน้อย
        if num1 < num2:
            num1, num2 = num2, num1  # สลับ num1 กับ num2 ถ้า num1 น้อยกว่า num2
        if num2 < num3:
            num2, num3 = num3, num2  # สลับ num2 กับ num3 ถ้า num2 น้อยกว่า num3
        if num1 < num2:
            num1, num2 = num2, num1  # ตรวจสอบอีกครั้งแล้วสลับ num1 กับ num2 ถ้าจำเป็น
    print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")
main()
