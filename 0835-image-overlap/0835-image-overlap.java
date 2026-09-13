class Solution {
    public int largestOverlap(int[][] img1, int[][] img2) {

        int n = img1.length;
        int maxOverlap = 0;

        for (int rowMove = -(n - 1); rowMove <= n - 1; rowMove++) {

            for (int colMove = -(n - 1); colMove <= n - 1; colMove++) {

                int overlap = 0;

                for (int i = 0; i < n; i++) {

                    for (int j = 0; j < n; j++) {

                        int newRow = i + rowMove;
                        int newCol = j + colMove;

                        if (newRow < 0 || newRow >= n ||
                            newCol < 0 || newCol >= n) {
                            continue;
                        }

                        if (img1[i][j] == 1 &&
                            img2[newRow][newCol] == 1) {
                            overlap++;
                        }
                    }
                }

                maxOverlap = Math.max(maxOverlap, overlap);
            }
        }

        return maxOverlap;
    }
}