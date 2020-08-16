def what_to_do(instructions):
    length_instructions = len(instructions)
    index_simon_word = instructions.find("Simon says")
    length_simon_word = len("Simon says")
    if index_simon_word > -1 and \
            (index_simon_word == 0 or index_simon_word + length_simon_word == length_instructions):
        answer = 'I '
        if index_simon_word > 0:
            answer += (instructions[:index_simon_word]).strip(" ")
        elif index_simon_word == 0:
            answer += (instructions[index_simon_word + length_simon_word:]).strip(" ")
        return answer
    else:
        return "I won't do it!"

