class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> h = new HashSet<>();
        for(int number:nums){
            if(h.contains(number)){
                return true;
            }
            h.add(number);
        }
        return false;
    }
}