def data_type():
    incoming_type = input()
    incoming_info = input()

    if incoming_type =='int':
        return int(incoming_info)*2
    elif incoming_type == 'real':
        return f'{1.5*float(incoming_info):.2f}'
    else:
        return '$'+incoming_info+'$'



print(data_type())