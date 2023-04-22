# PE_2023_Happiness_Counter

There is a **list of n integers**. There are also **2 disjoint sets**, **A** and **B**, each containing **m integers**.
You like all the integers in set **A** and dislike all the integers in set **B**. 
Your initial happiness is **0**. 
For each integer **i** in the list, if **i belongs to A**, you add **1** to your happiness. If **i belongs to B**, you add **-1** to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

*Note* 
Since A and B and are sets, they have no repeated elements. However, the array is a list, and might contain duplicate elements.

*Constraints*
- Input Format
The first line contains integers **n** and **m** separated by a space.
The second line contains **n integers**, the elements of the list.
The third and fourth lines contain **m integers**, **A** and **B**, respectively.

- Output Format
Output a **single integer**, your total happiness.

- Sample Input
3 2
1 5 3
3 1
5 7

- Sample Output
1

- Explanation of the sample output
You gain unit of happiness for elements 1 and 3 in set A. You lose unit for 5 in set B. 
The element 7 in set B does not exist in the list so it is not included in the calculation.
Hence, the total happiness is 1.
