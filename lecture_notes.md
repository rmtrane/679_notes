---
title: "Lecture Notes"
author: "Ralph Møller Trane"
date: "9/10/2018"
output: html_document
---

## 9/10 Lecture 2

### Homework due

* create a github account, pick a “professional” name (like your real name)
    * Done!
* install a good text editor
    * Chose Atom because of issues with Julia markdown and Visual Studio Code
* software carpentry introduction: 
    * do “Setup” to download the data and open a terminal, and do “Navigating Files and Directories”. 
    * note all your questions.
        * Fairly simple stuff. Went through shell commands such as `cd`, `ls`, etc. Main takeaways
            - root is `/`
            - relative versus absolute paths using `.` and `..`. **Tip:** In projects, use relative paths as much as possible. 
            - Shortcuts: `.` (current folder), `..` (one level up), `~` (user's home folder), and `-` (previous working directory)
            - `!` can be used to repeat commands. Use `history` to get a list of previous commands, then `!602` will repeat command number 602. 
            
            
### Tips from todays lecture I did not know of:

* `rmdir` to delete directories
* wildcards:
    - `*`: matches zero or more characters
    - `?`: matches exactly one character
    - **Example**: 
        - we have folders `raw_sequences`, `raw-sequences`, and `rawSequences`. If we want to delete just the first two, we can use `rm raw?s*` 
* use `echo` to print the command. 
    - This is useful to check that an expression using wildcards actually expands to what you want it to be. 
    - **Example**:
        - as above. If we use `echo raw?s*`, we will see the expansion done by the shell. I.e. it will print `raw-sequences` and `raw_sequences`.

## 9/12 Lecture 3

### Homework due 

Tips and tricks:

* `wc` for word count. 
    * `-l` for number of lines
    * `-w` for number of words
    * `-c` for number of characters
* `>` send to:
    * send output from command to file:
        * `wc -l *.pdb > lengths.txt`
            * sends number of lines for each .pdb file to new text file named lengths.txt
    * double `>>` will add to the end of an exciting file. 
* `<` specify input
    * send input to command
    * for example, `wc -l < lengths.txt` will send the content of the file to the `wc` command, not the file. 
* `sort` to sort things.
    * `-n` to sort numerically
    * i.e., `sort -n lengths.txt` will display the content of `lengths.txt` sorted numerically. 
* `head`/`tail` gives you the first/last `n` lines of a file
    * for example, `head -n 4 lengths.txt` will give you the first 4 lines of the file `lengths.txt`. 
* `|` pipe
    * send output from one command to the next
    * for example, `wc -l *.pdb | sort -n | head -n 1` will give the file with the most lines.
* `uniq`
    * removes adjacent duplicated lines. 
    * i.e. if lines 2 and 3 have the same content, line 3 is removed. However, is line 4 is different, but line 5 is the same as 2 and 3, line 5 is NOT removed.
* `cut`
    * can be used to cut a file by a seperator 
    * take a look at the `animals.txt` file in the `data-shell/data` folder. `cut -d , -f 2 animals.txt` will return the second column after defining columns by comma. 
* extra tidbit on wildcards `*`
    * we can use `[AB]` to match `A` OR `B`. So, for example, in the folder `data-shell/north-pacific-gyre/2012-07-03`, we can use `ls *[AB].txt` to show all files where the last letter before `.txt` is `A` OR `B`. 
    
    
## Homework Assignment 1

### Exercise 2

* Use \` around code to evaluate first before saving to variable.
    * might be the same thing as `(...)`?? Do more testing!


## 9/17 Lecture 4

Looking at `less` and `more`. Using `less`:

* type `g`to go to first line
* type `G` to go to last line
* search forward using `/`
* search backwards using `?`
* `n` (for next) to repeat previous search

On using `grep` 
* use `-w` to specify search for phrases only
    - for example `grep -w The haiku.txt` returns only lines where the word `The` is found, not the line where `Thesis` is found.
    - `grep -w "is not" haiku.txt` return line with `is not`
* `-n` will return numbered lines
* `-i` will force the search to be case-insensitive
* `-v` inverts the search, i.e. returns lines where the pattern is NOT found
* `-E` will perform the search using regular expressions
    - this means you can perform complicated querries that might for example include wildcards
* you can pipe content to grep to search content rather than file
    - `echo "orchestra and band" | grep "and"` 
* `--color` will color code matches
* `-o` returns only matches


On using `find`
* use `-type d` to specify "find directories"
* use `-type f` to specify "find files"
* use `-name` to specify a specific name to look for
    * for example `-name *.pdf`
* use `-d`for depth 
    * for example `-d 1` for this directory only, `-d 2` for this directory and subdirectories



Note on quotes: (go to folder `data-shell/writing`)
* no quotes, double quotes and single quotes are used to control how much the shell should expand/interpret
    * no quotes: expansion of expression first, then execute
        * `echo *.txt` is expanded to `echo haiku.txt`
    * double quotes interprets variables, but does not expand
        * `echo "*.txt and this is my shell: $SHELL"` will become `.txt and this is my shell: /bin/bash`.
    * single quotes ensures nothing is interpreted or expanded
        * `echo "*.txt and this is my shell: $SHELL"` will become `.txt and this is my shell: $SHELL`.

Command substitution with `$()`: 


`xargs`: 
* use what you provide as argument to command instead of input
    * `find . -name '*.txt' | wc -l` vs `find . -name '*.txt' | xargs wc -l`
        - note the use of single quotations. This ensures that we get list of all files ending with `.txt`, not just files from the current folder

### Regular Expressions


- `.`: any one character
- `^`: beginning of the line (only if placed first)
- `$`: end of line (only if placed last)
- `[aBc]`: anything in `a` or `B` or `c`
- `[^aBc]`: anything but... i.e. negation of above
- `\w`: any word character: letter, number, or "_". Also `[[:alnum::]_]`. (`[:alnum:]` means any alphanumeric character. Include `_` to get alphanumeric of underscore)
- `\W`: opposite of `\w`, i.e. not word
- `\d`: any single digit. Also: `[[:digit:]]` or `[0-9]`. 
- `\D`: opposite of `\d`, i.e. not digit
- `\s`: any white character: single space, `\t`(tab), `\n` (line feed), `\r` (carriage return). Also `[[:space:]]`
- `\S`: opposite of `\s`. I.e. not white character
- `\b`: 
- `+`: one or more of previous 
- `?`: zero or one of the previous
- `*`: zero or more of the previous
- `{4}`: 4 of the previous
- `{4,6}`: between 4 and 6 of the previous
-  `{4,}`: 4 or more of the previous


Some practice with `grep`:

```{bash}
## Simply displays the text
echo abc a g ef$ g
## Returns the strings with all a's colored
echo abc a g ef$ g | grep --color 'a'    # 2 matches
## Returns the strings with only the first a colored (because of ^)
echo abc a g ef$ g | grep --color '^a'   # 1 match only: first one
## Returns the strings with all g's colored
echo abc a g ef$ g | grep --color 'g'    # 2 matches
## Returns the strings with only the last all g colored (because of $)
echo abc a g ef$ g | grep --color 'g$'   # 1 match
## Returns nothing since the last character isn't f
echo abc a g ef$ g | grep --color 'f$'   # no match
## Returns nothing since the last two characters aren't 'f$'
echo abc a g ef$ g | grep --color 'f\$'  # match. mind the single quotes.
## Why does this match? Why isn't $ interpreted as variable begin? A: $ when placed at the end of the line, is interpreted as end of line. When it is not end of line, it is interpreted as \$. 
echo ^abc a g ef$ g | grep --color '$ '  # match
## No match, since the first character isn't a
echo ^abc a g ef$ g | grep --color '^a'  # no match
## Match because of `\` -- this ensures that we look for the character
echo ^abc a g ef$ g | grep --color '\^a' # match
## Match -- the first two characters are `^a`
echo ^abc a g ef$ g | grep --color '^^a' # match
```

```{bash}
cd vsbuffalo/bds-files/chapter-03-remedial-unix/

## First, get all lines where the first character is NOT ">", (-v specifies line) then every line that contains caracters that are not ACGTacgt. 
grep -v "^>" tb1.fasta | grep -on [^ACGTacgt]

## Alternatively, specify case insensitivity
grep -v "^>" tb1.fasta | grep -oni [^acgt]
```



## 9/24 Lecture: Introduction to git

* Snapshots of a project. commit = snapshot
* git stores the changes between snapshots/commits, not complete files
* data is stored in a special `.git` directory
* easily restore project at a previous snapshot
* each collaborator has the project on their local machine, and then there's a remote copy on GitHub. Collaborators "pull" from and "push" to GitHub.

To get a log of changes, use `git log`. 


## 9/26 Lecture: More on git

* To turn a git repository into a normal folder, simply delete the .git folder
* `git push`: transfer local changes to github
* `git pull`: transfer changes from github to local repository
* `git clone`: clone a github repository to a new local repository
* `git remote -v`: check if any remote repositories are connected to the local repository
* `git remote add ...`: add local repository to remote repository

To remove something already added (say you did `git add .` and regret including `proj.Rproj`....), do `git rm --cached proj.Rproj`. 














