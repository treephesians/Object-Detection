def confidence(li, pass_conf, amb_conf):
    filter = "pass"
    print(li)
    ambList = [x for x in li if amb_conf <= x and x < pass_conf]
    print(ambList)
    failList = [x for x in li if x < amb_conf]
    print(failList)
    if len(ambList)>0:
        filter = "amb"
    if len(failList)>0:
        filter = "fail"
    return filter
    