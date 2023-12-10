import matplotlib.pyplot as plt

def plot_figure(figure):
    data = figure['data']

    # Criar uma nova figura
    plt.figure(figsize=(10, 6))

    # Mapeamento de estilos de marcadores
    marker_mapping = {
        'triangle-up': '^',
        'circle': 'o',
        'triangle-down': 'v',
        'x': 'x'
    }

    # Plotar os dados sem valores zero
    for trace in data:
        if trace['type'] == 'scatter':
            x_values = [x for x in trace['x'] if x != 0]
            y_values = [y for y in trace['y'] if y != 0]

            if trace['name'] == '1x speed':
                plt.plot(x_values, y_values, label=trace['name'], color='blue', linestyle='dashdot')
            else:
                marker_style = marker_mapping.get(trace['marker']['symbol'], 'o')
                color = 'blue' if trace['legendgroup'] == 'Forward' else 'green' if trace['legendgroup'] == 'Mixed' else 'red'
                plt.scatter(x_values, y_values, label=trace['name'], color=color, marker=marker_style)

    # Configurar o layout
    layout = figure['layout']
    plt.title(layout['title']['text'])
    plt.xlabel(layout['xaxis']['title']['text'])
    plt.ylabel(layout['yaxis']['title']['text'])
    plt.legend(loc='upper right')

    # Mostrar o gráfico
    plt.grid(True)
    plt.show()
