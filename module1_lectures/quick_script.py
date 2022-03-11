tile_conv = 0.5625

def num_tile(length, width):
    """Compute the number of 9 inch 
       tile for a room of area length*width
       
       Args:
           length: a number that is length of the room in feet
           width: a number that is width of the room in feet
           
       Returns:
           A number representing the number of 9 inch tile 
           needed to tile the room
    """
    output = length*width*tile_conv
    return output

def test_num_tile():
    assert num_tile(10, 12) == 67.5
    assert num_tile(0, 12) == 0
    
test_num_tile()