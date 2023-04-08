/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    //As the graph is undirected that means if 1-> 2 edge exists, 2->1 edge will also exist.
    //And if simply try to do it recursivly we might be stuck in an infinite loop. 
    //So we create this map to see if we have already made a deep copy a node or note
    unordered_map<Node*,Node*> visited;
    Node* cloneGraph(Node* node) {
        //if node is null return
        if(node == nullptr)
            return nullptr;
        //if we already created deep copy of this node return
        if(visited.find(node) != visited.end()){
            return visited[node];
        }
        //creat deep copy
        Node* res = new Node();
        res->val = node->val;
        res->neighbors.resize(node->neighbors.size());
        //store in map
        visited[node] = res;
        //create deep copy of each node by calling hte cloneGraph function recursively.
        for(int i=0;i<node->neighbors.size();i++){
            res->neighbors[i] = cloneGraph(node->neighbors[i]);
        }
        //return the result;
        return res;
    }
};