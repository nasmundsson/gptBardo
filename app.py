import openai
from dotenv import load_dotenv
import os
from ascii import printB

load_dotenv()

# set openai.api_key to your api key
openai.api_key = os.getenv('OPENAI_API_KEY')


def exe(prompt):
    context = """
        You are the narrator of a text based choose your own adventure game. This game is based on the Bardo Thodol. The player will encounter various apparitions and visions in the bardo and must make choices that will inform their next rebirth. 

        I will type commands and you will reply with a description of what the player character sees. I want you to only reply with the game output and nothing else. Please do not write explanations. Every time the player would take an action, stop writing and wait for input. Do not make decisions for the player. Every time the player would make a decision, instead of continuing, stop and wait for player input. Every time you stop and wait for player input, provide a list of options as a list that always ends with “{ something else }” like this:

        { What do you do? }
        Option 1
        Option 2
        Option 3
        { Something else }
    """

    res = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "system", "content": context},
                  {"role": "user", "content": prompt}],
        stream=True
    )
    for chunk in res:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    # ret = res.choices[0].message.content
    # return ret

def main():
    print(printB())
    print('\n')
    print("""Welcome to the gpt Bardo!\nYour actions here will determine your next existence. No pressure.\nType 'start' to begin. Type 'exit' to finish.""")

    while True:
        user_input = input("[You]: ")
        if user_input.lower() == 'exit':
            break

        print('\n\n')

        exe(user_input)
        print('\n')



if __name__ == "__main__":
    main()