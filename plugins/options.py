import pykakasi

DEFAULT_OPTIONS = {
    'text': None,
    'name': None,
    'color': 'EC71A1',
    'back_color': 'FFFFFF',
    'font': 'notosans-mono-bold'
}
COLORS = {
    'white': 'FFFFFF',
    'silver': 'C0C0C0',
    'gray': '808080',
    'black': '000000',
    'red': 'FF0000',
    'maroon': '800000',
    'yellow': 'FFFF00',
    'olive': '808000',
    'lime': '00FF00',
    'green': '008000',
    'aqua': '00FFFF',
    'teal': '008080',
    'blue': '0000FF',
    'navy': '000080',
    'fuchsia': 'FF00FF',
    'purple': '800080',
}
FONTS = [
    'notosans-mono-bold',
    'mplus-1p-black',
    'rounded-x-mplus-1p-black',
    'ipamjm',
    'aoyagireisyoshimo',
]


def parse(text):
    # store command
    _, *opt = text.split('--')

    # extract options
    opt = [lrstrip(opt_) for opt_ in opt]
    opt = [opt_.split(' ') for opt_ in opt]
    opt = {opt[0]: opt[1] for opt in opt}

    if 'name' not in opt.keys():
        kakasi = pykakasi.kakasi()
        kakasi.setMode('H', 'a')
        kakasi.setMode('K', 'a')
        kakasi.setMode('J', 'a')
        conv = kakasi.getConverter()
        opt['name'] = conv.do(opt['text'].replace('\\n', '')).lower()
    if 'color' not in opt.keys():
        opt['color'] = DEFAULT_OPTIONS['color']
    if 'back_color' not in opt.keys():
        opt['back_color'] = DEFAULT_OPTIONS['back_color']
    if 'font' not in opt.keys():
        opt['font'] = DEFAULT_OPTIONS['font']

    if opt['color'] != DEFAULT_OPTIONS['color']:
        assert opt['color'] in COLORS.keys()
        opt['name'] += '_' + opt['color']
        opt['color'] = COLORS[opt['color']]
    if opt['back_color'] != DEFAULT_OPTIONS['back_color']:
        assert opt['back_color'] in COLORS.keys()
        opt['name'] += '_bg' + opt['back_color']
        opt['back_color'] = COLORS[opt['back_color']]
    if opt['font'] != DEFAULT_OPTIONS['font']:
        assert opt['font'] in FONTS
        opt['name'] += '_' + opt['font']

    opt['text'] = opt['text'].replace('\\n', '%0A')
    opt['color'] += 'FF'
    opt['back_color'] += 'FF'

    return opt


def lrstrip(text):
    return text.lstrip().rstrip()
