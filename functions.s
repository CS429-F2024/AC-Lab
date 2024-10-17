// This is the general format of an assembly-language program file.
    // Written by: REPLACE THIS WITH YOUR NAME AND UT EID
    .arch armv8-a
    .text
    // Code for all functions go here.


    // ***** WEEK 1 deliverables *****
    // Every function starts from the .align below this line ...
    .align  2
    .p2align 3,,7
    .global popcount_byte
    .type   popcount_byte, %function
popcount_byte:
    // (STUDENT TODO) Code for popcount_byte goes here.
    // Input parameter n is passed in X0
    // Output value is returned in X0.



    ret
    .size   popcount_byte, .-popcount_byte
    // ... and ends with the .size above this line.


    // Every function starts from the .align below this line ...
    .align  2
    .p2align 3,,7
    .global transpose
    .type   transpose, %function
transpose:
    // Input parameter buf is passed in X0
    // Output value is returned in X0.



    ret
    .size   transpose, .-transpose
    // ... and ends with the .size above this line.


    // Every function starts from the .align below this line ...
    .align  2
    .p2align 3,,7
    .global compare
    .type   compare, %function
compare:
    // (STUDENT TODO) Code for compare goes here.
    // Input parameter a is passed in X0; input parameter utf8 is passed in X1.
    // There are no output values.



    ret
    .size   compare, .-compare
    // ... and ends with the .size above this line.


    // Every function starts from the .align below this line ...
    .align  2
    .p2align 3,,7
    .global change_case
    .type   change_case, %function
change_case:
    // (STUDENT TODO) Code for change_case goes here.
    // Input parameter utf8 is passed in X0.
    // Output value is returned in X0.



    ret
    .size   change_case, .-change_case
    // ... and ends with the .size above this line.


    // ***** WEEK 2 deliverables *****
    // Every function starts from the .align below this line ...
    .align  2
    .p2align 3,,7
    .global tree_depth
    .type   tree_depth, %function
tree_depth:
    // (STUDENT TODO) Code for tree_depth goes here.
    // Input parameter str1 is passed in X0; input parameter str2 is passed in X1;
    //  input parameter num is passed in X2
    // Output value is returned in X0.



    ret
    .size   tree_depth, .-tree_depth
    // ... and ends with the .size above this line.


    // Every function starts from the .align below this line ...
    .align  2
    .p2align 3,,7
    .global diamond_center
    .type   diamond_center, %function
diamond_center:
    // (STUDENT TODO) Code for diamond_center goes here.
    // Input parameter a is passed in X0; input parameter b is passed in X1.
    // Output value is returned in X0.



    ret
    .size   diamond_center, .-diamond_center
    // ... and ends with the .size above this line.

    
    .section    .rodata
    .align  4
    // (STUDENT TODO) Any read-only global variables go here.
    .data
    // (STUDENT TODO) Any modifiable global variables go here.
    .align  3

