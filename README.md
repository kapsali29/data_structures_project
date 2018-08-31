# data_structures_project

## Instractions
1. Run `preprocess_data.py`

Initially we run the script preprocess_data.py in order to clean the data from the original file
and to define the size of the test dataset.

2. Run `choose_action.py`

Run the above script to see the choices you have and to interact with the books dataset.

3. Run `main_binary_search.py`.

Run the main_binary_search.py script to apply binary search using the books id in the dataset.

**Binary Search**: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

4. Run `interpolation_search.py`

Run that script to apply interpollation search on the dataset.

Given a sorted array of n uniformly distributed values arr[], write a function to search for a particular element x in the array.

Linear Search finds the element in O(n) time, Jump Search takes O(√ n) time and Binary Search take O(Log n) time.
The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.

5. Run `trie_main.py`

Run that script to apply the TRIE algorithm.


