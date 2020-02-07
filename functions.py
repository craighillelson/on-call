""" __doc__ """

def write_dct_to_csv(a, b, c, d):
    """ write dictionary to a csv """
    import csv

    HEADERS = a

    with open(b, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for c in d.items():
            keys_values = (c)
            out_csv.writerow(keys_values)
