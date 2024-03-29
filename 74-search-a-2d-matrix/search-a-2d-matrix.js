/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
     if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
        return false;
    }
    
    const rows = matrix.length;
    const cols = matrix[0].length;
    
    let left = 0;
    let right = rows * cols - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const midElement = matrix[Math.floor(mid / cols)][mid % cols];
        
        if (midElement === target) {
            return true;
        } else if (midElement < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return false;

};