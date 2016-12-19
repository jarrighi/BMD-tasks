# Bright.MD Take Home Tasks

This is my code challenge submission for a Developer position at Bright.MD

## Task 1: Globophone

### Feature specs

These are somewhat reorganized from the prompt to represent how I plan to implement the features

Page Structure

+ Text field exists
+ Phone number field exists
+ Save button exists
+ Confirmation section hidden initially
+ Go Back button exists within hidden confirmation section


Phone number Validation

* Validate number field not blank
* Validate number field 10 or 11 digits
* Validate number field doesn't start with 0
* Validate number field spaces, dots, dashes okay
* Validate number field alpha and special characters not okay


Save a number

+ Clicking save adds name and number to localStorage
* Clicking save sends user to success message
* Can't click save without a name
* Can't click save on invalid number


Delete a number

* Visible only if number data in localStorage
* Clicking delete button removes data from localStorage


Confirmation section

* Visible immediately after clicking save


Data persists over browser sessions

### How to use it

1. Simply visit [LINK] to interact with the page.

    or 

1. The whole thing is contained in one page, so this should work by downloading the globophone.html file and loading it in a browser.


### Additional notes

## Task 2: Book Search

### Feature specs

These are somewhat reorganized from the prompt

Basic usage 

* Usage: yourbookprogram word1 word2 ...
* Output: id and title for each book that matches any word


Search

* Allow user to match words case-insensitively is desired
* Punctuation surrounding words should be ignored


Performance 

* Searches run in constant time (O(1)) with respect to a single word
* Multiple word searches linear (O(n)) with respect to number of words
    

### How to use it

#### Running the search

#### Running the tests

### Additional notes