from setuptools import setup

setup(name='mongoq',
      version='0.1',
      classifiers = ["Development Status :: 3 - Alpha",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: BSD License",
                     "Programming Language :: Python :: 2",
                     "Programming Language :: Python :: 3"],
      description="mongoq generates MongoDB queries from simple python expressions",
      author='Alon Horev',
      author_email='alonho@gmail.com',
      packages=['mongoq'],
      license='BSD',
      url='https://github.com/alonho/mongoq')
