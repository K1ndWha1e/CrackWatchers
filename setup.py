from setuptools import setup

with open('README.md', 'r') as readme:
    description = readme.read()

setup(name='CrackWatchers',
      version='0.3',
      description=description,
      url='https://github.com/K1ndWha1e/CrackWatchers',
      author='K1ndWha1e',
      author_email='nikita356@gmail.com',
      license='Apache-2.0',
      download_url='https://github.com/K1ndWha1e/CrackWatchers/blob/master/archive/CrackWatchers.tar.gz',
      keywords=['PyCrackWatch', 'Crack', 'Watch', 'CrackWatch API', 'CrackWatch Python Api'],
      packages=[
                  'CrackWatchers',
                  'requests',
      ])
