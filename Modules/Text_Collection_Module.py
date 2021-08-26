
def Text_Collection(all_templates):
    if isinstance(all_templates, str):
        return "No text can be created"
    
    #amount_rounded = [("", 0.5), ("bijna", 0.2), ("zo'n", 0.2), ("ongeveer", 0.2), ("naar schatting", 0.2), \
     #                 ("rond de", 0.2), ("ruim", 0.3), ("meer dan", 0.3), ("minder dan", 0.3)]
    #rounded_words = [i[0] for i in amount_rounded]
    #rounded_weights = [i[1] for i in amount_rounded]
    #amount_rounded_normalized = [i/sum(rounded_weights) for i in rounded_weights]
    #rounded = np.random.choice(rounded_words, p = amount_rounded_normalized)
    #round_number = round(int(amount))
    
    text = ""
    line = ""
    
    fixed_templates = []
    
    for t in all_templates:
        if not t[0].isupper():
            upper_letter = t[0].upper()
            new_t = upper_letter + t[1:]
        else:
            new_t = t
        
        if line.endswith(".") and (new_t.startswith(":") or new_t.startswith(",")):
            line = line[:-1]    
        elif line.endswith("."):
            line += " "
            
        if t != "\n":
            line += new_t
            
        if all_templates[all_templates.index(t)] != (len(all_templates)-1):
            if all_templates[all_templates.index(t)+1] == "\n":
                fixed_templates.append(line)
                line = ""
                
    #print(fixed_templates)
                   
    for sentence in fixed_templates:
        line2 = ""
        i = 0
        if fixed_templates.index(sentence) == 0:
            text += sentence
            text += "\n\n"
            continue
        
        words = sentence.split(" ")
        for w in words:
            if w[:-1].isdigit():
                if w[-1] == ":":
                    w = "{:,}:".format(int(w[:-1])).replace(",", ".")
                elif w[-1] == ",":
                    w = "{:,},".format(int(w[:-1])).replace(",", ".")
                elif w[-1] == ".":
                    w = "{:,}.".format(int(w[:-1])).replace(",", ".")
                else:
                    w = "{:,}".format(int(w)).replace(",", ".")
            line2 += w + " "
            if len(line2) > 75:
                text += line2 +"\n"
                line2 = ""
            if i == (len(words)-1):
                text += line2
            i += 1
        if not text.endswith("\n"):        
            text += "\n"

    return text
