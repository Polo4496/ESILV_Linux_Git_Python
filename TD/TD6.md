# TD6
## Exercise 1: Configure Git
1. Check that Git is installed on your environment.
```
git version
```
2. Configure your name and e-mail globally.
```
git config --global user.name Polo4496
git config --global user.email polo.lejamtel@gmail.com
```
3. Check that Git has correctly recorded these two pieces of information.
```
git config user.name
git config user.email
```
It displays *Polo4496* and *polo.lejamtel@gmail.com*.

## Exercise 2: Basic workflow with a single file
1. Create a git repository
```
mkdir td_git
cd td_git
git init
```
2. Check that git has correctly initiliazed a repository by displaying the files wihtin your current folder
```
ls -a
```
There is a file *.git*.
3. Check the current git status
```
git status
```
4. Create a text file named “readme.md” whose content is “# Test repository”
```
touch readme.md
echo "# Test repository" > readme.md 
```
5. Check the current git status
```
git status
```
6. Stage the file
```
git add readme.md
```
7. Check the current git status
```
git status
```
8. Commit the file
```
git commit -m "Creation Readme.md"
```
9. Check the current git status
```
git status
```
10. Check the git logs
```
git log
```
11. Which informations are displayed ?
```
commit 32e3086b722cc687ab02451bf6f2f6095ea50566 (HEAD -> master)
Author: Polo4496 <polo.lejamtel@gmail.com>
Date:   Mon Mar 6 11:28:19 2023 +0200
    Creation Readme.md
```

## Exercise 3: Basic workflow with multiple files treated separately
1. Create two empty python files named “main.py” and “functions.py”
```
```
2. Check the current git status
```
```
3. Stage only the file “main.py”
```
```
4. Check the current git status
```
```
5. Commit the file with an appropriate message
```
```
6. Check the current git status
```
```
7. Now stage and commit the file “functions.py”
```
```
8. Check the current git status
```
```
9. Check the git logs
```
```
