# 덧셈, 뺄셈, 곱셈, 나눗셈 프로그램
def add_subtract_multiply_divide(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "0으로 나눌 수 없습니다"

if __name__ == "__main__":
    a = int(input("첫 번째 숫자를 입력하세요: "))
    b = int(input("두 번째 숫자를 입력하세요: "))
    
    result_sum, result_diff, result_mul, result_div = add_subtract_multiply_divide(a, b)
    
    print(f"합: {result_sum}, 차: {result_diff}, 곱: {result_mul}, 나눗셈: {result_div}")
    
    print("두번째 브랜치")