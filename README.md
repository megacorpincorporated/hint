# HOME-interface

## Get started

### Install Python3
Install a recent version of Python3, get it from [here](https://www.python.org/downloads/) or whatever package manager you're using.

### Checking 'pip' versions
Check which version of the Python Package Index (pip) you should use to proceed. You need to check this since many systems have Python installed by default and the command line tool "pip" usually defaults to a Python version less than 3.


```
$ which pip

# If the output displays some local path to a pre-existing version of Python located in /usr/local/... then try 'pip3' instead.

$ which pip3

# Depending on your system, this should give you the path to where the newly installed version of Python3 was installed, and in 
# which case, this is the pip command you want to use when proceeding. 'pip3' is usually more safe to use since it can only be 
# associated with Python 3.
```

### Python virtual environment setup
To separate Python packages you'll need for this project from other projects, install a Python virtual environment manager. Its documentation can be found [here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

```
# Assuming that 'pip3' was the correct one!

$ pip3 install virtualenvwrapper
...

# This will install a wrapper for ease of use around the basic Python virtual environment manager. Now, check what Python packages 
# are installed! NOTE that the version may differ since these packages are well maintained.

$ pip3 list
Package           Version
----------------- -------
pbr               5.4.1  <--
pip               19.2.1 
setuptools        28.8.0 
six               1.12.0 <--
stevedore         1.30.1 <--
virtualenv        16.7.2 <--
virtualenv-clone  0.5.3  <--
virtualenvwrapper 4.8.4  <--
...
# The six packages above come with the installation of 'virtualenvwrapper' and are the ones we want to see here.
```

Now, in order to make the newly installed package 'virtualenvwrapper' available for use in any new terminal window you start (without having to use `export` and `source` to set environment locations each time a new shell is started), you will need to edit your shell startup file. The file to edit depends on your system, for a Mac it would be the `.bash_profile` file.
```
# Insert the following into your shell startup file

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

Sometimes, when you have multiple Python versions on your $PATH variable, virtualenvwrapper will behave weirdly. This is because it by default looks for the first version of Python it can find from the $PATH variable. If you have multiple Python versions on the $PATH variable (test by `echo $PATH` in your terminal and check manually) it can be good to also add the line `export VIRTUALENVWRAPPER_PYTHON=<path to your Python3 version>` in order to make sure that the wrapper uses the Python version you want it to.

### Create a virtual environment
Now, after installing all the necessary Python utilities, go ahead and create a virtual environment where all Python packages related to this project can be installed.

```
# NOTE! If the below command does not work (your terminal can't find it) try opening a new shell so that you shell startup file
# gets executed and the virtualenvwrapper variable gets exported and the script sourced.

$ mkvirtualenv <name of virtual environment>
```

The command should output some installation information.

### Interacting with the virtual environment
Now that the virtual environment is created, you can exit out of it by using `deactivate`, and go back into it by using `workon <name of virtual environment>`. Make sure that you have used `workon` *before* installing any packages related to this project.

### Installing project Python dependencies
Assuming that the virtual environment related to this project is active (through `workon <name of virtual environment>`) then go ahead and install this project's dependencies.

```
# NOTE! Inside your virtual environment 'pip' will point to the Python version in use for this environment, so you do not have to
# use 'pip3'. Both 'pip' and 'pip3' should yield the same output.

$ pip install -r requirements.txt
```
And that's it, all Python dependencies are now installed into the project's virtual Python environment and will not affect any other project on your system!

### Installing frontend dependencies
The frontend part of this project is build with Angular. To use Angular we opted to use their Command Line Interface (Angular CLI). The Angular CLI is nice to use since it does a lot for you and is necessary to, upon code changes, immediately see the changes in the browser. It can also quickly create bare-bones Angular files for you.

To install the Angular CLI, you will first need to install both `node` and `npm`. In particular, `npm` is used as the package manager for all things Angular.
