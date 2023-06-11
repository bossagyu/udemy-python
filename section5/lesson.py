l = [1, 2, 3]
i = 5
del l

class UppercaseError(Exception):
    pass


try:
    l[i]
except IndexError as ex:
    print("except. {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    print('done')
finally:
    print('clean up')

animal = 'cat'

def f():
    print('local:', locals())

f()
print('global:', globals())
