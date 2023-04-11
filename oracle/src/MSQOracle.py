def middle_square_predict_n(sequence):
    digits  = len(str(sequence[0]))
    last_number = sequence[-1]
    seed_str = str(last_number**2).zfill(digits*2)
    mid = len(seed_str) // 2
    return int(seed_str[mid-digits//2:mid+digits//2])


sequence = [6521,5234,3947,5788,5009,900,8100,6100,2100,4100,8100,6100,2100,4100,8100,6100,2100,4100,8100]  # middle square sequence
next_number = middle_square_predict_n(sequence)
print(next_number)


# to generate MSQ sequence https://sadale.net/27/online-middle-square-method-generator