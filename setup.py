from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django_mzxl",
    version="0.1",
    author="zhaofeng-shu33",
    description="mzxl information collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/freewind201301/mzxl",
    author_email="616545598@qq.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
