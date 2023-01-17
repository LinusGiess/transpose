# Transposer
This script is a command line tool for transposing a song from one key to another. It uses the argparse library to
handle command line arguments, which allows the user to specify the source key, destination key, and song to be
transposed. The script also has an optional debug flag and test flag that can be used to show additional log output
or run a predefined test.

- source_key: the key to transpose from
- dest_key: the key to transpose to
- song: the song to be transposed, encoded as a list of keys separated by whitespace
- debug: an optional argument, when set to true, will show additional log output for debugging purposes
- test: an optional argument, when set to true, will run a test procedure on a predefined song

The script first defines a chromatic scale of keys as a list of strings, and a constant for the number of keys in 
the scale. Next, two helper functions are defined: get_index (skey) which takes a key as a string and returns the 
integer index of that key in the chromatic scale, and get_key(t) which is the reverse function of get_index() and
takes an index of a key in the chromatic scale and returns the key as a string.
The main function of the script is transpose_song (source_key, dest_key, song)'. 
It calculates the indexes of the source and destination keys using the get_index function, then calculates the
transpose interval by subtracting the source key index from the destination key index. The function then splits 
the song string into a list of individual keys, transposes each key by adding the transpose interval to its index 
and uses the get_key) function to get the transposed key as a string. Finally, it returns the transposed song as a 
list of strings.
The script also provides a way to handle the command line argument passed while executing the script, the user can
pass the source key, destination key and the song to be.
The script can debug log and run the test transposed.
The script also provides: Stop generating procedure on a predefined song.
