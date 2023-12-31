# openai-pricing

This repository hosts an unofficial library for OpenAI pricing calculations. Its purpose is to simplify the prediction of costs when using GPT models. The data is obtained from https://gptforwork.com/tools/openai-chatgpt-api-pricing-calculator.

##  Library usage

The module provides just one class, `OpneAIPricing`, which loads the pricing data when instanced and answers about max tokens and costs per tokens (prompt and completion tokens).

Currently, it supports the following models:

- GPT-4 32k
- GPT-4
- GPT-3.5 16k
- GPT-3.5
- Davinci
- Curie
- Babbage
- Ada

This list can be obtained by calling `OpenAIPricing.list_available_models()`.

### Example
-----------

```shell
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
```

Output:

```shell
+--------------+-------------------+
| Model name   | Technical name    |
|--------------+-------------------|
| GPT-4 32k    | gpt-4-32k         |
| GPT-4        | gpt-4             |
| GPT-3.5 16k  | gpt-3.5-turbo-16k |
| GPT-3.5      | gpt-3.5-turbo     |
| Davinci      | text-davinci-003  |
| Curie        | text-curie-001    |
| Babbage      | text-babbage-001  |
| Ada          | text-ada-001      |
+--------------+-------------------+
The model GPT-4 32k
accepts up to 32768 tokens.
It costs $ 0.06 per 1,000 prompt tokens
and $ 0.12 per 1,000 completion tokens.
The average value for request is 0.09 per 1,000 tokens (500 tokens in prompt and 500 pormpt in completion.
```

