//link -https://www.codingninjas.com/studio/problems/data-type_8357232


/*
    Time complexity: O(1)
    Space complexity: O(1)
*/

int dataTypes(string type) {

    // Checking 'type' with all the data types we know.

    if (type == "Integer")
        return 4;
    else if (type == "Long")
        return 8;
    else if (type == "Float")
        return 4;
    else if (type == "Double")
        return 8;
    else if (type == "Character")
        return 1;
    else // 'type' should have matched with some data type above
        return -1; // Should not be returned
}

---------------------------python-----------------------------
'''
    Time complexity: O(1)
    Space complexity: O(1)
'''

def dataTypes(type):
    # Checking 'type' with all the data types we know.
    if type == "Integer":
        return 4
    elif type == "Long":
        return 8
    elif type == "Float":
        return 4
    elif type == "Double":
        return 8
    elif type == "Character":
        return 1
    else:
        # 'type' should have matched with some data type above, this line should not be reached
        return -1  
