try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

# here = os.path.abspath( os.path.dirname( __file__ ) )
# README = open(os.path.join( here, 'README.rst' ) ).read()

setup(name='chibi_file',
      version='0.1',
      description='',
      # long_description=README,
      license='',
      author='',
      author_email='',
      packages=find_packages(),
      install_requires=[],
      dependency_links = [],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
      ])
