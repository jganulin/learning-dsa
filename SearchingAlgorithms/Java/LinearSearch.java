package SearchingAlgorithms;

public class LinearSearch {

    // Searches an array 'input' for 'target'; returns index, or -1 if not found
    public static int linearSearch(int[] input, int target) {
        for (int i = 0; i < input.length; i++) {
           if (input[i] == target) {
               return i;
           }
        }

        return -1;
    }

}
