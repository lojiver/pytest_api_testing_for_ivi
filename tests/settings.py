name_valid_for_get = [
    'Avalanche',
    'Shang-Chi',
    'Sebastian Shaw',

]

name_valid_for_post = [
    'Incredi-Boy',
    'Mr. Incredible',
    'Frozone',

]

name_invalid = [
    'Sylvia Sersi',  # это имя отображено в other_aliases, Нужно убедиться, что по ним поиск не работает
    'rtkid_167328',
    'nice site,  i think i\'ll take it. <script>alert("executing js")</script>',
    'robert\'); drop table students;--',
    '<i><b>bold</i></b>',
    '"-prompt()-"',
    '我不会说汉语请做不辣的怎么样你会说英语',
    '',
    12345,
    5.12,
    True,
    None
]

str_valid = ['Marvel Universe', 'High school (unfinished)', 'Well-known']

int_valid = [1, 55, 115]

float_valid = [70.10, 0.99, 5.667376]

int_invalid = ['45', 'ten', 1.0, 281597344350982367258, -15, True]

float_invalid = [1.239483587569843756456964309654, '1.99', 67, -0.9, True]
