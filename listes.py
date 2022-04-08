from itertools import count


text = "foo bar baz"
split_text = text.split(' ')
print(split_text)
print(len(split_text))
#print(split_text[3])
split_text.append(123456789)
print(split_text)
print(len(split_text))

list = "Sed sodales congue massa, ultrices posuere mauris. Vestibulum dictum ipsum massa, vitae pharetra purus varius ut. Duis convallis eget elit non vehicula. Sed consequat malesuada lectus, et gravida neque semper sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vitae rhoncus nibh. Fusce ac enim id tellus interdum luctus eu in mauris. Ut a leo nec sem mollis interdum ac eu ligula. In ultricies eros vitae nibh placerat, ac venenatis nisi sollicitudin. "
splitted_list = list.split(',')
list = ''.join(splitted_list)
splitted_list = list.split('.')
my_text = ''.join(splitted_list)
print(my_text)
print(len(my_text))
partial_list = splitted_list[3:7:2]
print (partial_list)
print (list)


#exemple de mise en ordre des index



#recuperer dans splitted_list les mots de l'index 35 a 49 inclus
partial_list = splitted_list[35:49+1]
print(partial_list)

#afficher le numéro du dernier index
last_index = len(splitted_list) - 1
print(last_index)


#recuperer 1 mot sur 2 sur tout le lorem

step_list = splitted_list[0:last_index:2]
print(step_list)

#
list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
ind = len(list)
split_up_list = list[0:ind:3]
print(split_up_list)
split_up_list = list[1:ind:3]
print(split_up_list)
split_up_list = list[2:ind:3]
print(split_up_list)


#recuperer la position de la chaine de caractères
my_text = " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vel consequat nibh. Nunc at enim mollis, pretium arcu sed, condimentum libero. Integer euismod sollicitudin pellentesque. Aenean elementum non sem eu blandit. In mattis a est eget pretium. Phasellus mollis ullamcorper mi interdum ornare. Maecenas et nunc nec urna congue consectetur.Vivamus bibendum leo vitae rhoncus fermentum. Nullam varius est ac dui posuere, et molestie mauris sollicitudin. Phasellus ac lacus at orci rhoncus viverra. Phasellus imperdiet molestie libero sit amet rhoncus. Cras sit amet erat molestie, fringilla justo sed, imperdiet orci. Praesent sit amet libero vitae enim scelerisque venenatis sed eget nulla. Nam tempor bibendum sagittis. Aenean semper lorem non lectus venenatis, varius viverra justo consequat. Maecenas turpis tortor, bibendum id aliquet in, pretium ac lorem. Quisque varius, lacus non viverra scelerisque, nisi massa consequat libero, ac efficitur est purus ut nunc. Integer tempor ipsum sapien. Phasellus nec felis in orci blandit placerat eget a ligula. Proin porta neque ac ipsum ultricies, at porttitor quam malesuada. Morbi faucibus varius enim, eget tincidunt libero posuere ac. "
finder = my_text.find('minim')
print(finder)