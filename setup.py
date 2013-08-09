import os

from setuptools import setup, find_packages


def local_file(fn):
    return open(os.path.join(os.path.dirname(__file__), fn))


setup(name='big',
      version='1.0.0',
      description="Create a Big presentation in Markdown",
      long_description=local_file('README.md').read(),
      author='Harper Reed',
      author_email='',
      license='whatever',
      url='https://github.com/harperreed/bigpy',
      include_package_data=True,
      classifiers=[],
      entry_points="""
          [console_scripts]
          bigpy = big:main
          """,
      py_modules=['big'],
      install_requires=[ln.strip() for ln in
                        local_file('requirements.txt')
                        if not ln.startswith('#')])
