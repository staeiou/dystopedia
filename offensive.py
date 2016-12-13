import re

offensive = re.compile(
    r"\b(deaths?|dead(ly)?|die(s|d)?|hurts?|(sex(ual(ly)?)?|child)[ -]?(abused?|trafficking|assault(ed|s)?)|"
    r"injur(e|i?es|ed|y)|kill(ing|ed|er|s)?s?|wound(ing|ed|s)?|fatal(ly|ity)?|shoo?t(s|ing|er)?s?|"
    r"crash(es|ed|ing)?|attack(s|ers?|ing|ed)?|murder(s|er|ed|ing)?s?|hostages?|rap(e|es|ed|ist|ists|ing)|"
    r"assault(s|ed)?|pile-?ups?|massacre(s|d)?|sex|bitch|nigg|pussy|fag|gay|fuck|shit|piss|kill|assassinate(d|s)?|sla(y|in|yed|ys|ying|yings)|"
    r"victims?|tortur(e|ed|ing|es)|execut(e|ion|ed|ioner)s?|gun(man|men|ned)|suicid(e|al|es)|"
    r"bomb(s|ed|ing|ings|er|ers)?|mass[- ]?graves?|bloodshed|state[- ]?of[- ]?emergency|"
    r"al[- ]?Qaeda|blasts?|violen(t|ce)|lethal|cancer(ous)?|stab(bed|bing|ber)?s?|casualt(y|ies)|"
    r"sla(y|ying|yer|in)|drown(s|ing|ed|ings)?|bod(y|ies)|kidnap(s|ped|per|pers|ping|pings)?|"
    r"rampage|beat(ings?|en)|terminal(ly)?|abduct(s|ed|ion)?s?|missing|behead(s|ed|ings?)?|"
    r"homicid(e|es|al)|burn(s|ed|ing)? alive|decapitated?s?|jihadi?s?t?|hang(ed|ing|s)?|"
    r"funerals?|traged(y|ies)|autops(y|ies)|child sex|sob(s|bing|bed)?|pa?edophil(e|es|ia)|9(/|-)11|"
    r"Sept(ember|\.)? 11|genocide)\W?\b",
    flags=re.IGNORECASE)


def tact(headline):
    # Avoid producing particularly tactless tweets
    if re.search(offensive, headline) is None:
        return True
    else:
        return False
