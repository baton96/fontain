import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fontain',
    packages=['fontain'],
    version='0.1.1',
    license='MIT',
    description='Python tool for font recognition on images',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Bartosz Paulewicz',
    author_email='podolce0@gmail.com',
    url='https://github.com/baton96/fontain',
    download_url='https://github.com/baton96/fontain/archive/refs/tags/0.1.1.tar.gz',
    keywords=['font', 'ocr'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
