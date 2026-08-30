
import requests 

class UsernameHunter:
    
    """ Tool for checking username availability accross different social media. """
    
    def __init__(self,username,social_media):
        
        """ Initialize UsernameHunter with a username and select social media for platforms. """
        
        self.username = username 
        self.social_media = social_media 
        self.platforms = {
            "github":{
                "url":"https://www.github.com/user/{username}",
                "method":"Get",
                "expected_Status":200
            },
            "linkedin":{
                "url":"https://www.linkdin.com/user/{username}",
                "method":"GET",
                "expected_status":200
            },
            "instagram":{
                "url":"https://www.instagram.com/user/{username}",
                "method":"GET",
                "expected_status":200
            }
        }
    
    def build_url(self):
        
        """ Build a URL for a selected social media. """
        
        urls =[]
        
        if self.social_media:
            
            for social in self.social_media:
                
                social = social.lower()
                
                if social in self.platforms:
                    
                    template = self.platforms[social]["url"]
                    social_url = template.format(username=self.username)
                    urls.append(social_url)
                
                else:
                    
                    print(f"{social} is not available. Select a Social Media available")
            
        
        return urls
        
    def build_request(self,urls):
        
        """ Send a HTTP GET Request for the provided URLS and stored their Status_Code. """
        
        results = {}
        
        for url in urls: 
            
            response = requests.get(url)
            results[url] = response.status_code
        
        return results
    
    def show_results(self,results):
        
        """ Display the results for the username search. """
        
        for url,status_code in results.items():
            
            if status_code == 200: 
                
                print(f"{url}:{status_code}: Found")
            else:
                print(f"{url}:{status_code}: Not found")
        
          
        
                    
                    
        
    
    
             
             
         
    
     
    