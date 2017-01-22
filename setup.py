from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pdf_reader',
      version='0.1',
      description='The best reader in the world',
      url='https://github.com/omfd/pdf_reader',
      author='OM',
      author_email='oldmonkfromdesert@gmail.com',
      test_suite='nose.collector',
      tests_require=['nose'],
      license='MIT',
      packages=['pdf_reader'],
      install_requires=['markdown'],
      scripts=['bin/reader_sample.py'],
      entry_points={
          'console_scripts': ['reader_sample=pdf_reader.reader_sample:main'],
      },
      include_package_data=True,
      zip_safe=False)
