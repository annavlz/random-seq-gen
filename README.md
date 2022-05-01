assuming you have Python 3 installed (to check run `python3 --version`, you should see something like `python 3.9.10`)
in the Terminal run `git clone https://github.com/annavlz/random-seq-gen.git`
then `cd random-seq-gen`

`musicxml2ly <name of the .musicxmlfile>` will create a .ly with the same name
`lilypond <name of .ly file.>` will create a pdf with the same name
`ly musicxml <name of .ly file>` will create a musicxml file with the same name

To install numpy `pip3 install numpy`

To run the main script `python3 main.py -f <file name without extention>`
Example `python2 main.py -f part1`
It will use `part1.json` file as input, and will write output to `part1.txt` file.