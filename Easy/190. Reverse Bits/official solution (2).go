// 190. Reverse Bits

// Runtime: 4 ms, faster than 25.91% of Go online submissions for Reverse Bits.

// Memory Usage: 2.5 MB, less than 25.00% of Go online submissions for Reverse Bits.


// Byte by Byte with Memoization
func reverseBits(num uint32) uint32 {
    ret := uint64(0)
    power := uint64(24)
    var cache = map[uint32]uint64{}

    for num != 0 {
        ret += reverseByte(num & 0xff, cache) << power
        num = num >> 8
        power -= 8
	}

    return uint32(ret)
}

// https://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv
func reverseByte(b uint32, cache map[uint32]uint64) uint64 {
    value, ok := cache[b]
    if ok {
        return value
	}

    value = (uint64(b) * 0x0202020202 & 0x010884422010) % 1023
    cache[b] = value
    return value
}