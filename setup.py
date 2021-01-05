from setuptools import setup, find_packages

version = "1.2.3"

setup(
	name='py_owm',
	version=version,
	packages=find_packages(),
	url='https://github.com/vcokltfre/py-owm',
	license='MIT',
	author='vcokltfre',
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=["requests", "aiohttp"],
	description='A Python library to interface with the OpenWeatherMap weather API',
	python_requires='>=3.6',
)