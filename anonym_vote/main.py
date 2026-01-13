shares = {"A": 10, "B": 20, "C": 20, "D": 50 }
votes = {"Yes": 50, "No": 50 }

def drop_keys(keys: list[str], share_dict: dict[str, int]) -> dict[str, int]:
    """
    Remove specified keys from the dictionary.
    
    Parameters:
    keys (list[str]): List of keys to be removed.
    share_dict (dict[str, int]): Dictionary from which keys will be removed.
    
    Returns:
    dict[str, int]: Updated dictionary with specified keys removed.
    """
    for key in keys:
        share_dict.pop(key)
    return share_dict


def find_keys_with_same_values(share_dict: dict[str, int]):
    from collections import defaultdict
    
    value_groups = defaultdict(list)
    for key, value in share_dict.items():
        value_groups[value].append(key)
    
    # Return groups that have more than one key
    # result = []
    result = share_dict.copy()
    for value, keys in value_groups.items():
        if len(keys) > 1:
            # common_dict = {
            #     "keys": keys,
            #     "value": value * len(keys)
            # }
            # result.append(common_dict)
            result = drop_keys(keys, result)
            key_val = "common_" + "_".join(keys)
            result[key_val] = value * len(keys)

    return result


def check_key_addition(my_dict: dict[str, int], val: int, exc_key: str) -> list[str]:
    counter = 0
    target_keys = []
    for k, v in my_dict.items():
        if k == exc_key:
            continue
        else:
            if (counter + v) < val:
                counter += v
                target_keys.append(k)
            elif (counter + v) == val:
                target_keys.append(k)
                # return f"Found exact match for {val} with key {k}"
            else:
                counter = 0
                target_keys = []

    return target_keys if counter == val else []


def check_share_candidate(share_dict: dict[str, int]) -> dict[int, list[str]]:
    candidates: dict[int, list[str]] = {}
    for k, v in share_dict.items():
        addition_candidates = check_key_addition(share_dict, v, k)
        candidates.setdefault(v, []).append(k)
        if addition_candidates != []:
            candidates[v].append(addition_candidates)
    return candidates


def run(shares, votes):
    temp_shares = shares.copy()
    temp_votes = votes.copy()
    for k, v in shares.items():
        if v in votes.values():
            temp_shares.pop(k)
            temp_votes.pop([i for i, j in votes.items() if j == v][0])
    print("Shares after removing common values with votes:", temp_shares)
    print("Votes after removing common values with shares:", temp_votes)
    processesd_shares = find_keys_with_same_values(temp_shares)
    print("Processed Shares:", processesd_shares)
    print("Share Candidates:", check_share_candidate(processesd_shares))

run(shares, votes)




# processesd_shares = find_keys_with_same_values(shares) # fixed common keys
# print("Processed Shares:", processesd_shares)

# print(check_share_candidate(processesd_shares))