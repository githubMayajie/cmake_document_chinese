  

# string  
String operations.  


Synopsis

Search and Replace
  string(FIND ```<string>``` ```<substring>``` ```<out-var>``` [...])
  string(REPLACE ```<match-string>``` ```<replace-string>``` ```<out-var>``` ```<input>```...)

Regular Expressions
  string(REGEX MATCH ```<match-regex>``` ```<out-var>``` ```<input>```...)
  string(REGEX MATCHALL ```<match-regex>``` ```<out-var>``` ```<input>```...)
  string(REGEX REPLACE ```<match-regex>``` ```<replace-expr>``` ```<out-var>``` ```<input>```...)

Manipulation
  string(APPEND ```<string-var>``` [```<input>```...])
  string(PREPEND ```<string-var>``` [```<input>```...])
  string(CONCAT ```<out-var>``` [```<input>```...])
  string(JOIN ```<glue>``` ```<out-var>``` [```<input>```...])
  string(TOLOWER ```<string1>``` ```<out-var>```)
  string(TOUPPER ```<string1>``` ```<out-var>```)
  string(LENGTH ```<string>``` ```<out-var>```)
  string(SUBSTRING ```<string>``` ```<begin>``` ```<length>``` ```<out-var>```)
  string(STRIP ```<string>``` ```<out-var>```)
  string(GENEX_STRIP ```<string>``` ```<out-var>```)
  string(REPEAT ```<string>``` ```<count>``` ```<out-var>```)

Comparison
  string(COMPARE ```<op>``` ```<string1>``` ```<string2>``` ```<out-var>```)

Hashing
  string(```<HASH>``` ```<out-var>``` ```<input>```)

Generation
  string(ASCII ```<number>```... ```<out-var>```)
  string(CONFIGURE ```<string1>``` ```<out-var>``` [...])
  string(MAKE_C_IDENTIFIER ```<string>``` ```<out-var>```)
  string(RANDOM [```<option>```...] ```<out-var>```)
  string(TIMESTAMP ```<out-var>``` [```<format string>```] [UTC])
  string(UUID ```<out-var>``` ...)

  


Search and Replace
string(FIND ```<string>``` ```<substring>``` ```<output variable>``` [REVERSE])


Return the position where the given substring was found in
the supplied string.  If the REVERSE flag was used, the command will
search for the position of the last occurrence of the specified
substring.  If the substring is not found, a position of -1 is returned.
string(REPLACE ```<match_string>```
       ```<replace_string>``` ```<output variable>```
       ```<input>``` [```<input>```...])


Replace all occurrences of match_string in the input
with replace_string and store the result in the output.
  


Regular Expressions
string(REGEX MATCH ```<regular_expression>```
       ```<output variable>``` ```<input>``` [```<input>```...])


Match the regular expression once and store the match in the output variable.
All ```<input>``` arguments are concatenated before matching.
string(REGEX MATCHALL ```<regular_expression>```
       ```<output variable>``` ```<input>``` [```<input>```...])


Match the regular expression as many times as possible and store the matches
in the output variable as a list.
All ```<input>``` arguments are concatenated before matching.
string(REGEX REPLACE ```<regular_expression>```
       ```<replace_expression>``` ```<output variable>```
       ```<input>``` [```<input>```...])


Match the regular expression as many times as possible and substitute the
replacement expression for the match in the output.
All ```<input>``` arguments are concatenated before matching.
The replace expression may refer to paren-delimited subexpressions of the
match using \1, \2, ¡­, \9.  Note that two backslashes (\\1)
are required in CMake code to get a backslash through argument parsing.

Regex Specification
The following characters have special meaning in regular expressions:

^
Matches at beginning of input
$
Matches at end of input
.
Matches any single character
\```<char>```
Matches the single character specified by ```<char>```.  Use this to
match special regex characters, e.g. \. for a literal .
or \\ for a literal backslash \.  Escaping a non-special
character is unnecessary but allowed, e.g. \a matches a.
[ ]
Matches any character(s) inside the brackets
[^ ]
Matches any character(s) not inside the brackets
-
Inside brackets, specifies an inclusive range between
characters on either side e.g. [a-f] is [abcdef]
To match a literal - using brackets, make it the first
or the last character e.g. [+*/-] matches basic
mathematical operators.
*
Matches preceding pattern zero or more times
+
Matches preceding pattern one or more times
?
Matches preceding pattern zero or once only
|
Matches a pattern on either side of the |
()
Saves a matched subexpression, which can be referenced
in the REGEX REPLACE operation. Additionally it is saved
by all regular expression-related commands, including
e.g. if(MATCHES), in the variables
CMAKE_MATCH_```<n>``` for ```<n>``` 0..9.

*, + and ? have higher precedence than concatenation.  |
has lower precedence than concatenation.  This means that the regular
expression ^ab+d$ matches abbd but not ababd, and the regular
expression ^(ab|cd)$ matches ab but not abd.
CMake language Escape Sequences such as \t, \r, \n,
and \\ may be used to construct literal tabs, carriage returns,
newlines, and backslashes (respectively) to pass in a regex.  For example:

The quoted argument "[ \t\r\n]" specifies a regex that matches
any single whitespace character.
The quoted argument "[/\\]" specifies a regex that matches
a single forward slash / or backslash \.
The quoted argument "[A-Za-z0-9_]" specifies a regex that matches
any single ¡°word¡± character in the C locale.
The quoted argument "\\(\\a\\+b\\)" specifies a regex that matches
the exact string (a+b).  Each \\ is parsed in a quoted argument
as just \, so the regex itself is actually \(\a\+\b\).  This
can alternatively be specified in a Bracket Argument without
having to escape the backslashes, e.g. [[\(\a\+\b\)]].


  


Manipulation
string(APPEND ```<string variable>``` [```<input>```...])


Append all the input arguments to the string.
string(PREPEND ```<string variable>``` [```<input>```...])


Prepend all the input arguments to the string.
string(CONCAT ```<output variable>``` [```<input>```...])


Concatenate all the input arguments together and store
the result in the named output variable.
string(JOIN ```<glue>``` ```<output variable>``` [```<input>```...])


Join all the input arguments together using the glue
string and store the result in the named output variable.
To join list¡¯s elements, use preferably the JOIN operator
from list() command. This allows for the elements to have
special characters like ; in them.
string(TOLOWER ```<string1>``` ```<output variable>```)


Convert string to lower characters.
string(TOUPPER ```<string1>``` ```<output variable>```)


Convert string to upper characters.
string(LENGTH ```<string>``` ```<output variable>```)


Store in an output variable a given string¡¯s length.
string(SUBSTRING ```<string>``` ```<begin>``` ```<length>``` ```<output variable>```)


Store in an output variable a substring of a given string.  If length is
-1 the remainder of the string starting at begin will be returned.
If string is shorter than length then end of string is used instead.

Note
CMake 3.1 and below reported an error if length pointed past
the end of string.

string(STRIP ```<string>``` ```<output variable>```)


Store in an output variable a substring of a given string with leading and
trailing spaces removed.
string(GENEX_STRIP ```<input string>``` ```<output variable>```)


Strip any generator expressions
from the input string and store the result in the output variable.
string(REPEAT ```<input string>``` ```<count>``` ```<output variable>```)


Produce the output string as repetion of input string count times.
  


Comparison
string(COMPARE LESS ```<string1>``` ```<string2>``` ```<output variable>```)
string(COMPARE GREATER ```<string1>``` ```<string2>``` ```<output variable>```)
string(COMPARE EQUAL ```<string1>``` ```<string2>``` ```<output variable>```)
string(COMPARE NOTEQUAL ```<string1>``` ```<string2>``` ```<output variable>```)
string(COMPARE LESS_EQUAL ```<string1>``` ```<string2>``` ```<output variable>```)
string(COMPARE GREATER_EQUAL ```<string1>``` ```<string2>``` ```<output variable>```)


Compare the strings and store true or false in the output variable.
  


Hashing
string(```<HASH>``` ```<output variable>``` ```<input>```)


Compute a cryptographic hash of the input string.
The supported ```<HASH>``` algorithm names are:

MD5
Message-Digest Algorithm 5, RFC 1321.
SHA1
US Secure Hash Algorithm 1, RFC 3174.
SHA224
US Secure Hash Algorithms, RFC 4634.
SHA256
US Secure Hash Algorithms, RFC 4634.
SHA384
US Secure Hash Algorithms, RFC 4634.
SHA512
US Secure Hash Algorithms, RFC 4634.
SHA3_224
Keccak SHA-3.
SHA3_256
Keccak SHA-3.
SHA3_384
Keccak SHA-3.
SHA3_512
Keccak SHA-3.

  


Generation
string(ASCII ```<number>``` [```<number>``` ...] ```<output variable>```)


Convert all numbers into corresponding ASCII characters.
string(CONFIGURE ```<string1>``` ```<output variable>```
       [@ONLY] [ESCAPE_QUOTES])


Transform a string like configure_file() transforms a file.
string(MAKE_C_IDENTIFIER ```<input string>``` ```<output variable>```)


Convert each non-alphanumeric character in the ```<input string>``` to an
underscore and store the result in the ```<output variable>```.  If the first
character of the string is a digit, an underscore will also be prepended to
the result.
string(RANDOM [LENGTH ```<length>```] [ALPHABET ```<alphabet>```]
       [RANDOM_SEED ```<seed>```] ```<output variable>```)


Return a random string of given length consisting of
characters from the given alphabet.  Default length is 5 characters
and default alphabet is all numbers and upper and lower case letters.
If an integer RANDOM_SEED is given, its value will be used to seed the
random number generator.
string(TIMESTAMP ```<output variable>``` [```<format string>```] [UTC])


Write a string representation of the current date
and/or time to the output variable.
Should the command be unable to obtain a timestamp the output variable
will be set to the empty string ¡°¡±.
The optional UTC flag requests the current date/time representation to
be in Coordinated Universal Time (UTC) rather than local time.
The optional ```<format string>``` may contain the following format
specifiers:
%%        A literal percent sign (%).
%d        The day of the current month (01-31).
%H        The hour on a 24-hour clock (00-23).
%I        The hour on a 12-hour clock (01-12).
%j        The day of the current year (001-366).
%m        The month of the current year (01-12).
%b        Abbreviated month name (e.g. Oct).
%B        Full month name (e.g. October).
%M        The minute of the current hour (00-59).
%s        Seconds since midnight (UTC) 1-Jan-1970 (UNIX time).
%S        The second of the current minute.
          60 represents a leap second. (00-60)
%U        The week number of the current year (00-53).
%w        The day of the current week. 0 is Sunday. (0-6)
%a        Abbreviated weekday name (e.g. Fri).
%A        Full weekday name (e.g. Friday).
%y        The last two digits of the current year (00-99)
%Y        The current year.


Unknown format specifiers will be ignored and copied to the output
as-is.
If no explicit ```<format string>``` is given it will default to:
%Y-%m-%dT%H:%M:%S    for local time.
%Y-%m-%dT%H:%M:%SZ   for UTC.



Note
If the SOURCE_DATE_EPOCH environment variable is set,
its value will be used instead of the current time.
See https://reproducible-builds.org/specs/source-date-epoch/ for details.

string(UUID ```<output variable>``` NAMESPACE ```<namespace>``` NAME ```<name>```
       TYPE ```<MD5|SHA1>``` [UPPER])


Create a universally unique identifier (aka GUID) as per RFC4122
based on the hash of the combined values of ```<namespace>```
(which itself has to be a valid UUID) and ```<name>```.
The hash algorithm can be either MD5 (Version 3 UUID) or
SHA1 (Version 5 UUID).
A UUID has the format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
where each x represents a lower case hexadecimal character.
Where required an uppercase representation can be requested
with the optional UPPER flag.
  

