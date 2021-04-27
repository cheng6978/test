base_encode = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/',
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0',
    '-': '-'
}
url_list=[]
def encoding(objurl):
    if '_z2C$q' in objurl:
        objurl=objurl.replace('_z2C$q',':')
    if '_z&e3B' in objurl:
        objurl=objurl.replace('_z&e3B','.')
    if 'AzdH3F' in objurl:
        objurl = objurl.replace('AzdH3F', '/')
    res=''
    for s in objurl:
        if s in base_encode:
            res+=base_encode[s]
        else:
            res+=s
    url_list.append(res)
