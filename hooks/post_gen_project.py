import shutil
import os
import glob

if '{{ cookiecutter.license }}' != 'Unlicensed':
    open('LICENSE.md', 'w').write(open('licenses/{{ cookiecutter.license }}','r').read())
shutil.rmtree('licenses')

readme_file = 'README_yarn.md' if '{{ cookiecutter.build_system }}' == 'yarn' \
    else 'README_npm.md'

os.rename(readme_file, 'README.md')
for file in glob.glob('README_*.md'): os.remove(file)
