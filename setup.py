from setuptools import setup, find_packages

setup(
      name = "greengraph",
      version = "2.4.3",
      packages = find_packages(exclude=['*test']),
      scripts = ['scripts/greengraph'],
      
      install_requires = ['argparse','numpy','geopy','requests','matplotlib']
      
      author = "Leo Carlos-Sandberg",
      description = "Meausres amount of green pixels in google maps",
      license = "MIT",
)
