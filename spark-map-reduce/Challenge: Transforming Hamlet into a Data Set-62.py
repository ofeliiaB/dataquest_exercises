## 2. Extract Line Numbers ##

raw_hamlet = sc.textFile("hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)

def clean(line):
    id = line[0].split("@")[1]
    results = list()
    results.append(id)
    if len(line) > 1:
        for y in line[1:]:
            results.append(y)
    return results
    
hamlet_with_ids = split_hamlet.map(lambda x: clean(x))
hamlet_with_ids.take(10)

## 3. Remove Blank Values ##

hamlet_with_ids.take(5)
real_text = hamlet_with_ids.filter(lambda l: len(l) >1)


hamlet_text_only = real_text.map(lambda x: [l for l in x if l != ""])

hamlet_text_only.take(10)

## 4. Remove Pipe Characters ##

# hamlet_text_only.take(10)

def clean_hamlet_f(line):
    results = []
    for l in line:
        if l == "|":
            pass
        elif "|" in l:
            f = l.replace("|", "")
            results.append(f)
        else:
            results.append(l)
    return results
    

clean_hamlet = hamlet_text_only.map(lambda l: clean_hamlet_f(l))
clean_hamlet.take(10)