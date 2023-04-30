# def print_given(*args, **kwargs):
#     for x in args:
#         print(x, type(x))
#     for x in kwargs:
#         print(x, kwargs[x], type(kwargs[x]))
#
#


# print_given(1, 2, 3, [5, 6, 7], 'one', 'two', 'three', five=5, six=6, seven=7)
# # очень хороший пример
#




#
# # вот два варианта решения первый тип продвинутый
# print(*map(float, input().split()), sep='\n')
#
# # второй не такой уж и продвинутый, но работает
# for i in (input().split()):
#     print(float(i))
#
#
# # третий вариант если использовать *
# def float_digit(*i):
#     for k in i:
#         print(float(k))
#
#
# float_digit(*input().split())





# k = sorted("This is a test string from Andrew".split(), key=str.lower)
#
# print(k)
#
# for i in k:
#     print(ord(i[0].lower()))
#
# print()
# m = sorted("This is a test string from Andrew".split(), key=str)
#
# print(m)
#
# for i in m:
#     print(ord(i[0]))




# number_names = {
#         0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9:'nine', 10:
#         'ten', 11: 'eleven', 12: 'twelve',
#         13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}
# # for i in number_names:
# #     print(number_names[i])
#
# print(type(number_names))


def decor(k):
    def wrapper():
        print("1 thik")
        k()
        print("3 thik")


    return wrapper


@decor
def lev():
    print('levon barev')


lev()

