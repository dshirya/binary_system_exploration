'''

Here you can adjust appearance of the plot and periodic table

'''

# Marker types for different structures
marker_types = ['o', 's', '^', 'D', 'P', '*', '2', '8', 'X', 'h']
marker_size = 200  # Default size for scatter markers

# Colors for different structures
colors = [
    "#c3121e",  # Sangre (195, 18, 30)
    "#0348a1",  # Neptune (3, 72, 161)
    "#ffb01c",  # Pumpkin (255, 176, 28)
    "#027608",  # Clover (2, 118, 8)
    "#1dace6",  # Cerulean (29, 172, 214)
    "#9c5300",  # Cocoa (156, 83, 0)
    "#9966cc",  # Amethyst (153, 102, 204)
    "#ff4500"   # Orange Red (255, 69, 0)
]

shape_linewidth = 2  # Line width for shapes (circles/rectangles)

# Plot
circle_radius = 0.30  # Radius for circles in periodic table (default 0.3)
circle_size = 0.26  # Default size for color circles (default 0.26)
shrink_factor_circle = 0.054  # How much each circle shrinks with additional layers (better not to change) (default 0.054)
text_fontsize_circle = 18  # Font size for text in circles (default 18)

# Table 
rectangle_size = 1.0  # Size of rectangles in periodic table (default 1)
initial_rect_size = 0.92  # Initial size for rectangles (default 0.92)
shrink_factor_rect = 0.15  # How much each rectangle shrinks with additional layers (default 0.15)
initial_rect_offset = 0.46  # Initial offset for rectangles (default 0.46)
text_fontsize_rectangle = 24  # Font size for text in rectangles (default 24)
text_weight_rectangle = 'bold'  # Font weight for text in rectangles (default 'bold')

# Figure size and scaling
scale_factor = 1.5  # Adjusts the overall figure size (default 1.5)
x_margin = 1.5  # X-axis margin for plots (default 1.5)
y_margin = 1.5  # Y-axis margin for plots (default 1.5)

# Legend properties
legend_props = {
    "fontsize": 24,
    "loc": 'upper center',
    "frameon": False,
    "framealpha": 1,
    "edgecolor": 'black',
    "markerscale": 1,
    "ncol": 3
}

# Axis properties
axis_visibility = False  # Whether to show axis lines and ticks
aspect_ratio = 'equal'  # Aspect ratio for plots

# Plot saving properties
plot_folder = "plots"
file_extension = ".png"
dpi = 600
bbox_inches = 'tight'