def detects_feeling(current_feeling, texto, dados):
    for i in dados[current_feeling]:
        if texto.find(i) != -1:
            return current_feeling

    return ''