def choice_maker(string):
    string = string.strip(",").split(",")
    ns = ""
    for s in string:
        ns = ns + s.strip().capitalize() + ","
    ns = ns.strip(",")   
    return ns



