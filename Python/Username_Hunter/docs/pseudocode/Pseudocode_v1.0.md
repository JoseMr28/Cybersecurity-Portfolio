# Username_Hunter - Pseudocode V1.0

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

    For each result:
      
       If request contains errors:

           Set result as "Request error"
           Set result color to red 

       Else if status_code == 200:

          Set result as "Found"
          Set status_code color to green
          Set result color to green
    
        Else if status_code >= 300 AND status_code < 400:

          Set result as " Redirect"
          Set status_code color to yellow
          Set result color to yellow
    
        Else if status_code == 403:
          
          Set result as " Access Restricted"
          Set status_code color to yellow
          Set result color to yellow

        Else if status_code == 404:

          Set result as " Not Found"
          Set status_code color to red
          Set result color to red
        
        Else:

          Set result as "Unknown"
          Set status_code color to yellow
          Set result color to yellow

            
    
    Add row to table 

End

```