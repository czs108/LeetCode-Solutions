// 190. Reverse Bits

// Runtime: 4 ms, faster than 25.91% of Go online submissions for Reverse Bits.

// Memory Usage: 2.5 MB, less than 25.00% of Go online submissions for Reverse Bits.


// Bit by Bit
func reverseBits(num uint32) uint32 {
    ret := uint32(0)
    power := uint32(31)
    for num != 0 {
        ret += (num & 1) << power
        num = num >> 1
        power -= 1
    }

    return ret
}