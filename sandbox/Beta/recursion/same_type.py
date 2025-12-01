def same_type(func):
    def wrapper(*args):
        types = [type(el) for el in args]
        if len(set(types)) > 1:
            print("Обнаружены различные типы данных")
            return "Fail"
        return func(*args)
    return wrapper


   
@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')