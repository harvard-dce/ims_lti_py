from setuptools import setup, find_packages

setup(
    name='ims_lti_py',
    version='0.6.0',
    description=('A Python library to help implement IMS '
                 'LTI tool consumers and providers'),
    author='Jay Luker',
    author_email='jay_luker@harvard.edu',
    url='https://github.com/harvard-dce/ims_lti_py',
    packages=find_packages(),
    install_requires=['lxml', 'oauth2'],
    license='MIT License',
    keywords='lti',
    zip_safe=True,
    test_suite='tests',
)
