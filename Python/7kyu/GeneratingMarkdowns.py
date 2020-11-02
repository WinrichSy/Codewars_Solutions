#Generating Markdowns
#https://www.codewars.com/kata/5f656199132bf60027275739

def generate_markdowns(markdown, text, url_or_language):
    if markdown == 'link':
        return '['+text+']' +'('+url_or_language+')'

    elif markdown == 'code':
        return '```'+url_or_language+'\n'+ text+'\n```'

    elif markdown == 'img':
        return '!['+text+']' + '('+url_or_language+')'

#OR

MODELS = {
    'link': '[{txt}]({uL})',
    'img':  '![{txt}]({uL})',
    'code': "```{uL}\n{txt}\n```",
}

def generate_markdowns(mkd, txt, url_or_language):
    return MODELS[mkd].format(txt=txt, uL=url_or_language)
