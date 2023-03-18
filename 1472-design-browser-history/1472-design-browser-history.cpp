class BrowserHistory {
public:
    stack<string> first;
    stack<string> second;
    string current;
    
    
    BrowserHistory(string homepage) {
        current = homepage;
        
    }
    
    void visit(string url) {
        first.push(current);
        current = url;
        second = stack<string>();   
    }
    
    string back(int steps) {
        while(steps > 0 && first.empty() == false){
            second.push(current);
            current = first.top();
            first.pop();
            steps--;
        }
        return current;
        
    }
    
    string forward(int steps) {
        while(steps > 0 && second.empty() == false){
            first.push(current);
            current = second.top();
            second.pop();
            steps--;
        }
        return current;
        
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */