from setuptools import setup, find_packages

setup(
    name='roadrushgame',
    version='0.1',
    author='Roshan Mishra',
    author_email='roshan4182@email.com',
    description='A simple racing game implemented in Pygame',
    long_description=open('README.md','r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/roshan4182/racing_game/actions/runs/8608562256/job/23591130691',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
