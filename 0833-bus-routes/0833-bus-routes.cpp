class Solution {
public:
    /*
    1. Each values in routes is the number of stops ith bus takes. (This is like strongly connected components of a bus).
    2. We can form an adjList of bus stops and use BFS on each stop to reach target. But as there can be 500 buses and each bus can have 10000 stops this increases the search space too much.
    3. Instead for each stop of bus we include the bus number (route number) in its adjList. We can reach all the other stops using this bus.
    4. Instead of running bfs on stops we run it on routes in other words buses instead of stops. As there can be only 500 buses(routes) we can this reduces the search space.
    */
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) {
            return 0;
        }
        
        unordered_map<int, vector<int>> adjList;
        for (int i = 0; i < routes.size(); ++i) {
            for (int j = 0; j < routes[i].size(); ++j) {
                int current = routes[i][j];
                adjList[current].push_back(i);
            }
        }
        
        queue<int> q;
        int cost = 1;
        unordered_set<int> visited;

        for(auto route: adjList[source]){
            q.push(route);
            visited.insert(route);
        }
        

        
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                int route = q.front();
                q.pop();

                for (auto stop:routes[route]){
                    if(stop == target){
                        return cost;
                    }
                    for (auto nextRoute: adjList[stop]){
                        if (visited.find(nextRoute) == visited.end()) {
                            q.push(nextRoute);
                            visited.insert(nextRoute);
                        }
                    }

                }

            }
            cost += 1;
        }
        return -1;
        
    }
};