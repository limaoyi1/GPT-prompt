import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gpt_prompt",
    version="0.0.12",
    author="limaoyi",
    author_email="2420845058@qq.com",
    description="python - pip package for a collection of high-quality GPT questions and prompts/ 包含GPT优质提问合集的pip包,支持多种语言",
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