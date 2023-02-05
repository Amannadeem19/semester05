#include <bits/stdc++.h> 
#include<unordered_map>
#include<list>
vector<pair<pair<int, int>, int>> calculatePrimsMST(int n, int m, vector<pair<pair<int, int>, int>> &g)
{
    // Write your code here.
    
//      lets create a adjaency list//
    
    unordered_map <int , list<pair <int, int > >> adj;
    
    for(int i=0; i<g.size(); i++){
        int u = g[i].first.first;
        int v = g[i].first.second;
        int w = g[i].second;
        
        adj[u].push_back(make_pair(u,v));
        adj[v].push_back(make_pair(u,w));
    }
    
    vector<int> key(n+1);
    vector<bool> mst(n+1);
    vector<int> parent(n+1);
    
    for(int i=0; i <= n; i++){
        key[i] = INT_MAX;
        mst[i] = false;
        parent[i] = -1;
    }
    //lets start the algo
    key[1] = 0;
    parent[1] = -1;
    for(int i=1; i <n; i++){
//         node to be selected 
        int u;
        int mini = INT_MAX;
//         find the min vali node 
        for(int v=1; v<=n; v++){
            if(mst[v]==false && key[v] < mini){
                u=v;
                mini = key[v];
            }
        }
//         mark mst true
        
        mst[u] = true;
        
//         check its adj nodes 
        for(auto it:adj[u]){
            int v = it.first;
            int w = it.second;
            if(mst[v] == false && w < key[v]){
                parent[v] = u;
                key[v]  = w;
            }
            
        }
        
    }
    
      
     vector <pair <pair <int , int >, int >>result;
    for(int i=2; i <=n ;i++){
        result.push_back({{parent[i],i}, key[i]});
    }
    
    return result;
    
}
