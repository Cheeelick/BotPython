def main(row):
    ans = {}
    row = row.replace('\n', ' ')
    row = row.replace('<sect>', '')
    row = row.replace('{', '')
    row = row.replace('declare ', '')
    row = row.replace('.</sect>', '')
    row = row.replace(' ', '')
    row = row.replace('list(', '')
    row = row.replace(')', '')
    row = row.replace('#', ' ')
    row = row.replace('.', '')
    row = row.split('}')
    row.pop()
    print(row)
    print('--------------')
    for i in row:
        i = i.split(':=')
        i[1] = i[1].split(' ')
        del i[1][0]
        for j in range(len(i[1])):
            i[1][j] = int(i[1][j])
        ans |= {i[0]: i[1]}
    return ans
    


if __name__ == '__main__':
    print(main('''<sect> { declare indila_599 :=list( #236#-4139 #4537 #-4086 )}. {
declare atbian_251:=list( #-7023 #-2916 #-700 #-9394 ) }. { declare
inso_595 :=list(#-4466 #8650 #-735 #8074 )}.{ declare tiat:=
list(#-7322 #-7334 #2055 )}. </sect>'''))
