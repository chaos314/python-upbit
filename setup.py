from setuptools import setup

dependencies = [
    'requests',
    'pyjwt'
]

version = '1.0.0'

setup(name='upbit',
      version=version,
      packages=['upbit'],
      description='Python wrapper for the Upbit REST API',
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
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Topic :: Office/Business :: Financial',
      ],
)
