class Solution {
    public int reverseDegree(String s) {

        int answer = 0;

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            int position = i + 1;

            int normalPosition = ch - 'a' + 1;

            int reversePosition = 27 - normalPosition;

            answer += reversePosition * position;
        }

        return answer;
    }
}