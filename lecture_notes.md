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
            - relative versus absolute paths using `.` and `..`. **Tip**: In projects, use relative paths as much as possible.
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

```bash
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

```bash
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

### Merges

This is important!! When you `git pull` and the online repository has changes that are not directly compatible with your own local repository,


## 10/1 Lecture:

### From homework:

* `"$@"` means "all arguments", i.e. `"$1"`, `"$2"`, ...
* `bash -x` will enable debug mode. For loops, for example, each iteration of the loop will be printed to the console
* `grep -r` will search recursively through files


### In lecture:

* When using `less`, use option `-S` to only display the portion of the lines that fit the console
* re: `cut`
    - uses `tab` as the default delimiter
    - `-f2` selects second field
    - `-f1-3` selects fields 1 through 3
* `sort`
    - use `-k1,1` to sort by column 1 to 1.
        - say we want to sort by the first two columns, but the second column is numeric (i.e. 8 should be before 10). Then using `sort -k1,2` won't work. We need to specify that column 2 is numeric. Instead, we do `sort -k1,1 -k2,2n`
    - use `-t` to specify what character you want to separate columns by
* `column`
    - format output nicely in a tabular way
* `sed` (stream editor)
    - most important use: substitute things
    - example `sed s/pattern/replacement/ filename > newfile`
    - DO NOT redirect to input file
    - options:
        - `s///` will replace first occurance of a match
        - `s///g` replaces all instances
        - `s///i` and `s///gi` as above, but case-insensitive
        - `-E` for extended regular expressions
        - `-n` does NOT print every line
        - `s///p` will print if there is a match
    - example:
        - `echo "chr12:74-431" | gsed -E 's/^(chr[^:]+):([0-9]+)-([0-9]+)/\1\t\2\t\3/'`
            - every set of parenthesis will be saved in memory, and is then returned when `\1`, `\2`, and `\3` are called at the end

## 10/3 Lecture:

### Homework:

(See the exercise [here](https://github.com/UWMadison-computingtools-master/lecture-examples/tree/master/tableofSNPs))

To fix column 2, we search for numbers between quotation marks. There is always at least one comma, but the second is only present sometimes. Hence the `?` (i.e. 0 or 1 comma). We send the result to a new file called `tableofSNPs_fixed.csv`.

```bash
sed -E 's/\"([0-9]+),([0-9]+),?([0-9]+)\"/\1\2\3/g' tableofSNPs.csv > tableofSNPs_min_fixed.csv
```

To check that it worked, I use the following line. This will look for chunks of characters that are not commas and replace them with a single space. `wc -lw` then returns the number of lines and the number of words. If the previous command worked, the number of lines times 3 should equal the number of words.

```bash
sed -E 's/([^,]+)/ /g' tableofSNPs_min_fixed.csv | wc -lw
```

The following one-liner switches A's for T's and T's for A's. Since I couldn't figure out how to do two switches at once, I first switched A's with Q's, then T's with A's, and finally Q's with T's.

```bash
sed -E 's/A/Q/g;s/T/A/g;s/Q/T/g' tableofSNPs_min_fixed.csv > tableofSNPs_fixed_min_AT_fixed.csv
```

To check that it worked, I count the number of A's and T's, respectively, in the original file, which should match with the number of T's and A's in the new file.

Number of T's in new file:

```bash
sed -E 's/[^T]+//g' tableofSNPs_fixed_min_AT_fixed.csv | wc -w
```

Number of A's in new file:

```bash
sed -E 's/[^A]+//g' tableofSNPs_fixed_min_AT_fixed.csv | wc -w
```

Number of T's in old file:

```bash
sed -E 's/[^T]+//g' tableofSNPs_min_fixed.csv | wc -w
```

Number of A's in new file:

```bash
sed -E 's/[^A]+//g' tableofSNPs_min_fixed.csv | wc -w
```


### In Lecture

A bunch about permissions (`chmod`), `PATH`, ~/.bash_profile, etc. All very familiar.

Re: `chmod` options:

* `u`, `g`, `o`: user, group, other; `a` for all


## 10/8 Lecture:

### In Lecture

A bunch on git.

* `branch`
* `checkout`
* `merge`
    * When you want to merge, it's important you're on the branch you want to add the changes to.
    * Make sure you have the most recent version, i.e. do `git pull` before you merge.

## 10/10

### In lecture

* `awk`
    * for quick text processing of tabular data
    * `awk pattern { action } filename`
        * look for `pattern`, do `action`
    * pattern: put regexp in slashes "/^chr\d/"
    * if no action is given, line is printed when pattern matched
    * combine patterns with `&&` and `||`
        * if within regular expression, use `|` (just one)
        * examples:
            * `awk '$1 ~ /chr1/ && $3 - $2 > 10' example.bed` not in regular expression
            * `awk '$1 ~ /chr2|chr3/ { print $0 "\t" $3 - $2 }'` in regular expression
    * variables:
        * `$0` = entire line, `$1` = first field, `$2` = second filed, ...
        * `NR` = current record (line) number
        * `NF` = number of fields (columns) on current line
        * example:
            * `awk '{ print $2 "\t" $3 }' example.bed` works like `cut -f2,3`
    * Combare with `<=`, `==`, ...
        * example:
            * `awk '$3 - $2 > 18' example.bed` will print all lines where the pattern `$3 - $2 > 18` is true
    * `awk` comes with its own built-in functions (`exit`, `sub(regexp, replacement, string)`, `substr(string, i,j)`, `split(string, array, delimiter)`, ...)
    * default is to separate fields by tab. Use `-F ","` to change to comma
    * to include shell variables, use `-v t=...`
        * example
            * `awk -v t=$threshold '$3 - $2 > t' example.bed`
    * can do for loops:
        * example
            * calculate mean feature length:
              `awk 'BEGIN{ s = 0 }; { s += ($3-$2) }; END{ print "mean: " s/NR };' example.bed`

* `wget`
    * download data from the internet
    * `-r` if you want to download files recursively
    * `-l` with `-r` to limit the level or maximum depth: `- 1` to go only 1 link away
    * `--accept-regex` to limit what should be downloaded.
        * for example `--accept-regex '\.fasta|\.txt'` will only download files that match `.fasta` or `.txt`
    * `-nd`(`--no-directory`) to not re-create directory hierachy
    * use `--limit-rate=50k` or `-w 1` to wait 1 second between file downloads


## 10/15

### Peer-review

From Hao-Chen's script: `basename -s 'extension' ...` will return the basename without the `'extension'`!

For example, `basename -s '.log' log/bt1.log` will return `bt1`.

### In lecture

SSH into remote machines. `hostname`

When copying from/to remote machine, `scp -p` will preserve time information.

`tmux` instead of `nohup` for multiple processes/running in background while logged out.

## 10/17

### In-lecture

Introduction to python, ipython, jupyter lab/notebook. Using `numpy`, `matlibplot`. See the python notebook `py_lect1_01` [here](../swc-python/data/py_lect_01.ipynb).

## 10/22

### Homework

Finished the loop part of the SCW (find it [here](http://swcarpentry.github.io/python-novice-inflammation/02-loop/)). My work is in [this](loop_exercise.ipynb) jupyter notebook. 


This is a very cool edit. SUPER COOL!!!!