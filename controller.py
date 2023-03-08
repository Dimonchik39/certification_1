import functions as func

def launch_program():
    '''
    Функция действий при выборе раздела меню пользователем
    '''
    program_mode = func.menu_select()

    while program_mode != 5:   
        if program_mode == 1:
            result = func.write_row()
        if program_mode == 2:
            result = func.read_row()
        if program_mode == 3:
            result = func.info()
        if program_mode == 4:
            result = func.delete_row()
        result
        launch_program()
        return
    
    
