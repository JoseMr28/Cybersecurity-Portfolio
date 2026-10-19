from username_hunter import UsernameHunter
import argparse


parser = argparse.ArgumentParser(description=" OSINT tool for checking username presence across social media platforms")
parser.add_argument("-u","--username",type=str,required=True,help="Introduce a username to search" )
parser.add_argument("-s","--social",type=str,required=False,nargs="+",help="Social media platforms to search. Multiple platforms can be specified")

args = parser.parse_args()

hunter = UsernameHunter(username=args.username,social_media=args.social)

urls = hunter.build_url()
results = hunter.build_request(urls)
hunter.show_results(results)

    
    

