# %%
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# %%
def draw_figure(
	body_shape="circle",  # "circle" or "square"
	body_fill="darkgreen",  # "white" or "darkgreen"
	line_lengths=(1, 1, 1),
	synapse_fills=("darkgreen", "white", "darkgreen"),
	line_thickness=4,
	line_color="darkgreen",
	body_edge_color="darkgreen",
	synapse_edge_color="darkgreen"
):
	# Create figure and axis
	fig, ax = plt.subplots(figsize=(6, 6))
	ax.set_aspect('equal')
	ax.axis('off')

  # Position synapses
	synapse_positions = [
		(0, 1+line_lengths[0]),  # Top synapse (diamond)
		(-1-line_lengths[1]*0.7, -1-line_lengths[1]*0.7),  # Bottom-left synapse (triangle)
		(1+line_lengths[2]*0.7, -1-line_lengths[2]*0.7),  # Bottom-right synapse (half-circle)
	]

	# Draw lines connecting to synapses
	for (x, y) in synapse_positions:
		ax.plot([0, x], [0, y], color=line_color, lw=line_thickness)

	# Draw the main body (circle or square) **after** the lines
	if body_shape == "circle":
		body = patches.Circle((0, 0), 1, facecolor=body_fill, edgecolor=body_edge_color, linewidth=line_thickness, zorder=3)
	elif body_shape == "square":
		body = patches.Rectangle((-1, -1), 2, 2, facecolor=body_fill, edgecolor=body_edge_color, linewidth=line_thickness, zorder=3)
	ax.add_patch(body)

	# Draw synapses
	for (x, y), fill, shape in zip(
		synapse_positions,
		synapse_fills,
		["diamond", "triangle", "semicircle"]
	):
		facecolor = fill
		if shape == "diamond":
			diamond = patches.Polygon(
				[(x, y + 0.3), (x + 0.3, y), (x, y - 0.3), (x - 0.3, y)],
				closed=True,
				facecolor=facecolor,
				edgecolor=synapse_edge_color,
				linewidth=line_thickness,
				zorder=2
			)
			ax.add_patch(diamond)
		elif shape == "triangle":
			triangle = patches.Polygon(
				[(x+0.2, y+0.2), (x-0.2, y+0.2), (x+0.2, y-0.2)],
				closed=True,
				facecolor=facecolor,
				edgecolor=synapse_edge_color,
				linewidth=line_thickness,
				zorder=2
			)
			ax.add_patch(triangle)
		elif shape == "semicircle":
			semicircle = patches.Wedge(
				(x, y-0.1), # Center
				r=0.3, # Radius
				theta1=0,  # Starting angle (0 degrees)
				theta2=180,  # Ending angle (180 degrees)
				facecolor=facecolor,
				edgecolor=synapse_edge_color,
				linewidth=line_thickness,
				zorder=2
			)
			ax.add_patch(semicircle)

	return plt

# # Example usage
# test = draw_figure(
# 	body_shape="square",
# 	body_fill="white",
# 	line_lengths=(0.4, 0.4, 0.4),
# 	synapse_fills=("white", "darkgreen", "white")
# )
# test.show()

# %%
def draw_boolean_features(feat_arr=[1, 1, 1, 1, 1, 1, 1, 1]):
	body_shape = "circle" if feat_arr[0] == 1 else "square"
	body_fill = "darkgreen" if feat_arr[1] == 1 else "white"
	top_line = 1 if feat_arr[2] == 1 else 0.4
	left_line = 1 if feat_arr[3] == 1 else 0 if body_shape == "circle" else 0.4
	right_line = 1 if feat_arr[4] == 1 else 0 if body_shape == "circle" else 0.4
	top_fill = "darkgreen" if feat_arr[5] == 1 else "white"
	left_fill = "darkgreen" if feat_arr[6] == 1 else "white"
	right_fill = "darkgreen" if feat_arr[7] == 1 else "white"

	figure = draw_figure(
    body_shape=body_shape,
    body_fill=body_fill,
    line_lengths=(top_line, left_line, right_line),
    synapse_fills=(top_fill, left_fill, right_fill)
  )

	figure_name = ''.join([str(i) for i in feat_arr])
	figure.savefig(figure_name, dpi=300, bbox_inches="tight")
	figure.show()

# %% maximalist
draw_boolean_features([1, 1, 0, 1, 1, 1, 1, 1])
draw_boolean_features([0, 0, 1, 0, 1, 1, 1, 1])
draw_boolean_features([0, 1, 1, 1, 1, 0, 0, 1])
draw_boolean_features([1, 0, 1, 1, 1, 1, 0, 0])

# %% minimalist
draw_boolean_features([1, 1, 1, 0, 0, 0, 1, 0])
draw_boolean_features([0, 0, 0, 1, 0, 0, 1, 0])
draw_boolean_features([0, 1, 0, 0, 1, 1, 0, 0])
draw_boolean_features([1, 0, 0, 0, 1, 0, 0, 1])
