
alpha = ['A','B','C',':D','E','F','G','>:DD','I','J','K',':33','M','N','O','P','Q',';)','S','T','U',':oo','W','X','Y','Z','a','b','c','d','-.-','f','g',":'((",'i','j','k','l',':cc','n','o','p','q',':?','s','t','u','v','w','@.@','y','z','0','1',':L','3','4','5','8==D','7','8','9','69','M.M']


PAD_CHAR = "O.O" 

def encode_block(block: bytearray) -> str:

    # divide each block into 4 groups of 6 bits
    groups = (g1, g2, g3, g4) = (
        (block[0] & 0b11111100) >> 2,                                       # 6 bits of 0
        (((block[0] & 0b00000011) << 4) | ((block[1] & 0b11110000) >> 4)),  # 2 bits of 0, 4 bits of 1
        (((block[1] & 0b00001111) << 2) | ((block[2] & 0b11000000) >> 6)),  # 4 bits of 1, 2 bits of 2
        (block[2] & 0b00111111)                                             # 6 bits of 2
    )

    # map each group to corresponding based64 map
    mappings = m1, m2, m3, m4 = tuple([alpha[g] for g in groups])

    return "".join(list(mappings))
    

def based64(data: bytes) -> str:

    based = ""

    # divide into blocks of 3 bytes (pad last block with 0)
    pad_len = 3 - (len(data) % 3) if (len(data) % 3 != 0) else 0
    based_bytes = bytearray(data, 'utf-8') + b"\x00"*pad_len

    # divide each block into 4 groups of 6 bits
    based_blocks = [based_bytes[i:i+3] for i in range(0, len(based_bytes), 3)]

    # map each 6-bit block to corresponding based64 map
    for block in based_blocks:
        based += encode_block(block)

    # replace last `pad_len` blocks with sanctioned emoji
    if pad_len:
        based = based[:-pad_len] + PAD_CHAR*pad_len

    # done
    return based


if __name__ == "__main__":

    data = input()

    print(based64(data))