# A short introduction to Git and GitHub
Sasha D. Hafner

# Overview
This document is meant to provide a basic introduction to Git and GitHub for students with no prior experience.

# What are Git and GitHub?
**Git** is a version control program that is used to track changes in files.
While initially intended for software development, it works well for any kind of text files, and Python scripts are a good fit.
Git finds every change in every file in your project files ("repository") and can tell you at any point which files you have changed and exactly how.
You, the user, need to decide how to group and save these changes together in the version history as a "commit".
When you "pull" a commit from a collaborator Git can "merge" the different versions automatically, as long as two people didn't change the same file in the same location.
You and your collaborators can check the history of every single line in every project file and restore any previous version.
The collection of files handled together as a single project by Git are called a "repository" or "repo".

Git is commonly used at the command-line interface, where users type commands in a shell.
Here is an example from my work on this file:

<img width="955" height="438" alt="image" src="https://github.com/user-attachments/assets/8eb51732-99a7-4011-b5b0-49f9cd6e0e4d" />

But a well-developed graphical interface is available through a program called GitHub Desktop.

In the simplest sense, **GitHub** is a service that provides a place for "remote" repos that all collaborators can access.
But GitHub is also a website for viewing and working with Git repos.
And the major operations that are done with Git can also be done using GitHub through a web browser. 
For example, here is what it looks like when saving changes through the browser interface:

<img width="1013" height="795" alt="image" src="https://github.com/user-attachments/assets/ad9f8af8-639e-4096-a94c-79b63ad238f5" />

# Git glossary
Here are some terms that are important to understand.

**Clone**: To make a local copy of a Git repository from GitHub or another platform or that copy itself. For example, if you download all the contents of a course assignment repo on your laptop, you have cloned it. Any public repo can be cloned. You can clone private repos if you have access.

**Fork**: A repo that was created as a copy of another or the act of creating this copy. For example, you will have to fork the assignment repos, which will create a copy that is associated with your GitHub account. Any public repo can be forked, and you can fork private repos if you have access.

**Remote**: Describes the version of a repo that is on GitHub or some similar platform or a server that can be used as a central shared copy. When collaborating, contributers pull the latest version of the remote repo, make edits, and then push back to the remote repo.

**Local**: Describes the version of a repo on your laptop or desktop. 

**Merge**: To combine different versions of a repo. Typically this is done automatically without any problems. If two contributors make changes to the same part of a file, merging will have to be done manually.

**Commit**: To create a permanent snapshot of the current version of your repo. This version is also called a commit. Commits are like checkpoints that allow you to see changes or revert back to earlier versions. When committing, a short but informative commit message should be included.

**Pull**: To download new commits from a remote repo and merge them into a local version. The new commits could have been made by a different contributor or yourself, but on a different machine.

**Push**: To upload new commits from a local to a remote repo.
