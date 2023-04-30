def del_multiple_keys(input_dict: dict, del_keys: [list]):
    for del_key in del_keys:
        del input_dict[del_key]


def pop_multiple_keys(input_dict: dict, pop_keys: [list]):
    for pop_key in pop_keys:
        input_dict.pop(pop_key, None)


def currency_parser(currency_dict: dict) -> str:
    if "keys" and "metal" in currency_dict:
        return (
            str(currency_dict["keys"])
            + " Keys"
            + " "
            + str(currency_dict["metal"])
            + " Refs"
        )
    elif "keys" in currency_dict:
        return str(currency_dict["keys"]) + " Keys"
    elif "metal" in currency_dict:
        return str(currency_dict["metal"]) + " Refs"
    elif "usd" in currency_dict:
        return str(currency_dict["usd"]) + " USD"
    else:
        return ""
