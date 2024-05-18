from setuptools import setup, find_packages

setup(
    name="minaibot",
    version="0.1.0",
    description="BotFramework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nikita Minai",
    author_email="nikita.minai@ya.ru",
    url="https://github.com/yourusername/minaibot",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "pyTelegramBotAPI",
        "telebot",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
