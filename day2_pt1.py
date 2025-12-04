text = "2157315-2351307,9277418835-9277548385,4316210399-4316270469,5108-10166,872858020-872881548,537939-575851,712-1001,326613-416466,53866-90153,907856-1011878,145-267,806649-874324,6161532344-6161720341,1-19,543444404-543597493,35316486-35418695,20-38,84775309-84908167,197736-309460,112892-187377,336-552,4789179-4964962,726183-793532,595834-656619,1838-3473,3529-5102,48-84,92914229-92940627,65847714-65945664,64090783-64286175,419838-474093,85-113,34939-52753,14849-30381"

pairs = text.split(",")
result = []
for p in pairs:
    wrapped_pairs = []
    x = p.split("-")
    for i in x:
        stripped = i.strip()
        wrapped_pairs.append([int(stripped)])
    result.append(wrapped_pairs)
# match whole number, not the pears within the number
# 121212.121212
invalid_ids = []
for pair in result:
    f_pair = pair[0]
    s_pair = pair[1]
    print(f"START: {f_pair} END: {s_pair}")
    while f_pair[0] <= s_pair[0]: # going through range
        f_pair[0] += 1
        if len(str(f_pair[0])) % 2 != 0:
            continue
        elif len(str(f_pair[0])) % 2 == 0:
            mid = len(str(f_pair[0])) // 2
            f_half = str(f_pair[0])[:mid]
            s_half = str(f_pair[0])[mid:]
            if f_half == s_half:
                result = [f_half, s_half]
                bleh = "".join(result)
                print(f"result: {result} joined: {int(bleh)}")
                invalid_ids.append(int(bleh))
print(sum(invalid_ids))
            
# join halves then add to arr

# EVEN e.g.: [1,2,2,3,1,2,2,3]
# find len of arr (8)
# split middle [1,2,2,3] [1,2,2,3]
# if both match add to invalid_id arr

# ODD e.g.: [4,4,4]
# continue; since nums muchy match twice

