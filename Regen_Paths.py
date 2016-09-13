bitmaps = [
    {'name': 'am120_54_wood_d.jpg', 'path': 'C:\\3d\\bibl\\wood', 'status': 'missing'},
    {'name': 'am120_54_wood_b.jpg', 'path': '', 'status': 'missing'},
    {'name': 'am10_glass.png', 'path': 'C:\\3d\\library\\evermotion', 'status': 'OK'},
    {'name': 'am54_ceramic.png', 'path': '', 'status': 'found'},
    {'name': 'am34_01.jpg', 'path': 'D:\\проекты\\самое важное\\сдать вчера\\', 'status': 'missing'},
]
libs = [
    {'name': 'Archmodels 120', 'template': 'am120', 'path': 'D:\\3d\\Library\\Evermotion\\Archmodels vol.120\\maps'},
    {'name': 'Archmodels 132', 'template': 'am132',
     'path': 'D:\\3d\\Library\\Evermotion\\Archmodels vol.132\\textures'},
    {'name': 'Archmodels 12', 'template': 'am12', 'path': 'D:\\3d\\Library\\Evermotion\\Archmodels vol.12\\textures'}
]


def print_bitmaps_table(bitmaps):
    print('{:^15}|{:^20}|{:^40}'.format('Status', 'Name', 'Path'))  #заголовок таблицы
    print('-'*77)   #горизонтальная черта
    for b in bitmaps:
        print('{:^15}|{:^20}|{:^40}'.format(b['status'], b['name'], b['path']))  # вывод строки таблицы


def find_lib(bitmap, libs):
    for lib in libs:
        if lib['template'] in bitmap['name']:
            return lib


for bitmap in bitmaps:
    if bitmap['status'] == 'missing':
        lib = find_lib(bitmap, libs)
        if lib is not None:
            bitmap['path'] = lib['path']
            print('карте {} задан путь {}'.format(bitmap['name'], lib['path']))
        else:
            print('карте {} не соотвествует ни одна библиотека'.format(bitmap['name']))

print_bitmaps_table(bitmaps)
