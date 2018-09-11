# recursively fetches all files that end in .py from all sub folders
# and then runs each one using "python [filename.py]"
for script in  `find . -name \*.py -print -type f`; 
    do python "$script"; 
done

read -p "Press enter to continue"

