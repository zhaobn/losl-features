# %%
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# %%
def draw_figure(
	body_shape="circle",  # "circle" or "square"
	body_color="orange",
	body_fill="orange",
	line_thickness=3,
	line_lengths=(1, 1, 1),
	synapse_colors = ("red", "purple", "orange"),
	synapse_fills = ("red", "purple", "orange"),
	line_styles = ("isExtended", "hasFeathers", "thick")
):
	# Create figure and axis
	fig, ax = plt.subplots(figsize=(5, 5))
	ax.set_aspect('equal')
	ax.axis('off')
	ax.set_facecolor('white')

	# Define fixed plot limits for consistency
	plot_limit = 3
	ax.set_xlim(-plot_limit, plot_limit)
	ax.set_ylim(-plot_limit, plot_limit)

  # Position synapses
	synapse_positions = [
		(0, 1+line_lengths[0]),  # Top synapse (diamond)
		(-1-line_lengths[1]*0.7, -1-line_lengths[1]*0.7),  # Bottom-left synapse (triangle)
		(1+line_lengths[2]*0.7, -1-line_lengths[2]*0.7),  # Bottom-right synapse (half-circle)
	]

	# Draw lines connecting to synapses
	for idx, (x, y) in enumerate(synapse_positions):
		# Draw main line
		if line_styles[idx] == "thick":
			offsets = [-0.3, 0, 0.3]  # Three parallel lines
			for offset in offsets:
				ax.plot([0, x + offset], [0, y], color=synapse_colors[idx], lw=3, zorder=1)

		if line_styles[idx] == "hasFeathers":
			line_length = np.sqrt(x**2 + y**2)
			num_feathers = 10
			for i in range(1, num_feathers):
				t = i / num_feathers
				fx = t * x
				fy = t * y
				dx, dy = -y / line_length, x / line_length
				ax.plot(
          [fx - 0.2 * dy, fx + 0.2 * dy],
          [fy - 0.2 * dx, fy + 0.2 * dx],
          color=synapse_colors[idx],
          lw=3,
          zorder=1,
        )

		ax.plot([0, x], [0, y], color=synapse_colors[idx], lw=line_thickness)

	# Draw the main body (circle or square) **after** the lines
	if body_shape == "circle":
		body = patches.Circle((0, 0), 1, facecolor=body_fill, edgecolor=body_color, linewidth=line_thickness, zorder=3)
	elif body_shape == "square":
		body = patches.Rectangle((-1, -1), 2, 2, facecolor=body_fill, edgecolor=body_color, linewidth=line_thickness, zorder=3)
	ax.add_patch(body)

	# Draw synapses
	for (x, y), color, fill, shape in zip(
		synapse_positions,
		synapse_colors,
		synapse_fills,
		["diamond", "triangle", "semicircle"]
	):
		if shape == "diamond":
			diamond = patches.Polygon(
				[(x, y + 0.3), (x + 0.3, y), (x, y - 0.3), (x - 0.3, y)],
				closed=True,
				facecolor=fill,
				edgecolor=color,
				linewidth=line_thickness,
				zorder=2
			)
			ax.add_patch(diamond)
		elif shape == "triangle":
			triangle = patches.Polygon(
				[(x+0.2, y+0.2), (x-0.2, y+0.2), (x+0.2, y-0.2)],
				closed=True,
				facecolor=fill,
				edgecolor=color,
				linewidth=line_thickness,
				zorder=2
			)
			ax.add_patch(triangle)
		elif shape == "semicircle":
			semicircle = patches.Wedge(
				(x, y-0.1),
				r=0.3,
				theta1=0,
				theta2=180,
				facecolor=fill,
				edgecolor=color,
				linewidth=line_thickness,
				zorder=2
			)
			ax.add_patch(semicircle)

	return plt

# Example usage
test = draw_figure(
	body_shape="circle",
  body_color="orange",
	body_fill="white",
  line_lengths=(1, 1, 1),
  line_styles=("plain", "hasFeathers", "thick"),
  synapse_colors=("red", "blue", "green"),
	synapse_fills=("white", "white", "white"),
)
test.show()

# %%
def draw_boolean_features(feat_arr=[1, 1, 1, 1, 1, 1, 1, 1]):
	body_shape = "circle" if feat_arr[0] == 1 else "square"
	body_color = "orange" if feat_arr[1] == 1 else "black"
	top_line = 1 if feat_arr[2] == 1 else 0.3
	left_line = "hasFeathers" if feat_arr[3] == 1 else "plain"
	right_line = "thick" if feat_arr[4] == 1 else "plain"
	top_fill = "red" if feat_arr[5] == 1 else "white"
	left_fill = "blue" if feat_arr[6] == 1 else "white"
	right_fill = "green" if feat_arr[7] == 1 else "white"

	figure = draw_figure(
		body_shape,
  	body_color, body_fill=body_color,
  	line_lengths=(top_line, 1, 1),
  	line_styles=("plain", left_line, right_line),
  	synapse_colors=("red", "blue", "green"),
		synapse_fills=(top_fill, left_fill, right_fill),
  )

	figure_name = ''.join([str(i) for i in feat_arr])
	figure.savefig(figure_name, dpi=300, bbox_inches="tight", pad_inches=0.1)
	figure.show()

# %% maximalist
draw_boolean_features([1, 1, 0, 1, 1, 1, 1, 1])
draw_boolean_features([0, 0, 1, 0, 1, 1, 1, 1])
draw_boolean_features([0, 1, 1, 1, 1, 0, 0, 1])
draw_boolean_features([1, 0, 1, 1, 1, 1, 0, 0])

# minimalist
draw_boolean_features([1, 1, 1, 0, 0, 0, 1, 0])
draw_boolean_features([0, 0, 0, 1, 0, 0, 1, 0])
draw_boolean_features([0, 1, 0, 0, 1, 1, 0, 0])
draw_boolean_features([1, 0, 0, 0, 1, 0, 0, 1])

# %%
