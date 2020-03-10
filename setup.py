import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='news_getter',
     version='0.2',
     author="Itai Sevitt",
     author_email="isevitt@gmail.com",
     description="A news getter package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/isevitt/news-getter",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
python_requires='>=3.6',
 )

