# Introduction
This script is a command line tool for transposing a song from one key to another. It uses the argparse library to
handle command line arguments, which allows the user to specify the source key, destination key, and song to be
transposed. The script also has an optional debug flag and test flag that can be used to show additional log output
or run a predefined test.

- source_key: the key to transpose from
- dest_key: the key to transpose to
- song: the song to be transposed, encoded as a list of keys separated by whitespace
- debug: an optional argument, when set to true, will show additional log output for debugging purposes
- test: an optional argument, when set to true, will run a test procedure on a predefined song

The script first defines the chromatic scale of keys as a list of strings, and a constant for the number of keys in 
the scale.

# Helper Functions

## get_index

get_index function which takes a key as a string and returns the 
integer index of that key in the chromatic scale

# get_key

get_key(t is the reverse function of get_index() and takes an index of a key in the chromatic scale and returns the key as a string.

# Tranposer function

The main function of the script is transpose_song(source_key, dest_key, song)'. 

It calculates the indexes of the source and destination keys using the get_index() function, then calculates the
transpose interval by subtracting the source key index from the destination key index. The function then splits 
the song string into a list of individual keys, transposes each key by adding the transpose interval to its index 
and uses the get_key() function to get the transposed key as a string.

Finally, it returns the transposed song as a strings joined together from the list of transposed keys.

# CLI

The script provides a CLI to handle the passed parameter while executing the script, the user can
pass the source key, destination key and the song to be.

The script can output additional debug log messages and run a test routing one a predefined song to be transposed, which is checked against the correct result.

The script also provides:  generating procedure on a predefined song.

# Sample script run

```
$ python transpose.py --source_key=C --dest_key=G --song="G D E F F F E E E D D E D G E E E E E G D E F F F E E E G G F D"       
Transposed Song: D A H C C C H H H A A H A D H H H H H D A H C C C H H H D D C A
```

# Known issues

The script lacks proper input validation and error handling. Specially it will accept invalid keys not present in the chromatic scale and not throw an error. This could be improved in future version.
