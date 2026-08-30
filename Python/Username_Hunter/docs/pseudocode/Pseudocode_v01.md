# Username Hunter - Pseudocode V0.1

This document contains the pseudocode of the version 0.1

```
Start

Enter Username 

If username is empty:

   Display: Not valid username
   End 

Build the Url 

Do the HTTP Request

if HTTP response status code == 200:

    Display:Found 
    End 

if HTTP response status code != 200:

   Display:Not Found 
   End

```