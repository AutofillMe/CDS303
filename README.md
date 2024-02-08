[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AutofillMe/CDS303/HEAD)

# CDS303
---
Stuff for GMU CDS 303-001

## Note
---
I will be using the Visual Studio Code extension called Better Comments for my code. If you are also using VS Code I highly recommend you get the extension as well.

### How To Sync To This Repo
---

I will be using `git` from the command line to do this.  For those on VS Code, there is a function already built in for cloning from a github repo when you open VS Code, so do that if you can and ignore this.

OTHERWISE:

This is mostly for me since I suck at `git` and I need a cheatsheet on how to use `git`.

#### Getting Started

In a folder of your choosing on your system, open a terminal window at the folder location.\
For example type: `cd C:\Users\username\Desktop` for Windows or `cd /Users/username/Desktop` for Mac.

Type this command and hit enter.
```
git clone https://github.com/AutofillMe/CDS303/
```

Change your terminal directory to the newly created folder with:\
`cd .\CDS303\` for Windows or `cd ./CDS303/` for Mac.

#### Working In the Repo

Run this every time you start working on any file.\
While inside the folder, type:
```
git pull
```
To make sure you're up to date with the repo.

Then, add the file you are working on to stage and track changes with:
```
git add <FILENAME>
```

Once you're ready to commit a change locally (It takes a local snapshot of any file(s) you tracked changes with):
```
git commit -m "<MESSAGE>"
```

Once you're ready to push the files to the repo (Update any changes made locally to the cloud):
```
git push
```
