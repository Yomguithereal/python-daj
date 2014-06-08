from setuptools import setup

setup(name='daj',
      version='0.1.0',
      description='Read and write data without further ado.',
      long_description=open('README.md').read().strip(),
      author='Yomguithereal',
      url='https://github.com/Yomguithereal/python-daj',
      py_modules=['daj'],
      install_requires=['pyyaml'],
      license='MIT License',
      zip_safe=False,
      keywords='data json yaml csv read write file')
