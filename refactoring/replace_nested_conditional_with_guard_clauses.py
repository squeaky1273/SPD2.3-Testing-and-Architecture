# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):
    if 'debug' in line or 'error' in line or not line:
        pos = None
    else:
        start_index = line.find('x:') + 2
        pos = line[start_index:] # from start_index to the end.
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)