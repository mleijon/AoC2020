fi = open('p7_input.txt')
contents = dict()


def read_contents():
    for rule in fi.readlines():
        bag = rule.split('bags')[0].strip()
        bag_content = rule.split('bags contain ')[1].strip()[:-1]
        bag_content = [(x.split(' ', 1)[0], x.split(' ', 1)[1].
                        rsplit(' ', 1)[0]) for x in bag_content.split(', ')]
        if bag_content[0][0] == 'no':
            contents[bag] = [('0', 'no other bags')]
        else:
            contents[bag] = bag_content


def contain_shiny_gold(color):
    colors = [x[1] for x in contents[color]]
    if 'no other bags' in colors:
        return False
    if 'shiny gold' in colors:
        return True
    else:
        for color in colors:
            if contain_shiny_gold(color):
                return True
            else:
                continue
        return False


def shiny_gold_contain(color):
    colors = [[x[1]]*int(x[0]) for x in contents[color]]
    print(colors)
    exit()
        # if not item == 'no other bags':
        #     shiny_gold_contain(item)
        #     print(item)


read_contents()
count = 0
for color in contents.keys():
    if contain_shiny_gold(color):
        count += 1
print('The answer to part is: {}'.format(count))
bag_count = 0
shiny_gold_contain('shiny gold')
