# mock-exam
FoCS WS 22/23

# Transponder

Working with spreadsheets, the problem is not uncommon that data you want to be in rows is coming to you as columns or vice-versa. Can you write two methods working on our spreadsheet object to convert data from Columns to Rows and back?

Here are some examples:

The old spreadsheet stored a list of letters per column:

Column 1: "A", "E", "I", "O", "U", "L", "N", "R", "S", "T",
Column 2: "D", "G",
Column 3: "B", "C", "M", "P",
Column 4: "F", "H", "V", "W", "Y",
Column 5: "K",
Column 8: "J", "X",
Column 10: "Q", "Z",

Your shiny new Spreadsheet system instead stores values per letter, so you can look up the column value for a certain letter easily. It also stores the letters in lower-case regardless of the case of the input letters:

"a" is in column 1.
"b" is in column 3.
"c" is in column 3.
"e" is in column 1.
