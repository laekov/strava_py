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
    activities = activities.groupby(['date'])['Distance'].sum()
    activities.index = pd.to_datetime(activities.index)
    activities.clip(0, max_dist, inplace=True)
    
    if year_min is not None:
        activities = activities[activities.index.year>=year_min]
    
    if year_max is not None:
        activities = activities[activities.index.year<=year_max]
    
    # Create heatmap
    fig, ax = calmap.calendarplot(
        data = activities
        )
    
    # Save plot
    fig.set_figheight(fig_height)
    fig.set_figwidth(fig_width)
    fig.savefig(output_file, dpi = 600)
