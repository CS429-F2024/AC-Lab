#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>


/**
 * A struct representing a student. The various fields
 * will be compared in the compare() function.
 */
typedef struct student {
  char initials[3];         // 1
  int credits;              // 2
  float gpa;                // 3
  struct student *ta;       // 4
  bool is_honors;           // 5
} student_t;

/**
 * A struct that represents a node of a binary tree.
 * It contains pointers to its 2 children and 1 piece of data.
 */
typedef struct tree_node {
  struct tree_node *left, *right;
  uint64_t data;
} node_t;

/**
 * A struct that contains a pair of coordinates.
 * This will be used in the diamond_center function.
 */
typedef struct coords {
  unsigned long row, col;
} coordinates_t;

// Week 1:

/**
 * popcount_byte function
 *
 * Given a uint64, return a uint64 such that each byte of the return value
 * stores the number of 1 bits in the corresponding byte of the input value.
 * 
 * @param input the bit-string to run the popcount on.
 * @return an 8-vector of eight 8-bit popcounts.
 */
uint64_t popcount_byte(uint64_t input);

/**
 * transpose function
 *
 * Given a uint64 that represents an 8x8 bit matrix, perform a transpose of
 * this matrix and return the resultant matrix. You can realize this function
 * using 3 applications of an Outer Perfect Shuffle.
 * 
 * @param input the bit-string representing an 8x8 bit matrix
 * @return the transposed matrix, also in bit-string form.
 */
uint64_t transpose(uint64_t input);

/**
 * compare function
 * 
 * Given two pointers to student_t structs, perform a field-by-field
 * comparison and return 0 if the two structs have the same field values.
 *
 * Compare characters, ints via numerical comparison.
 * Compare floats as raw binary strings, disregarding their numerical value.
 * Compare pointers by seeing if they point to the same memory location.
 * 
 * @param a a pointer to the first struct to compare
 * @param b a pointer to the second struct to compare
 * @return a uint64_t representing the ordinal position of the first field
 *          that the two structs differ. For example if the structs first
 *          differ in the "gpa" field, return 3.
 */
uint64_t compare(student_t *a, student_t *b);

// Week 2:

/**
 * change_case function
 *
 * Given a pointer to a string, modify the case of the string according
 * to the flag. If the flag is true, make the string uppercase. If it
 * is false, make the string lowercase. Ignore non-alphabetical characters
 * in the string (that is, keep them the same).
 * 
 * This function modifies the string in-place. It does NOT create a new
 * string or copy it to a different location.
 *
 * @param str a pointer to the string to modify.
 * @param flag the flag to specify uppercase or lowercase operation.
 * This function does not return any value.
 */
void change_case(char *str, bool flag);

/**
 * tree_depth function
 * 
 * Given a pointer to the root of a binary tree, return the depth of the tree.
 * The tree is not necessarily complete or balanced.
 * A tree with only 1 node (the root) has depth 1.
 * This function must use recursion.
 *
 * @param root a pointer to the root node of the tree.
 * @return the depth of the tree.
 */
uint64_t tree_depth(node_t *root);


void diamond_center(uint64_t screen, coordinates_t *coords);

#endif
