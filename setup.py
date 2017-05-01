from distutils.core import setup
setup(
  name = 'sghmc',
  packages = ['sghmc'], # this must be the same as the name above
  version = '0.1',
  description = 'Stochastic gradient Hamiltonian Monte Carlo package',
  author = 'Shen Yan',
  author_email = 'shenyan.username@gmail.com',
  license='LICENSE.txt',
  long_description=open('README.txt').read(),  
  url = 'https://github.com/yanshen0/SGHMCPackage', # use the URL to the github repo
  download_url = 'https://github.com/yanshen0/SGHMCPackage/archive/0.1.tar.gz', 
  keywords = ['Stochastic Gradient Hamiltonian Monte Carlo', 'Hamiltonian Monte Carlo'], 
  classifiers = [],
)
