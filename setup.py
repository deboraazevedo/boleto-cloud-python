from setuptools import setup

setup(name='boleto-cloud-python',
      version='0.1',
      description='Biblioteca de integração com a API do boletocloud.com',
      url='https://github.com/hudsonbrendon/boleto-cloud-python',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['boletocloud'],
      install_requires=[
          'requests',
      ],
      zip_safe=False
)