"""its a exam work author: Chernov"""
import operator

def is_palindrome(pal_str):
    """that function take 1 arg: str and tell is it a palindrome"""
    is_palindrome_flag = True
    if pal_str == '':
        return False
    pal_str = pal_str.replace(' ', '')
    for var_a, var_b in zip(pal_str, pal_str[::-1]):
        if var_a.strip().lower() != var_b.strip().lower():
            is_palindrome_flag = False
    return is_palindrome_flag

def get_most_frequent_value(max_num, list_of_values):
    """gets the most frequent value """

    if max(list_of_values) > max_num:
        raise ValueError('Ошибка, одно из значений превышает максимальное!')

    my_map = dict()
    for word in list_of_values:
        if word not in my_map:
            my_map[word] = 1
        else:
            my_map[word] += 1
    return sorted(my_map.items(), key=operator.itemgetter(1))[-1][0]

def is_prime(num):
    """check is it num prime or not"""
    try:
        return all(num % i for i in range(2, num))
    except TypeError:
        print("Задан неверный тип! Требуется int")

class Human:
    """thats class describes Human"""
    def __init__(self, name, weight, age):
        """Init a params of Human"""
        if weight < 0:
            weight = 0
        if age < 0:
            age = 0
        self.weight = weight
        self.name = name
        self.age = age
    def change_name(self, new_name):
        """change name on the given """
        self.name = new_name
    def happy_birthday(self):
        """adds 1 to age"""
        self.age += 1
    def add_weight(self, weight_update):
        """adds the given weight"""
        self.weight += weight_update
        if self.weight < 0:
            self.weight = 0

def count_castles(landscape):
    """none"""
    if landscape == 0:
        pass

def main():
    """the main function"""
    print(get_most_frequent_value(25, [3, 4, 2, 5, 6, 6,
                                       23, 4, 4, 2, 2, 2, 2, 2]))
    print(is_prime(7))
    print(is_prime(6))

    alex = Human('alex', 60, 20)
    print(alex.name)
    print(alex.weight)  # == 60
    alex.add_weight(-225)
    print(alex.weight)  # == 65
    alex.add_weight(-15)
    print(alex.weight)  # == 50
    alex.happy_birthday()
    alex.happy_birthday()
    print(alex.age)

if __name__ == '__main__':
    main()
