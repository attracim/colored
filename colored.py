import pandas as pd


# Закраска фона ячеек 
def configure_colors(pdf):
    columns = pdf.columns[8:9]

    ret = pd.DataFrame('', index=pdf.index, columns=pdf.columns)

    for index, row in pdf.iterrows():

        need_down = False
        need_up = False
        colored = False
        colored_columns = []

        for column in columns:
            item = row[column]
            if item == 'Down' and not colored:
                need_up = False
                if need_down:
                    colored_columns.append(column)
                    # Закрашиваем красным, если есть два Down подрят
                    ret.loc[index, colored_columns] = 'background-color: red'
                    colored = True
                elif not need_down:
                    colored_columns.clear()
                    colored_columns.append(column)
                    need_down = True

            elif item == 'Up' and not colored:
                need_down = False
                if need_up:
                    # Закрашиваем зеленым, если есть два Up подрят
                    colored_columns.append(column)
                    ret.loc[index, colored_columns] = 'background-color: green'
                    colored = True
                elif not need_up:
                    colored_columns.clear()
                    colored_columns.append(column)
                    need_up = True
            elif item != 'Up' and item != 'Down':
                need_down = False
                need_up = False
                colored_columns.clear()

    return ret


def run(df):
    # Передача строк в функцию для закраски
    pdf = df.style.apply(configure_colors, axis=None)
    return pdf
