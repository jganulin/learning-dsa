package learning-dsa;

public class SearchAlgorithms {

    // Searches an array of integers 'arr' for int 'target' using linear / simple search
    // Returns the index of 'target' if it's found in 'arr', or -1 if not.
    public static void linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            // If the target was found, return its index.
            if (arr[i] == target) {
                return i;
            }
        }

        // The target wasn't found in the array
        return -1;
    }

    public static void main(String[] args) {
        System.out.println("Placeholder");
    }

}
