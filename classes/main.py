from cookie import Cookie

if __name__ == '__main__':
    cookie_1 = Cookie('red')
    cookie_2 = Cookie('chocolate')
    print(cookie_1.color)
    print(cookie_2.color)
    cookie_1.set_color('vanilla')
    print(cookie_1.color)