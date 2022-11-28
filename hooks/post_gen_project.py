import shutil

if '{{ cookiecutter.license }}' != 'Unlicensed':
    open('LICENSE.md', 'w').write(open('licenses/{{ cookiecutter.license }}','r').read())
shutil.rmtree('licenses')
