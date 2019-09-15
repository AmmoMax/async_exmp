from time import time


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))

        sum = 234 + 234
        print(sum)

# g = gen_filename()

def gen(n):
    for i in n:
        yield i


def gen2(n):
    for i in range(n):
        yield i

g1 = gen('max')
g2 = gen2(3)

tasks = [g1, g2]
while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass


