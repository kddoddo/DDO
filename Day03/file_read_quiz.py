'''
* points.txt 파일의 숫자값을 모두 읽어서
총합과 평균을 구한 뒤
총점, 평균값을 result.txt라는 파일에
쓰는 프로그램을 작성해 보세요.
'''

file_path = 'C:/test/points.txt'

try:
    f = open(file_path, 'r')

    text = f.readlines()
    print(text)
except:
    print('파일 로드 실패')
finally:
    f.close()