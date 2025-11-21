# 파일 경로: my_project/main.py

# 1. 내가 만든 패키지 불러오기
import mypackage

# 2. 인사 함수 실행
mypackage.introduce()

# 3. 덧셈/뺄셈 함수 사용 및 결과 출력
num1 = 10
num2 = 5

result_add = mypackage.add_numbers(num1, num2)
result_sub = mypackage.subtract_numbers(num1, num2)

print(f"{num1} + {num2} = {result_add}")
print(f"{num1} - {num2} = {result_sub}")