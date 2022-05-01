assuming you have Python 3 installed (to check run `python3 --version`, you should see something like `python 3.9.10`)
in the Terminal run `git clone https://github.com/annavlz/random-seq-gen.git`
then `cd random-seq-gen`

`musicxml2ly <name of the .musicxmlfile>` will create a .ly with the same name
`lilypond <name of .ly file.>` will create a pdf with the same name
`ly musicxml <name of .ly file> > <name of new file>` will create a musicxml file with the same name

To install numpy `pip3 install numpy`
To install ly `pip3 install python-ly`

To run the main script `python3 main.py -f <file name without extension>`
Example `python3 main.py -f part1`
It will use `part1.json` file as input, and will write output to `part1.txt` file.

1. Create file in Sibelius and export it as musicxml
2. run `musicxml2ly part1.musicxml` 
3. open `part1.ly` and copy notes only to `part1.json`
4. update parameters and edit the string to match the example
5. run `python3 main.py -f part1`
6. create `part1_output.ly` by copying `example.ly`
7. open `part1.txt` and copy voices to `part1_output.ly`, remember to add `\relative <>` to the voices
8. run `ly musicxml part1_output.ly > part1_output.musicxml`
9. open `part1_output.musicxml` in Sibelius

Voices structure:
all voices [
    voice [ cell [ string "", number n ], cell [ ... ], cell [ ... ]],
    voice [ ... ]
]