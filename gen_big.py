import os
import re
file_list = [(each[0][-3:], each[0]+'/'+each[2][0]) for each in list(os.walk('./note/'))[1:]]

overview = open('overview.md', 'wt')

pattern = re.compile(r'^(.+?)## 结语', flags=re.DOTALL)
title_pattern = re.compile(r'# \[(.+?)\]\[title\]')

for i, name in file_list:
    f = open(name)
    cont = f.read()
    sub_pat = lambda matched: '# {}:'.format(i) + matched.groups()[0]
    new_cont = pattern.search(cont).groups()[0]
    new_new_cont = title_pattern.sub(sub_pat, new_cont)
    overview.write(new_new_cont)
    f.close()

overview.close()
