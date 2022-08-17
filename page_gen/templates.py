from jinja2 import Environment, select_autoescape, FileSystemLoader


'''
To be called from the project root
'''


env = Environment(
    loader=FileSystemLoader('page_gen'),
    autoescape=select_autoescape(),
)


template = env.get_template('index_template.html')


with open('2/index.html', 'w') as f:
    print(template.render(
        round=2,
        description='Esolang Buffet round #2',
        start_date='2022-08-23T21:37:00.148869',
        first_deadline='2022-08-30T21:37:00.148869',
        second_deadline='2022-09-06T21:37:00.148869',
        now='2022-08-20T21:37:00.148869',
        task_description='multiply two matrices',
        test_cases='1 1 1 1 1 => 1',
        file_length=5,
        file_language='python',
        file_contents='''import antigravity
beeeees = lambda _: snans_dundertol
# hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha
def test(a, q):
    print(q)'''), file=f)
