
# https://en.wikipedia.org/wiki/Trifid_cipher

def encrypt_message(
    enc_squares: dict[str, tuple[int, int, int]],
    msg: str
) -> str:

    BLOCKS = (len(msg) // 5) + 1
    BLOCK_SIZE = 5

    blocks = []

    # create blocks aligning with 5 characters, 15 numbers in size
    for b in range(BLOCKS):

        block_msg = msg[b*BLOCK_SIZE : b*BLOCK_SIZE + BLOCK_SIZE]

        # create block of (square, row, col)
        block = [list(enc_squares[c.upper()]) for c in block_msg]

        # transpose the block before adding it back in (https://stackoverflow.com/questions/6473679/transpose-list-of-lists)
        block = list(map(list, zip(*block)))

        # flatten the block
        block = [item for sublist in block for item in sublist]

        # add it in
        blocks.append(block)

    encrypted = ""

    # swap our dictionary around to use the tuples as indexes so we can retrieve letters
    square_encs = res = dict((v,k) for k,v in enc_squares.items())

    for b in blocks:

        for i in range(len(b) // 3):
            # 3 elements for each letter: block no, row, col
            sq, row, col = b[i*3], b[i*3 + 1], b[i*3 + 2]
            
            encrypted += square_encs[(sq, row, col)]
        encrypted += " "
    return encrypted

def construct_squares(key: str) -> \
    tuple[dict[str, tuple[int, int, int]], dict[str, tuple[int, int, int]], dict[str, tuple[int, int, int]]]:
    """
    Takes a key as a str and forms the three squares for encryption
    """

    assert len(key) == 27, "Key size should be 27 for 3 blocks of 9"

    def square_up(box_parts: str, box_no: int) -> str:

        return {c : (box_no, i // 3, i % 3) for i,c in enumerate(box_parts)}

    return tuple([square_up(key[i*9:i*9+9], i) for i in range(3)])


def day_of_the_trifids(key: str, msg: str) -> str:
    """
    Encrypts a given string
    """

    # construct squares 1, 2 and 3
    squares = s1, s2, s3 = construct_squares(key)
    # join all the dictionaries together for encryption. Note, all keys should be unique
    enc_squares = s1 
    enc_squares.update(s2)
    enc_squares.update(s3)

    # encrypt message
    enc = encrypt_message(enc_squares, msg)

    return enc

if __name__ == "__main__":

    key = input().strip()
    msg = input().strip().replace(' ', '')


    print(day_of_the_trifids(key, msg))