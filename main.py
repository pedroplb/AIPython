from openai import OpenAI

api_key = input("Digite sua chave: ")

client = OpenAI(
    api_key = api_key
)

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário."
            },
            {
                "role": "user",
                "content": "Gere 5 produtos"
            }
        ]
)

print(resposta.choices[0].message.content)