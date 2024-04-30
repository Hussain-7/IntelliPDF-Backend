# # Handle 
# import openai
# import os


# openai_api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = openai_api_key

# def vectorize_text(documents):
#     """Convert text to vector embeddings using OpenAI."""
#     response = openai.Embedding.create(
#         input=[documents],  # OpenAI expects a list of texts
#         model="text-embedding-ada-002"  # Specify the model you want to use
#     )
#     # Assuming we take the first embedding for simplicity
#     return response['data'][0]['embedding']