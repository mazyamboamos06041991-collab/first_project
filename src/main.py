import os 
import dotenv 

# Charge les variables du fichier .env

dotenv.load_dotenv()


def print_author():

       """ Mazyambo Kindumbulanga Amos """

       author = os.getenv("AUTHOR")
       print(f"Auteur du projet : {author}")

def main():

    print("Hello from main!")
    print_author()

if __name__ == "__main__":
   main()




