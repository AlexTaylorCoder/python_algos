matrix = (
    (0,3,2,0,0),
    (0,4,1,0,0),
    (0,5,0,0,0),
    (0,6,0,0,0),
    (0,7,8,0,0)
)
midy = len(matrix) // 2
midx = len(matrix[midy]) // 2


def find_peak(md,mdx):
    while mdx > 1:        
        mdx = mdx // 2
        if matrix[md][mdx+1] <= matrix[md][mdx] >= matrix[md][mdx-1]:
            if matrix[md+1][mdx] < matrix[md][mdx] and matrix[md-1][mdx] < matrix[md][mdx]:
                
        if matrix[md][mdx+1] > matrix[md][mdx]:
            #Return right side
            find_peak(matrix[mdx:])
        if matrix[md][mdx-1] > matrix[md][mdx]:
            #Return left side
            find_peak(matrix[:mid])

    

        
            
find_peak(midy,midx)

