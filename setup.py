from setuptools import setup

setup(
    name='django-flatpages-plus',
    packages=['flatpages_plus'],
    include_package_data=True,
    version='0.1.1',
    description='A more robust FlatPage app for Django.',
    author='Dana Woodman',
    author_email='dana@danawoodman.com',
    url='https://github.com/danawoodman/django-flatpages-plus',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    install_requires=['setuptools'],
)
