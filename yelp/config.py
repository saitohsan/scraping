import configparser

config = configparser.ConfigParser()

section1 = 'place'
config.add_section(section1)
config.set(section1, 'pref', '神奈川県')
config.set(section1, 'city', '横浜市')

with open('setting.ini', 'w') as file:
    config.write(file)