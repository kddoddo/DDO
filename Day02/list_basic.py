
'''
* 리스트 (list)

- 리스트: 여러 개의 값을 집합적으로 저장하기 위해 사용하는 파이썬의 자료형
- 다른 언어의 배열과 유사한 개념이며, 실제로 배열과 유사한 방식으로 데이터가 관리
- [] (대괄호) 안에 요소를 콤마로 구분하여 나열
'''
x = [5, 6, 10, 'a']
print(type(x))

for c in x:
    print(c)

print('리스트의 길이:', len(x))