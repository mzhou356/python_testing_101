import setuptools

setuptools.setup(
	name="mindytests",
	version="1.0.0",
	author="Mindy Dossett",
	author_email="minzhou16@gmail.com",
	description="An example package with python testings",
	url="https://github.com/mzhou356/python_testing_101",
	packages=setuptools.find_packages(),
	entry_points={ "console_scripts":["quicktest=mindytests:main"]},
	python_requires=">=3.7"
)
