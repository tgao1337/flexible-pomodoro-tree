from setuptools import setup

setup(name='pomodorotree',
	version='1.0',
	description='Flexible Pomodoro Tree for productivity',
	author='Tommy Gao, Shahzeb Naseer, Nick Coluccio',
	author_email='tommygao@nyu.edu',
	url='https://github.com/tgao1337/flexible-pomodoro-tree',
	install_requires=['smbus', 'PIL', 'pigpio', 'time', 'luma.oled'],
	py_modules=['pomodorotree'],
       )
