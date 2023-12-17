from setuptools import setup, find_packages

REPO_NAME = 'End-To-End-Malicious-Classification'
AUTHOR_USER_NAME = 'aqibrehmanpirzada'
SRC_REPO = 'End-To-End-Malicious-Classification'
AUTHOR_EMAIL = 'aqibrehmanpirzada75@gmail.com'

setup(
    name=REPO_NAME,
    version='0.1',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'scikit-learn'
    ],
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
)
