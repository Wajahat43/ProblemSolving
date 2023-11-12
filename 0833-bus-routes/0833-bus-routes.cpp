class Solution {
public:
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