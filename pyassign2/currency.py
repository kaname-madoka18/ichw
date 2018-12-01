#!/usr/bin/env python3

"""currency.py: It is a currency converter .

__author__ = "Songzetian"
__pkuid__  = "1800011835"
__email__  = "1800011835@pku.edu.cn"
"""


def cal(x, y, z):         # 接受三个参数x,y,z;返回从数量为z的x货币转换为y货币后的量
    from urllib.request import urlopen
    st = "http://cs1110.cs.cornell.edu/2016fa/\
a1server.php?from=%s&to=%s&amt=%s" % (x, y, z)
    doc = urlopen(st)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    true = True
    false = False
    get = eval(jstr)
    if get['success']:
        amount = float(get['to'].split()[0])
        return amount
    else:
        return get['error']


def get_test_data():                # 测试数据库
    d = {
        ('USD', 'EUR', '2.36'): 2.03802284,
        ('JPY', 'USD', '12356'): 110.9166150504,
        ('GBP', 'USD', '535221561'): 687951640.95307,
        ('CAD', 'USD', '12.225'): 9.2741577585442,
        ('GBP', 'JPY', '0.00000002'): 2.8637532728444e-06,
        ('EUR', 'JPY', '125335'): 16168011.664384,
        ('aaa', 'bbb', '2536'): 'Source currency code is invalid.',
        ('USD', 'EUR', '25a'): 'Currency amount is invalid.'
        }
    return d


def test_all():                     # 测试函数
    d = get_test_data()
    for i in d:
        assert(d[i] == cal(*i))
    print('All Test Pass!')


def main():              # 主函数，接受输入并打印结果，当用户全部输入空字符串时退出
    while True:
        x = input('from(all type enter to quit)')
        y = input('to=')
        z = input('amount=')
        if (x, y, z) == ('', '', ''):
            break
        print(cal(x, y, z))


if __name__ == '__main__':
    main()
