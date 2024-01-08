import tiktoken

codificador = tiktoken.encoding_for_model('gpt-3.5-turbo-16k')
lista_tokens = codificador.encode('Você é um categorizador de produtos.')

print(lista_tokens)
print(len(lista_tokens))