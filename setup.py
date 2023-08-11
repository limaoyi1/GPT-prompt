import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_prompts",
    version="0.0.10",
    author="limaoyi",
    author_email="limaoyi@qq.com",
    description="Convenient for Python users to directly reference the source code of the GPT question template "
                "package. / 方便python用户直接引用GPT提问模板包的源代码",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/limaoyi1/GPT-prompt",
    packages=setuptools.find_packages(),
    # 不需要
    # install_requires=['Pillow>=5.1.0', 'numpy==1.14.4'],
    # entry_points={
    #     'console_scripts': [
    #         'douyin_image=douyin_image:main'
    #     ],
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)