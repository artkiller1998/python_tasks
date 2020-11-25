# class Planet:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return "Planet {0}".format(self.name)
#
# solar_system = []
# planet_names = [
#     "Mercury", "Venus", "Earth", "Mars",
#     "Jupiter", "Saturn", "Uranus", "Neptune"
# ]
#
# for name in planet_names:
#     planet = Planet(name)
#     solar_system.append(planet)
#
# print(solar_system)
#
# mars = Planet("Mars")
# print(mars)
# print(mars.name)
# mars.name = "Second Earth?"
# del mars.name
# print(mars.name)

# for _ in range(5):
#     print(_)
#
# for letter in 'python':
#     print(ord(letter))
#
# iterator = iter([1, 2, 3])
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# class SquareIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#
#         result = self.current ** 2
#         self.current += 1
#         return result
#
# for num in SquareIterator(1, 4):
#     print(num)

# class suppress_exception:
#     def __init__(self, exc_type):
#         self.exc_type = exc_type
#
# def __enter__(self):
#     return
#
# def __exit__(self, exc_type, exc_value, traceback):
#     if exc_type == self.exc_type:
#         print('Nothing happend.')
#         return True
#
# with suppress_exception(ZeroDivisionError):
#     really_big_number = 1 / 0
#
# class open_file:
#     def __init__(self, filename, mode):
#         self.f = open(filename, mode)
#
#     def __enter__(self):
#         return self.f
#
#     def __exit__(self, *args):
#         self.f.close()
#
# with open_file('test.log', 'w') as f:
#     f.write('Inside `open_file` context manager')
#
# with open_file('test.log', 'r') as f:
#     print(f.readlines())

class Planet:

    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

# Можем напрямую обратиться к атрибуту класса через точку:
earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)

print(earth.__dict__)
print(earth)

earth.mass = 5.97e24
earth.people_dead = 112
print(earth.__dict__)