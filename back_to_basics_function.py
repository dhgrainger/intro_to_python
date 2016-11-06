def addition(num1,num2):
    answer = num1+num2
    return answer

x = addition(5,6)

print(x)

def website(font,background_color,font_size,font_color):
    print('font:',font)
    print('bg:', background_color)
    print('Font size:', font_size)
    print('Font color:',font_color)

#website('TNR','White','11','black')

website(background_color='White',
        font_size='11',
        font_color='black',
        font='TNR')

#use function parameter defaults
def default_website(font='TNR',background_color='White',font_size='11',font_color='black'):
    print('font:',font)
    print('bg:', background_color)
    print('Font size:', font_size)
    print('Font color:',font_color)

default_website(font='Wingdings')
