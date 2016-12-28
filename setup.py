from setuptools import setup, find_packages

setup(
      name = "greengraph",
      version = "3",
      packages = find_packages(exclude=['*test']),
      scripts = ['scripts/greengraph'],
      
      install_requires = ['argparse','numpy','geopy','requests','matplotlib']
      
)
