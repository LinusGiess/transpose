# Script to transpose the keys of a song into another key

# Sample how to use it:
# python transpose.py --source_key=C --dest_key=G
# --song="G D E F F F E E E D D E D G E E E E E G D E F F F E E E G G F D"

# Use of argparse module for simple command line handling
import argparse

parser = argparse.ArgumentParser(description='Transpose a song into a different keys.')

# The script takes the following arguments
parser.add_argument('--source_key',
                    dest='source_key',
                    action='store',
                    required=True,
                    help='the source key to transpose from')

parser.add_argument('--dest_key',
                    dest='dest_key',
                    action='store',
                    required=True,
                    help='the dest key to transpose to')

parser.add_argument('--song',
                    dest='song',
                    action='store',
                    required=True,
                    help='the song (a list of keys to be transposed separated with whitespace)')

parser.add_argument('--debug',
                    dest='debug',
                    action='store_true',
                    required=False,
                    default=False,
                    help='show additional log output for debugging purpose')

parser.add_argument('--test',
                    dest='test',
                    action='store_true',
                    required=False,
                    default=False,
                    help='run a test procedure on a predefined song')


args = parser.parse_args()

# Chromatic scale
keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

NUMBER_OF_KEYS_IN_THE_CHROMATIC_SCALE = 12

# The get_index function takes one argument which is a key as encoded as a character and returns the integer
# index of that key in the chromatic scale
def get_index(skey):
    x = 0
    # Search through all keys and return if the matching one has been found
    for key in keys:
        if key == skey:
            return x
        x = x + 1

# The get_key function is the reverse function of the get_index function, it takes a index of a key in the
# chromatic scale and returns the key as a character
def get_key(t):
    x = 0

    # If the index is lower than 0 we have to map it to the upper keys
    if t < 0:
        t = t + NUMBER_OF_KEYS_IN_THE_CHROMATIC_SCALE

    # If the index is larger than the maximum in the scale we have to map the index to the lower keys
    if t > 11:
        t = t - NUMBER_OF_KEYS_IN_THE_CHROMATIC_SCALE


    # Go through the scale and return when the matching index has been reached
    for key in keys:
        if t == x:
            return key
        x = x + 1

def transpose_song(source_key, dest_key, song):
    # Calculate the indexes of the source and destination key
    source_key_index = get_index(source_key)
    dest_key_index = get_index(dest_key)

    if args.debug:
        print("source_key_index:" ,source_key_index)
        print("dest_key_index:" ,dest_key_index)

    transpose_interval = dest_key_index - source_key_index

    if args.debug:
        print("half_steps:" ,transpose_interval)

    t_song = []

    # Split the user input into single keys and transpose each individual
    for song_key in song.split():

        song_key_index = get_index(song_key)

        # Transpose the key by adding the transpose interval to its index
        transposed_key_index = song_key_index + transpose_interval

        if args.debug:
            print("Index Of The Transposed Key:" ,transposed_key_index )

        transposed_key = get_key(transposed_key_index)

        if args.debug:
            print("Source Key", song_key, "was transposed to", transposed_key)

        t_song.append(transposed_key)

    if args.debug:
        print("Transposed Chords:", ' '.join(t_song))

    return ' '.join(t_song)

# If in test mode we compare the output for a predefined test song to identify an error in the code
if args.test:
    test_song = "G D E F F F E E E D D E D G E E E E E G D E F F F E E E G G F D"
    transposed_test_song = "D A H C C C H H H A A H A D H H H H H D A H C C C H H H D D C A"
    if transposed_test_song == transpose_song('C', 'G', test_song):
        print("Test passed")
    else:
        print("Test failed, please check code for mistakes")
else:
    transposed_song = transpose_song (args.source_key, args.dest_key, args.song)

    print("Transposed Song:", transposed_song)
