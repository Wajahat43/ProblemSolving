class Solution {
public:
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> numsMap;

    // Count the frequency of each element in nums
    for (auto num : nums)
        numsMap[num] += 1;

    // Create a vector of pairs where the first element is the num
    // and the second element is its frequency
    vector<pair<int, int>> freqVec;
    for (auto num : numsMap) {
        freqVec.push_back({num.first, num.second});
    }

    // Sort the vector of pairs based on the frequency of the elements
    sort(freqVec.begin(), freqVec.end(), [](auto &a, auto &b) {
        return a.second > b.second;
    });

    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(freqVec[i].first);
    }
    return result;
}

};