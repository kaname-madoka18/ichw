#!/usr/bin/env python3

"""
tile.py: print all choice to overspread the wall,
and draw it by turtle.

__author__ = "Songzetian"
__pkuid__  = "1800011835"
__email__  = "1800011835@pku.edu.cn"
"""

import turtle


def get_rect(a, b, m, n, i):
    # i,a,b,m,n分别为左上顶点位置代号、
    # 长方形的横向跨度、纵向跨度、大长方形的长和宽
    t = tuple()
    p, q = divmod(i, m)
    if q+a <= m and p+b <= n:
        for k in range(b):
            t += tuple(range(i, i+a))
            i += m
    else:
        t = False
    return t


def put_in(start, abmni, total, results):
    # abmni为get_rect函数的参数元组
    # start为已铺好的瓷砖（由元组表示）组成的列表
    # total是格子总数m*n,
    # 在现有状况下铺一块瓷砖并记录，再以此为初始状况调用自身进行递归，
    # 结果用results列表储存
    a, b, m, n, i = abmni
    t = get_rect(a, b, m, n, i)
    if t:
        now0 = start+[t]
        occ0 = []
        for k in now0:
            occ0.extend(k)
        occ = set(occ0)
        s = len(occ)
        if s == total:
            results.append(now0)
        elif len(occ0) == s:
            uno = set(range(total))-occ
            i = min(uno)
            put_in(now0, (a, b, m, n, i), total, results)
            put_in(now0, (b, a, m, n, i), total, results)
    return results


def draw(results, m, n):       # 用turtle进行可视化
    para = 400/m
    bob = turtle.Turtle()
    ln = len(results)
    while True:
        need = turtle.textinput(
            'which you want to draw?',
            'input a interger from 1 to {}\
            (input nothing to quit):'.format(ln)
            )
        bob.reset()
        if need == '':
            return 0
        elif not need.isdigit():
            bob.write('invalid input', font=("Arial", 20, "normal"))
            continue
        need = int(need)-1
        if need >= ln:
            bob.write('invalid input', font=("Arial", 20, "normal"))
            continue
        grl = results[need]
        bob.speed(0)
        bob.penup()

        bob.goto(-200, 200)
        bob.pencolor('blue')
        for i in range(1, n+1):
            bob.pendown()
            bob.fd(400)
            bob.penup()
            bob.goto(-200+0.5*para, 200-(i-0.5)*para)
            for u in range(m):
                bob.write('%s' % int(m*(i-1)+u),
                          align='center',
                          font=("Arial", 10, "normal"))
                bob.fd(para)
            bob.goto(-200, 200-i*para)
        bob.pendown()
        bob.fd(400)
        bob.penup()
        bob.goto(-200, 200)
        bob.rt(90)
        width = para*n
        for i in range(1, m+2):
            bob.pendown()
            bob.fd(width)
            bob.penup()
            bob.goto(-200+i*para, 200)
        bob.lt(90)              # draw the based wall

        bob.penup()
        bob.goto(-200, 200)
        bob.pensize(5)
        bob.pencolor('black')
        for i in grl:
            lu, rd = i[0], i[-1]
            y, x = divmod(lu, m)
            bob.goto(para*x-200, 200-para*y)
            dy, dx = divmod(rd-lu, m)
            dy += 1
            dx += 1
            bob.pendown()
            for k in range(2):
                bob.fd(para*dx)
                bob.rt(90)
                bob.fd(para*dy)
                bob.rt(90)
            bob.penup()         # draw the bricks


def main():             # 分类讨论正方形和长方形
    m = int(input('length of wall = '))
    n = int(input('width of wall = '))
    a = int(input('length of brick = '))
    b = int(input('width of brick = '))
    total = n*m
    if a != b:
        results = (
            put_in([], (a, b, m, n, 0), total, []) +
            put_in([], (b, a, m, n, 0), total, [])
            )
    else:
        if m % a == 0 and n % a == 0:
            t = True
            result = []
            for i in range(n//a):
                for u in range(m//a):
                    result.append(get_rect(a, b, m, n, u*a+i*a*m))
            results = [result]
        else:
            results = []
    num = len(results)
    if num == 0:
        print('None')
    else:
        for i in range(num):
            print(i+1, results[i])
        draw(results, m, n)


if __name__ == '__main__':
    main()
