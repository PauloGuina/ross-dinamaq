import matplotlib.pyplot as plt

def plot_figure(figure):
    data = figure['data']

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Mapping of marker styles
    marker_mapping = {
        'triangle-up': '^',
        'circle': 'o',
        'triangle-down': 'v',
        'x': 'x',
    }

    # Plot the data without zero values
    for trace in data:
        if trace['type'] == 'scatter':
            x_values = [x for x in trace['x'] if x != 0]
            y_values = [y for y in trace['y'] if y != 0]

            if trace['name'] == '1x speed':
                # Plot 1x speed data only once
                plt.plot(x_values, y_values, label=trace['name'], color='red', linestyle='dashdot')
            elif trace['name'] == '0.5x speed':
                # Plot 0.5x speed data with red dashdot style
                plt.plot(x_values, y_values, label=trace['name'], color='orange', linestyle='dashdot')
            else:
                marker_style = marker_mapping.get(trace['marker']['symbol'], 'o')
                color = 'blue' if trace['legendgroup'] == 'Forward' else 'red' if trace['legendgroup'] == 'Mixed' else 'red' if trace['legendgroup'] == 'Crit. Speed' else 'green'
                plt.scatter(x_values, y_values, label=trace['name'], color=color, marker=marker_style)

    # Configure the layout
    layout = figure['layout']
    plt.title(layout['title']['text'])
    plt.xlabel(layout['xaxis']['title']['text'])
    plt.ylabel(layout['yaxis']['title']['text'])
    plt.legend(loc='upper right')

    # Show the graph
    plt.grid(True)
    plt.show()