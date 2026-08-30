from username_hunter import UsernameHunter
import argparse
import requests

parser = argparse.ArgumentParser(description=" This tool allows you to check if a username is used in a Social Media")
parser.add_argument("-u","--username",type=str,required=True,help="Introduce a username to search" )
parser.add_argument("-s","--social",type=str,required=False,nargs="+",help="Introduce the social media which you want to seach. You can introduce more than one")

args = parser.parse_args()

hunter = UsernameHunter(username=args.username,social_media=args.social)

urls = hunter.build_url()
results = hunter.build_request(urls)
hunter.show_results(results)

    
    

