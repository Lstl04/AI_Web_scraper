from scrapper import get_website_content_and_clean
from ai import format_content_with_ollama

def main():
    print("Welcome to my AI scrapper")
    input1 = input("What is the wesbite you want to scrap?: ")
    cleaned_content = get_website_content_and_clean(input1)
    input2 = input("Please explain what do you want to get form this website, the more details the better: ")
    formatted_content = format_content_with_ollama(cleaned_content, input2)
    print(formatted_content)

main()
