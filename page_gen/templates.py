from jinja2 import Environment, select_autoescape, FileSystemLoader


env = Environment(
    loader=FileSystemLoader('page_gen'),
    autoescape=select_autoescape(),
)


html_template = env.get_template('template.html')
config_template = env.get_template('template.cfg')
