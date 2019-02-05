from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='modulename',
    version='1.0',
    description='desciption of module',
    long_description=readme(),
    url='https://github.com/',
    author='Fame',
    author_email='natthapolmnc@outlook.com',
    license='',
    install_requires=[
    ],
    scripts=['bin/****',
            'bin/****',
            'bin/****'],
    keywords='',
    packages=['modulename(packagename)'],
    package_dir={'modulename(packagename)': 'src/__init__(Path)'},
    package_data={'modulename' :['file'] #ใช้สำหรับเพิ่มไฟล์เข้าไปในแพ็กเกจเพราะบางไฟล์ ตอนบีบไฟล์ก่อนอัพขึ้นมันจะไม่ถูกรวมไปกับไฟล์บีบอัด
    },
)