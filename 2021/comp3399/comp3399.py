import re


def solve(string):
    num_re = re.compile(r'(\d+)')
    arg_re = re.compile(r'\\([^.]+)\. ')
    var_re = re.compile(r' ([a-z])')

    lambda_re = re.compile(r'([^(])(lambda[^)]+)')

    class N:
        def __init__(self, val):
            self.val = val.val if isinstance(val, N) else val

        def __mul__(self, right):
            right = N(right)
            # print('applying', right, 'to', self)
            if isinstance(self.val, int):
                raise TypeError('cannot apply ' + str(right) + ' to ' + str(self))
            if isinstance(right.val, int):
                return N(self.val(right.val))

            result = self.val(right.val)
            if callable(result):
                return N(lambda xx: result * N(xx))
            return result

        def __rmul__(self, left):
            return N(left).__mul__(self)

        def __str__(self):
            return 'N(' + str(self.val) + ')'

    string = '(' + num_re.sub(lambda x: '(' + x[1] + ')', string) + ')'
    string = var_re.sub(lambda x: ' (' + x[1] + ')', string)
    # string = arg_re.sub(lambda x: 'lambda|' + ':lambda|'.join(x[1].split()) + ':', string)
    string = string.replace('. ', ':')
    string = string.replace(' ', '*')
    string = string.replace('\\', 'lambda ')
    n = 1
    # while n:
    #     string, n = lambda_re.subn(lambda x: x[1] + '(' + x[2] + ')', string)
    string = string.replace('(', 'N(')

    print(string)
    result = (eval(string, {'N': N}).val)
    print('>>>', result)
    return result

if __name__ == '__main__':
    # print(solve(r'(\p. \q. p q) (\x. x) 1'))
    # print(solve(r'(\p. \q. (p q) p) (\x. \y. x) (\x. \y. y) 1 2'))
    # solve(r'(\p. \q. (p q) p) (\x. \y. x) (\x. \y. x) 1 2')
    # print(solve(r'(\p. \q. p p q) (\x. \y. y) (\x. \y. y) 100 99'))

    solve(r'\x. x')

    # (solve(r'(\p. \q. p (\x. \y. q y x) q) (\x. \y. x) (\x. \y. y) 421 0'))
    # (solve(r'(\p. \x. \y. p y x) (\x. \y. y) 888 808'))

    (solve(r'(\p. \q. p ((\p. \x. \y. p y x) q) q) (\x. \y. x) (\x. \y. x) 1000 1111'))

    # solve(r'(\x. \y. x) 1 (\x. x)')
    # solve(r'(\x. \y. x) 42 (\x. x)')
    # solve(r'(\x. \y. y) (\x. x) 43')

    solve(r'(\x. \y. x) 42 (\x. x)')

