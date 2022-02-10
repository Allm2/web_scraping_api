import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    'bandit',
    'flake8',
    'isort',
    'pytest',
]
unit_test_requirements = [
    'pytest',
]
integration_test_requirements = [
    'pytest',
]
run_requirements = [
    'Flask==1.1.2',
]

with io.open('./web_scraping/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^_version_ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name="web-scraping",
    version=version,
    author="Allm2 Corporation",
    author_email="allm2@outlook.com.br",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url="",
    license="COPYRIGHT",
    description="Web scraping - metasearch anuncios",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
         'integration': integration_test_requirements,
    },
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6'
    ],
    # keywords=('API', 'Classification', 'Classification'),
    entry_points={
        'console_scripts': [
            'web_scraping = web_scraping.__main__:start_server'
        ],
    },
)
