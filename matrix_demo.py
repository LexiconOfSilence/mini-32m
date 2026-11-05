def print_matrix(matrix): 
    for i in range(len(matrix)): 
        row = matrix[i]
        for j in range(len(row)): 
            elt = matrix[i][j] # element
            if j > 0:
                print(f"{elt} ", end = '')
            else: 
                print(f"{elt} ", end = '')
        print()

def main(): 
    # Make a 3 x 4 matrix of zero 
    num_rows = 3 
    num_cols = 4 
    matrix = []
    for i in range(num_rows):
        row = [0] * num_cols
        # for j in range(num_cols):
        #    row.append(0)
        matrix.append(row)
    print_matrix(matrix)
    print(matrix)
    matrix[0][0] = 2
    print(matrix)
    matrix[1][3] = 4 
    print(matrix)

if __name__ == "__main__": 
    main()


