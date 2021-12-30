def expand_contractions(sent):
    c_l=["can't","n't","'ve","'d","'re","'m","it's","cannot","he's","she's","which's","who's"]
    f_l=["can not"," not"," have"," had"," are"," am","it is","can not","he is","she is","which is","who is"]
    index=0
    for cli in c_l:
        sent=sent.replace(cli,f_l[index])
        index=index+1
    return sent
def get_normalized_matching_score(sent1,sent2):
    sent1=sent1.lower()
    sent2=sent2.lower()
    sent1=expand_contractions(sent1)
    sent2=expand_contractions(sent2)
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sent1=''.join(filter(whitelist.__contains__, sent1))
    sent2=''.join(filter(whitelist.__contains__, sent2))
    w_l1=sent1.split(" ")
    w_l2=sent2.split(" ")
    total_count=len(w_l1)+len(w_l2)
    if total_count==0:
        return 0
    match_count=0
    for w1 in w_l1:
        if w1 in w_l2:
            match_count=match_count+1
    match_score=int((match_count*200)/total_count)
    return match_score