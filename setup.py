from setuptools import setup, find_packages

setup(
    name='django-flatpages-plus',
    version='0.1.1',
    description='A more robust FlatPage app for Django.',
    author='Dana Woodman',
    author_email='dana@danawoodman.com',
    url='https://github.com/danawoodman/django-flatpages-plus',
    license='MIT',
    template_patterns = [
        'templates/*.html',
        'templates/*/*.html',
        'templates/*/*/*.html',
    ],
    packages=find_packages(),
)
