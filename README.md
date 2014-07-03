# Getting started on Linux Mint

    cd ~
    sudo apt-get update
    sudo apt-get install python2.7
    sudo apt-get install lib32stdc++6 lib32z1
    wget http://python-distribute.org/distribute_setup.py
    python distribute_setup.py
    easy_install cython
    sudo easy_install pip
    sudo pip install buildozer


    buildozer android debug deploy run --verbose

---

## This is old and doesn't work all the way.

    cd ~
    sudo apt-get update
    sudo apt-get install python2.7
    wget http://python-distribute.org/distribute_setup.py
    python distribute_setup.py
    sudo easy_install jinja
    sudo apt-get install openjdk-7-jre-headless
    sudo apt-get install openjdk-7-jdk
    sudo apt-get install ant1.8
    sudo apt-get install android-tools-adb

Download the [android sdk](http://developer.android.com/sdk/installing/index.html?pkg=tools).
Extract the contents to your home directory.

    cd ~
    cd android-sdk-linux
    tools/android update sdk --no-ui
    cd ..
    git clone git://github.com/kivy/python-for-android
    cd python-for-android/
    ./distribute.sh -m "kivy"

----
