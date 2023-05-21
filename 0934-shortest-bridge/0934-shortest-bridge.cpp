class Solution {

public:
    //class to represent X and Y and cost 
    class Val {
    public:
        int x;
        int y;
        int cost = 0;

        Val() {
            x = 0;
            y = 0;
            cost = 0;
        }
        Val(int x, int y, int c = 0) {
            this->x = x;
            this->y = y;
            cost = c;
        }

        bool operator == (const Val& other) {
            return x == other.x && y == other.y;
        }
    };

    //hash function for unordered set
    struct MyHash {
        std::size_t operator()(const Val& obj) const {
            return std::hash<int>()(obj.x) ^ std::hash<int>()(obj.y);
        }
    };

    // Custom equality function
    struct MyEqual {
        bool operator()(const Val& lhs, const Val& rhs) const {
            return lhs.x == rhs.x && lhs.y == rhs.y;
        }
    };
    
    //mark a complete island and add all values to the queue (dfs)
    void markIsland(vector<vector<int>>& grid, int x, int y, int val, queue<Val>& q) {
        //if out of bounds or a 0 cell return
        if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() ||
            grid[x][y] == 0 || grid[x][y] == val)
            return;
        grid[x][y] = val;
        q.push(Val(x, y));

        markIsland(grid, x + 1, y, val, q);
        markIsland(grid, x - 1, y, val, q);
        markIsland(grid, x, y + 1, val, q);
        markIsland(grid, x, y - 1, val, q);
    }

    //visit the q and perform bfs until we reach other island (key value)
    int visit(vector<vector<int>>& grid, queue<Val> q, int key) {
        std::unordered_set<Val, MyHash, MyEqual> visited;

        while (!q.empty()) {
            Val cu = q.front();
            q.pop();

            //if already visited continue
            if (visited.find(cu) != visited.end())
                continue;

            //if we have reached a cell of other island 
            if (grid[cu.x][cu.y] == key)
                return cu.cost;


            if (cu.x + 1 < grid.size() && (grid[cu.x + 1][cu.y] == 0 || grid[cu.x + 1][cu.y] == key))
                q.push(Val(cu.x + 1, cu.y, cu.cost + 1));

            if (cu.y + 1 < grid[0].size() && (grid[cu.x][cu.y + 1] == 0 || grid[cu.x][cu.y + 1] == key))
                q.push(Val(cu.x, cu.y + 1, cu.cost + 1));

            if (cu.y - 1 >= 0 && (grid[cu.x][cu.y - 1] == 0 || grid[cu.x][cu.y - 1] == key))
                q.push(Val(cu.x, cu.y - 1, cu.cost + 1));
            if (cu.x - 1 >= 0 && (grid[cu.x - 1][cu.y] == 0 || grid[cu.x - 1][cu.y] == key))
                q.push(Val(cu.x - 1, cu.y, cu.cost + 1));
            
            visited.insert(cu);

        }
        return INT_MAX;

    }
    
    //We will perform both DFS and BFS in this solution. 
    //DFS to visit all the nodes of first island and BFS to find the shortest path from 
    //any node in first island to our second island.
    int shortestBridge(vector<vector<int>>& grid) {

        bool marked = false;
        queue<Val> q;
        
        //find a first island and mark it
        for (int i = 0; i < grid.size() && !marked; i++) {
            for (int j = 0; j < grid[i].size() && !marked; j++) {
                if (grid[i][j] == 1)
                {
                    markIsland(grid, i, j, 2, q);
                    marked = true;
                }
            }
        }

        return visit(grid, q, 1) - 1;



    }
};