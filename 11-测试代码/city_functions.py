__Author__ = "noduez"

"""一系列处理城市的函数。"""


def city_country(city, country):
    """返回一个形如'Santiago, Chile'的字符串。"""
    return (city.title() + ", " + country.title())


def city_country_population(city, country, population):
    """返回一个形如'Santiago, Chile - population 5000000'的字符串。"""
    output_string = city.title() + ", " + country.title()
    output_string += ' - population ' + str(population)
    return output_string