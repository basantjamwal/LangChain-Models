from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

pokemon_info = [
    "Pikachu is an Electric-type Pokémon known for its loyalty and powerful Thunderbolt.",
    "Charizard is a Fire/Flying-type Pokémon famous for its fiery breath and majestic wings.",
    "Bulbasaur is a Grass/Poison-type Pokémon recognized for the plant bulb on its back.",
    "Squirtle is a Water-type Pokémon loved for its playful nature and strong Water Gun.",
    "Jigglypuff is a Fairy-type Pokémon known for its soothing lullabies that put foes to sleep."
]

query = "what type of pokemon is Pikachu"

doc_embeddings = embedding.embed_documents(pokemon_info)
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding],doc_embeddings)[0]

index , score = sorted(list(enumerate(score)), key = lambda x:x[1])[-1]

print(query)
print(pokemon_info[index])
print("similarity score is:", score) 