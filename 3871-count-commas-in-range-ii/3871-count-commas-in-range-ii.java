class Solution {
    public long countCommas(long n) {
        long count = 0;
        long st = 1000;
        long comma = 1;

        while(st <= n){

            long end = st * 1000 - 1;

            if(end > n){
                end = n;
            }
            count += (end - st + 1) * comma;
            st *= 1000;
            comma++;
        }
        return count;
    }
}