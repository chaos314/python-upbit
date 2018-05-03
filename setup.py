from setuptools import setup

dependencies = [
    'requests',
    'pyjwt'
]

version = '0.2.0'

setup(name='python-upbit',
      version=version,
      packages=['upbit'],
      description='Python wrapper for the Upbit API',
      url='https://github.com/chaos314/python-upbit',
      author='Seokhwan Cheon',
      author_email='chaos314@gmail.com',
      license='MIT',
      install_requires=dependencies,
      keywords=['upbit', 'crypto', 'bitcoin'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Development Status :: 3 - Alpha',
          'Topic :: Office/Business :: Financial',
      ],
)
