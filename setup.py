from setuptools import setup

setup(name='daj',
      version='0.1.0',
      description='Read and write data without further ado.',
      long_description=open('README.md').read().strip(),
      author='Yomguithereal',
      url='https://github.com/Yomguithereal/python-daj',
      packages=['daj'],
      py_modules=['daj'],
      install_requires=['pyyaml'],
      license='MIT License',
      zip_safe=False,
      keywords='data json yaml csv read write file',
      classifiers=[
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Utilities'
      ])
