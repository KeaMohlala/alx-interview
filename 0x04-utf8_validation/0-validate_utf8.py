#!/usr/bin/python3
"""
Validate UTF-8 encoding
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list of int): The data set containing bytes.
        
    Returns:
        bool: True if the data set is valid UTF-8, False otherwise.
    """
    # Number of bytes remaining in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits (because each number represents a byte)
        byte = num & 0xFF
        
        if n_bytes == 0:
            # Check how many 1s are leading the current byte
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1
            
            # 1-byte character (no leading 1s) or invalid UTF-8 (more than 4 leading 1s)
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # This byte must start with '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        # Decrease the byte count for the current character
        n_bytes -= 1
    
    # If there are leftover bytes expected, it's invalid
    return n_bytes == 0
