from datetime import datetime
from binary import Statement

#dump_dict = {}
state_dict = {'hui':'huihui'}
state = Statement('saved_states.bin')


def check_file_exist(func):
    def inner_func():
        if state._checkfile():
            return func
        else:
            state.newdump()
            dic={}
            state.rewrite(dic)
            return func

    return inner_func()


@check_file_exist
def save_state(state_dic):
    date = datetime.now()
    date = date.strftime('%d-%m-%Y_%H%M%S')
    dict = state.read()
    dict[date]=state_dic
    state.rewrite(dict)
def load_state():
    return state.read()


