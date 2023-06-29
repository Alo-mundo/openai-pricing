from openai_pricing import OpenAIPricing

p = OpenAIPricing()

p.list_available_models()


model = 'gpt-4-32k'
tokens = 1000 # default value for tokens is 1000 


model_name = p.model_name(model) # get model name

max_tokens = p.get_max_tokens(model) # get the max tokens for a model 

price_prompt = p.get_price(model, type='prompt', tokens=1000) # get the current price per 1,000 tokens in prompt 

price_completion = p.get_price(model, type='completion', tokens=1000) # get the current price per 1,000 tokens in completion  


print('The model', model_name)

print('accepts up to', max_tokens,'tokens.')

print('It costs $', price_prompt,'per 1,000 prompt tokens')

print('and $', price_completion, 'per 1,000 completion tokens.')

# Get an average price per requests with  "p.get_price(model, type='both')". "both" is the default value for the "type" argument and 1000 is the default value for the "tokens" argument.
print('The average value for request is', p.get_price(model, type='both'),'per 1,000 tokens (500 tokens in prompt and 500 pormpt in completion.')