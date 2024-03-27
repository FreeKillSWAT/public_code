import openai

openai.api_key = "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"

completion = openai.Completion.create(engine="text-davinci-003",
                         prompt="",
                         max_tokens=2048)

print(completion.choices[0].text)