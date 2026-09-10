# Username_Hunter - Pseudocode V0.3

This document contains the pseudocode of the version 0.3

```
Start

Enter the username 

While username is empty:
   
  Receive username from argument

Select the Social Media 

While no social media is selected:

    Display: Social media is empty
    Select the Social Media 
    

For each social media:

    Run the Social media
    Build the URL
    Build the request

    send the request 
    Analyze the response

Show the results using rich

    If status_code == 200:

         Set status_code color to green
         Set result color to green
    
    Else if status_code >= 300 AND status_code < 400:
         
         Set status_code color to yellow
         Set result color to yellow
    
    Else if status_code >= 400 :
         
          Set status_code color to red
          Set result color to red
    
    Add row to table 

End

```