def generatePrompt(user, description, genre):
    prompt = f"{user} is a {description}. Provide the prompt for an interesting situation in {genre} genre, to start a story. Also Provide the prompt for an image generating AI to depict the situation. Start a conversational statement from a character in the situation and take response from the user as input for carrying conversation further. After some conversation again give prompt for new scene and image generating AI to carry the story further. Continue the conversation and new scene cycle till you receive terminate as input"
    
    print(prompt)
    return prompt

# generatePrompt('swati','student at iit roorkee','horror')