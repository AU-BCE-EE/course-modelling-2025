# Introduction to requirements.txt
It is good practice to include a small file called requirements.txt as part of any Python project, and that might as well extend to assignments.

# File contents and creation
The requirements.txt file has a single package (library) and version number on each line.
Here are the contents for one that uses two common packages:

```
numpy==1.26.4
matplotlib==3.6.3
```

You can create the file manually, or else use the Python package installer pip to return what you need by running the following in an appropriate shell.

```
pip freeze
```

Relevant lines can be copied and pasted into the text file.
Save the file at the root of your project directory.

# File usage
The file is human-readable, so you can see in a glance what packages are reuired for your old project, or a new project from someone else.
The version numbers are included because package behavior does, in some cases, change over time.
So it is possible, but not typically the norm, that a project won't run or won't return the correct results if you instead use the latest available package version.
To install the specified versions, just run the following command in an appropriate shell.

```
pip install -r requirement.txt
```

# More information
This site has a good summary and some details: <https://coderivers.org/blog/requirementstxt-python/>.
