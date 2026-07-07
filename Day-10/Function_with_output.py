# def format_name(f_name, l_name):
#     # print(f_name.title())
#     # print(l_name.title())
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#
#     return (f" {formatted_f_name} {formatted_l_name} ")
#
# formated_string = format_name("SaUrAbH", "KuMaR")
#
# print(formated_string)


def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("Hello"))
print(output)