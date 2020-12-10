fi = open('p7_input.txt')
contents = dict()


def read_contents():
    for rule in fi.readlines():
        bag = rule.split('bags')[0].strip()
        bag_content = rule.split('bags contain ')[1].strip()[:-1]
        bag_content = [(x.split(' ', 1)[0], x.split(' ', 1)[1])
                       for x in bag_content.split(', ')]
        if bag_content[0][0] == 'no':
            contents[bag] = [('0', 'no other bags')]
        else:
            contents[bag] = bag_content


def give_content(color):
    return contents[color]


read_contents()
print(give_content('shiny crimson'))


