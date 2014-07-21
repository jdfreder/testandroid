# Getting started on Linux Mint

    cd ~
    sudo add-apt-repository ppa:kivy-team/kivy
    sudo apt-get update
    sudo apt-get install python2.7
    sudo apt-get install lib32stdc++6 lib32z1
    sudo apt-get install python-kivy
    wget http://python-distribute.org/distribute_setup.py
    sudo python distribute_setup.py
    sudo apt-get install python-dev
    sudo easy_install cython
    sudo easy_install pip
    sudo pip install buildozer
    sudo apt-get install zlib1g-dev
    sudo apt-get install freeglut3-dev
    sudo apt-get install openjdk-7-jdk

    buildozer android debug deploy run --verbose
