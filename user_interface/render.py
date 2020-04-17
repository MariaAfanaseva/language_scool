"""
Pattern INTERFACE
Use template engine jinja2
"""
from jinja2 import Template


def render(template_name, **kwargs):
    file_path = 'templates/' + template_name
    with open(file_path) as html_file:
        template = Template(html_file.read())
    return template.render(**kwargs)


if __name__ == '__main__':
    outputText = render('teachers.html', object_list=[{'name': 'Leo', 'surname': 'Lenovich'},
                                                      {'name': 'Kate', 'surname': 'kATIVICH'}])
    print(outputText)
