from setuptools import setup

setup(
    name = "modern_robotics",
    version = "0.0.1",
    author = "Huen Weng",
    author_email = "asdf@gmail.com",
    description = ("Modern Robotics library"),
    license = "MIT",
    keywords = "kinematics robotics dynamics",
    url = "http://hades.mech.northwestern.edu/index.php/Modern_Robotics",
    packages=['modern_robotics'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'numpy',
        'scipy',
    ],
    platforms='Linux, Mac, Windows',
)
