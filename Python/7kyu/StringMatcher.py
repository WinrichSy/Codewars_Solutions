#String Matcher
#https://www.codewars.com/kata/565ce4ab24ef4aee6a000074

def is_matching(st, st1, st2):
    return sorted(st.lower().replace(' ','')) == sorted((st1.lower()+st2.lower()).replace(' ',''))
