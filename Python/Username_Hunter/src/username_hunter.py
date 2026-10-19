
import requests 
from rich.console import Console 
from rich.table import Table

class UsernameHunter:
    
    """ Tool for checking username availability accross different social media. """
    
    def __init__(self,username,social_media):
        
        """ Initialize UsernameHunter with a username and select social media for platforms. """
        
        self.username = username 
        self.social_media = social_media 
        self.platforms = {
            "github":{
                "url":"https://github.com/{username}",
                "method":"Get",
                "expected_Status":200
            },
            "linkedin":{
                "url":"https://www.linkedin.com/in/{username}",
                "method":"GET",
                "expected_status":200
            },
            "instagram":{
                "url":"https://www.instagram.com/{username}",
                "method":"GET",
                "expected_status":200
            },
            "x":{
                "url":"https://x.com/{username}",
                "method":"GET",
                "expected_status":200
                
            },
            
            "facebook":{
                "url":"https://www.facebook.com/{username}",
                "method":"GET",
                "expected_status":200  
            },
            
            "tiktok":{
                "url":"https://www.tiktok.com/@{username}",
                "method":"GET",
                "expected_status":200
            },
            
            "youtube":{
                "url":"https://www.youtube.com/@{username}",
                "method":"GET",
                "expected_status":200
            },
            
            "onlyfans":{
                "url":"https://www.onlyfans.com/{username}",
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
                    urls.append((social,social_url))
                
                else:
                    
                    print(f"{social} is not available. Select a Social Media available")
            
        
        return urls
        
    def build_request(self,urls):
        
        """ Send a HTTP GET Request for the provided URLS and stored their Status_Code. """
        
        results = {}
        
        for social,url in urls: 
            
            try:
                
            
                response = requests.get(url,timeout=10)
            
                results[social] = {
                "url":url,
                "status_code": response.status_code
                }
            
            except requests.RequestException as e:
                
                results[social]={
                    "url":url,
                    "error":str(e)
                }
                
             
            
        return results
    
    def show_results(self,results):
        
        """ Display the results for the username search. """
        
        console = Console()
        table = Table(title="Username Hunter")
        
        table.add_column("Platform",style="cyan",justify="center")
        table.add_column("Status",style="magenta",justify="center")
        table.add_column("Result",style="green",justify="center")
        table.add_column("Url",style="blue")
        
        for social,data in results.items():
            
            if "error" in data:
                
                status = "[red]Error[/red]"
                result = "[red]Request Error[/red]"
                
            elif data["status_code"] == 200: 
                
                status = f"[green]{data['status_code']}[/green]"
                table.add_row(social,status,"[green]Found[/green]",data["url"])
                
            elif data["status_code"] >= 300 and data["status_code"] < 400:
                
                status = f"[yellow]{data['status_code']}[/yellow]"
                table.add_row(social,status,"[yellow]Redirect[/yellow]",data["url"])
            
            elif data["status_code"] == 403:
                
                status = f"[yellow]{data['status_code']}[/yellow]"
                table.add_row(social,status,"[red]Access Restricted[/red]",data["url"])
            
            elif data["status_code"]==404:
                
                status = f"[red]{data['status_code']}[/red]"
                table.add_row(social,status,"[red]Not found[/red]",data["url"]) 
            
            else:
                
                status = f"[yellow]{data['status_code']}[/yellow]"
                table.add_row(social,status,"[yellow]Unknown[/yellow]",data["url"])
                       
        console.print(table)
        
          
        
                    
                    
        
    
    
             
             
         
    
     
    