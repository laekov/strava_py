import calmap
import matplotlib.pyplot as plt
import pandas as pd

def plot_calendar(activities, year_min=None, year_max=None, max_dist=None,
                  fig_height = 15, fig_width = 9, output_file='calendar.png'):
    # Create a new figure
    plt.figure()
    
    # Process data
    activities['Activity Date'] = pd.to_datetime(activities['Activity Date'])
    activities['date'] = activities['Activity Date'].dt.date
    activities['dis'] = activities['Distance'].apply(lambda x: float(x.replace(',', '.')))
    activities = activities.groupby(['date'])['dis'].sum()
    activities.index = pd.to_datetime(activities.index)
    activities.clip(0, max_dist, inplace=True)
    
    if year_min:
        activities = activities[activities.index.year>=year_min]
    
    if year_max:
        activities = activities[activities.index.year<=year_max]
    
    # Create heatmap
    fig, ax = calmap.calendarplot(
        data = activities
        )
    
    # Save plot
    fig.set_figheight(fig_height)
    fig.set_figwidth(fig_width)
    fig.savefig(output_file, dpi = 600)
