# 덧셈과 뺄셈 프로그램
def add_and_subtract(a, b):
    return a + b, a - b

if __name__ == "__main__":
    a = int(input("첫 번째 숫자를 입력하세요: "))
    b = int(input("두 번째 숫자를 입력하세요: "))
    
    result_sum, result_diff = add_and_subtract(a, b)
    
    print(f"합: {result_sum}, 차: {result_diff}")