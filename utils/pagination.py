import math


def make_pagination_range(
        page_range, # sabe quantas receitas vai existir
        qyt_pages, # quantidade de paginas a serem mostradas
        current_page): # pagina que o usuario esta
    middle_range = math.ceil(qyt_pages / 2) # quantas paginas vao ficar antes e depois da que o usuario esta
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    return page_range[start_range:stop_range]
