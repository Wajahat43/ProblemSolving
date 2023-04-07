class Solution {
public:
//This can be done by doing a dfs on each cell. 
    //if we go out of bounds we return 1
    //if we reach a 0 or already visited cell we return 1
    //we also keep track of current size of adjacent cells with value 1. And add it to our answer.
 int visit(vector<vector<int>>& grid, vector<vector<bool>>& visited, int i, int j, int& size){
        if(i < 0 || j < 0 || i == grid.size() || j == grid[i].size())
            return 0;
        if(visited[i][j] == true || grid[i][j] == 0)
            return 1;
        int result = 0;
        visited[i][j] = true;
        size++;
        result += visit(grid,visited,i+1,j,size);
        result += visit(grid,visited,i-1,j,size);
        result += visit(grid,visited,i,j+1,size);
        result += visit(grid,visited,i,j-1,size);
        if(result == 4)
            return 1;
        return 0;
    }
    int numEnclaves(vector<vector<int>>& grid) {
        vector<vector<bool>> visited (grid.size(),vector<bool>(grid[0].size(),false));
        int ans = 0;
        int pieceSize = 0;
        for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[i].size();j++){
                if(visited[i][j] == false && grid[i][j] == 1){
                    if( visit(grid,visited,i,j,pieceSize) == 1)
                        ans += pieceSize;
                    pieceSize =0;
                }
            }
        }
        return ans;
        
    }
};