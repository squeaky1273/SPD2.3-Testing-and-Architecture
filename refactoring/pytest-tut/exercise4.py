# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else: 
                pos = None
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)

def test_extract_position_with_empty_line():
    """Test extraction method with nothing in the line"""
    assert extract_position("") == None

def test_extract_position_with_error():
    """Test extraction method with an error in the line"""
    assert extract_position("error numerical calculations could not converge") == None

def test_extract_position_with_x():
    """Test extraction method with x in the line"""
    assert extract_position("the positron location in the particle accelerator is x:21.432") == '21.432'