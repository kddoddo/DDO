
'''
* 사전 (Dictionary)

- 사전은 키(key)와 값(value)의 쌍을 저장하는 대용량의 자료구조
- 사전은 'Map'이라고도 부르며 '연관배열'이라고도 부른다
- 사전을 정의하는 기호는 {}이고, 괄호 안에 데이터를 key:value 형태로 나열하여 저장
'''

students = {'멍멍이':'김철수', '야옹이':'박영희', '짹짹이':'홍길동'}
print(type(students))
print(len(students))

'''
- 사전에 사용되는 key값은 중복값을 가질 수 없고, 변경도 불가능
- 반면에 value값은 중복 허용, 데이터를 자유롭게 편집 가능
- 사전 내부에 저장된 데이터를 검색할 때는 인덱스 대신 key를 사용 (시퀀스 자료가 아님)
'''
print(students['멍멍이'])
print(students['짹짹이'])
# print(students['메뚜기']) (X)

# in 키워드를 사용하여 key의 존재 유무를 파악 가능
print('멍멍이' in students)
print('메뚜기' in students)
