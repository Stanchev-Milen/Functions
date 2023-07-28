from math import pi


def figure_area(figure='figure could be: square, rectangle, circle or triangle'):
    figure = input('Please give us the figure: ')
    valid_values = ['square', 'rectangle', 'circle', 'triangle']
    while figure in valid_values:
        area = 0
        if figure == 'square':
            a = float(input('a = '))
            area = a * a
        elif figure == 'rectangle':
            a = float(input('a = '))
            b = float(input('b = '))
            area = a * b
        elif figure == 'circle':
            r = float(input('r ='))
            area = pi * (r * r)
        elif figure == 'triangle':
            a = float(input('a= '))
            h = float(input('h= '))
            area = (a * h) / 2

        print(f'The area of the {figure} is {area: .3f}')
        figure = input('Please give us the figure: ')


figure_area()
# 3 more
