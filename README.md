# n2w.py
This python program is used to convert a given number into words. For example, if “1234” is given as input, output should be “one thousand two hundred thirty four”. n2w method takes number in string format  and returns its corresponding word format.up to ten crore format number it is valid.
```sh
>>>n2w('1')
'One'
>>> n2w('111')
'One Hundred Eleven '
>>> n2w('111111')
'One Lakh Eleven Thousand One Hundred Eleven '
>>> n2w('1111111')
'Eleven Lakh Eleven Thousand One Hundred Eleven '
>>> n2w('11111111')
'One Crore Eleven Lakh Eleven Thousand One Hundred Eleven '
>>> n2w('111111111')
'Eleven Crore Eleven Lakh Eleven Thousand One Hundred Eleven '
>>> n2w('1111111111')
wohhhwohhh!! its sooo big 
```
---

# sort_analysis.py
#### Comparison of Sorting Algorithms
This python program is used to analyze different sorting algorithms. sort_analysis returns a list of run times with string representations of 'non-decreasing','decreasing' and 'random' and their respective run times.
values may differ depending upon computer's clock.
Sorting algorithms used:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
```sh
FOR ARRAY SIZE  100
BUBBLE SORT
[['Random', 0.00097], ['Non-Decreasing', 0.00044], ['Decreasing', 0.00121]]
SELECTION SORT
[['Random', 0.0006], ['Non-Decreasing', 0.00059], ['Decreasing', 0.0004]]
INSERTION SORT
[['Random', 0.00176], ['Non-Decreasing', 2e-05], ['Decreasing', 0.00151]]
MERGE SORT
[['Random', 0.00034], ['Non-Decreasing', 0.00026], ['Decreasing', 0.00025]]
QUICK SORT
[['Random', 0.00026], ['Non-Decreasing', 0.00025], ['Decreasing', 0.00029]]
HEAP SORT
[['Random', 0.00044], ['Non-Decreasing', 0.00035], ['Decreasing', 0.00029]]

FOR ARRAY SIZE  1000
BUBBLE SORT
[['Random', 0.0952], ['Non-Decreasing', 0.04673], ['Decreasing', 0.13433]]
SELECTION SORT
[['Random', 0.03748], ['Non-Decreasing', 0.03818], ['Decreasing', 0.03878]]
INSERTION SORT
[['Random', 0.08757], ['Non-Decreasing', 0.00015], ['Decreasing', 0.17286]]
MERGE SORT
[['Random', 0.00397], ['Non-Decreasing', 0.00298], ['Decreasing', 0.0035]]
QUICK SORT
[['Random', 0.00327], ['Non-Decreasing', 0.00296], ['Decreasing', 0.00261]]
HEAP SORT
[['Random', 0.00521], ['Non-Decreasing', 0.00566], ['Decreasing', 0.00532]]

FOR ARRAY SIZE  10000
BUBBLE SORT
[['Random', 10.15551], ['Non-Decreasing', 5.20691], ['Decreasing', 14.91139]]
SELECTION SORT
[['Random', 3.71751], ['Non-Decreasing', 3.85444], ['Decreasing', 3.95274]]
INSERTION SORT
[['Random', 10.11007], ['Non-Decreasing', 0.00163], ['Decreasing', 19.37381]]
MERGE SORT
[['Random', 0.05259], ['Non-Decreasing', 0.03827], ['Decreasing', 0.04146]]
QUICK SORT
[['Random', 0.03224], ['Non-Decreasing', 0.03522], ['Decreasing', 0.03613]]
HEAP SORT
[['Random', 0.0754], ['Non-Decreasing', 0.08027], ['Decreasing', 0.06941]]
```
---
# wordCloud.py
This python program is used to generate a word cloud with the help of wordCloud library in python.Size of the word in wordCloud image is dependent on the number of occurence in text file
 
