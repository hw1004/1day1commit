def func():
    print('hi')
    
if __name__ == '__main__':
    print('내가 부르는 이름', __name__)   # __main__
else:
    print('남이 부르는 이름', __name__)   # a
    
print(__name__)    # __name__은 나(파일 자신)을 의미