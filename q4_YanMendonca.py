lista_columns = lambda t1, t2: [e for e in t1[1] if e in t2[1]]

join_columns = lambda columns=None: "\n, ".join(columns) if columns else "*"

add_column_alias = lambda table_tuples: [f"{table[2]}.{column}" for table in table_tuples for column in table[1]] if table_tuples else None

inner_join_text = lambda t1, t2: f" INNER JOIN {t2[0]} {t2[2]} ON " + ''.join([" AND " + f"{t1[2]}.{attr} = {t2[2]}.{attr}" if index > 0 else f"{t1[2]}.{attr} = {t2[2]}.{attr}" for index, attr in enumerate(lista_columns(t1, t2))])

select_text = lambda table, columns=None, condition=None: f"SELECT {join_columns(add_column_alias(columns))} \nFROM {table[0]} {table[2].lower()} WHERE {condition}" if condition else f"SELECT {join_columns(add_column_alias(columns))} \nFROM {table[0]} {table[2].lower()}"

imprimir = lambda f1, f2, f3: print(f"{f1}\n{f2}\n{f3}")

VIDEOGAMES = lambda:  ("VIDEOGAMES", ["id_game", "name", "genre", "release_date", "id_console"], "videogames")
GAMES = lambda:  ("GAMES", ["id_game", "id_console", "title", "genre", "release_date", "id_company"], "games")
COMPANY = lambda:  ("COMPANY", ["id_company", "name", "country"], "company")

print_queries = lambda: imprimir(inner_join_text(GAMES(), VIDEOGAMES()), inner_join_text(GAMES(), COMPANY()), select_text(GAMES(), (GAMES(), VIDEOGAMES(), COMPANY()), "videogames.id_game = 1"))

# Execute the function to print queries
print_queries()
