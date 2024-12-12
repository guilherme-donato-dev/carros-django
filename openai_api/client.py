from openai import OpenAI
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API da OpenAI a partir das variáveis de ambiente
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
        api_key = openai_api_key
)



def get_car_ai_bio(model, brand, year):
    # Prompt formatado corretamente
    message = ''''
    Me mostre uma descirção de venda para o carro modelo {} {}, ano {} em apenas 270 caracteres, fale coisas específicas e técnicas desse modelo de carro.
    '''

    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages = [
            {
                'role':'user',
                'content': message
            }
        ],
        max_tokens=270,
        model='gpt-3.5-turbo'
    )
    
    return response.choices[0].message.content