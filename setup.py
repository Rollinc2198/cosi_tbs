from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cosi_tbs',
      version='0.1',
      description='Client for COSI Turn-based Strategy',
      classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.6',
            'Topic :: Games/Entertainment :: Board Games',
      ],
      keywords='board game games cosi turn turn-based strategy',
      url='http://github.com/Rollinc2198/cosi_tbs',
      author='Carter Rollins, Anthony (Mangiacapra, Rinaldo)',
      author_email='rollinc@clarkson.edu',
      license='MIT',
      packages=['cosi_tbs'],
      install_requires=[
            'pygame'
      ],
      include_package_data=True,
      zip_safe=False)