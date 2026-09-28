class Solution {
    public int maxDepth(String s) {
        int depth = 0;
        int max_depth = 0;
        for(char ch: s.toCharArray()){
            if(ch == '('){
                depth++;
                max_depth = Math.max(max_depth, depth);
            }
            else if(ch == ')'){
                depth--;
            }
        }
        return max_depth;
    }
}