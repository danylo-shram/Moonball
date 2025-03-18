from setuptools import setup, find_packages

setup(
    name="ball-simulation",
    version="1.0.0",
    packages=find_packages('src/main/python'),
    package_dir={'': 'src/main/python'},
    include_package_data=True,
    install_requires=[],
    package_data={
        'ball_simulation': ['../resources/*.gif'],
    },
    entry_points={
        'console_scripts': [
            'ball-simulation=ball_simulation.ball_simulation:main',
        ],
    }
)