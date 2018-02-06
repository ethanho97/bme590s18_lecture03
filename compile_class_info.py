import pandas as pd

def main():
    filenames = collect_all_csv_filenames()
    student_data = read_csv(filenames)
    write_data(student_data, filenames)


def collect_all_csv_filenames():
    from glob import glob
    f = glob('*.csv')
    f.remove('mlp6.csv')
    if 'everyone.csv' in f:
        f.remove('everyone.csv')
    return f


def read_csv(f):
    df = []
    for i in f:
        df.append(pd.read_csv(i, names = ['First Name', 'Last Name', 'netid', 'Git Username', 'Team Name']))
        d = pd.concat(df, axis = 0)
    check_no_spaces(d)
    check_camel_case(d)
    return d


def write_data(d, f):
    d.to_csv('everyone.csv')
    for i in f:
        name = i[0:len(i)-3]
        df = pd.read_csv(i, names = ['First Name', 'Last Name', 'netid', 'Git Username', 'Team Name'])
        df.to_json(name+'json')


def front_space_stripper(s):
    if s[0] == ' ':
        s = s[1:]
    return s

def check_no_spaces(d):
    for i, row in d.iterrows():
        tname = str(row['Team Name'])
        tname = front_space_stripper(tname)
        if ' ' in tname:
            print(tname+' contains space.')
            return
    print('No team names contain a space.')


def check_camel_case(d):
    cc = 0;
    for i, row in d.iterrows():
        tname = str(row['Team Name'])
        tname = front_space_stripper(tname)
        if tname[0].isupper() == 1:
            for j in range(1, len(tname)):
                if tname[j].isupper() == 1:
                    cc += 1;
                    break
    print cc


if __name__ == "__main__":
    main()