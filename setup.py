from setuptools import setup , find_packages

setup(
    name='sveltctl',
    version='0.0.0.',
    packages=find_packages(),
    install_requires=[
        'click'
        'pytailwindcss'
        'trpc'
    ],
    entry_points='''
    [console_scripts]
    sveltctl=sveltctl:sveltctl
    '''
)

    
