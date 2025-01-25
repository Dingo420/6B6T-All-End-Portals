#SmknBwls420
#May All Thy Nuggs Be DANK!
#My Locations are the center of the portal.
#There are other player made portals, or there was... I noticed one turn into boundry blocks? or "impassible / unbreakable / air"
#Most of ring 1-3 Locations were taken from a Reddit Post and not confirmed, But appear to be legit.
#Some portals are outside of rings slightly or doubled up as seen in ring 4
#(at 90 degrees, like a phasor 0 on the right 180 on the left 90 on top 270 at the bottom)

import math
import plotly.graph_objects as go

# Unconfirmed Stronghold Locations
unconfirmed_locations = [
  
]

# Confirmed Stronghold Locations
confirmed_locations = [
  # Ring 1 (3 Found, 0 Missing)
  (-560, 1504),    # 
  (1008, -1440),   # 
  (1888, -32),     # 
  
  # Ring 2 (6 Found, 0 Missing)
  (-3200, 4480),   # 
  (2064, -4400),   # 
  (4992, -512),    # 
  (2960, 4208),    # 
  (-2496, 5296),   # 
  (-5568, 608),    # Missing Portal in Stronghold
  
  # Ring 3 (10 Found, 0 Missing)
  (7213, 2211),    # 
  (-7728, -2208),  # 
  (-4656, -6144),  # 
  (-80, -8544),    # 
  (4544, -6544),   # 
  (-7191, 2696),   # 
  (4960, 6592),    # 
  (96, 7808),      # 
  (-4592, 6832),   # 
  (7879, -2569),   # 
  
  # Ring 4 (14 Found, 1 Missing)
  (-6788, -8869),  # 
  (-2590, -10795), # 
  (2093, -10394),  # 
  (6834, -9584),   # 
  (10792, 3285),   # 
  (8903, 7776),    # 
  (4955, 10662),   # 
  (350, 10700),    # 
  (-4243, 10145),  # 
  (-8479, 7968),   # 
  (9445, -5591),   # 
  (-9673, -5251),  # 
  (-10663, -736),  # 
  (-10785, 3926),  # 
  #(11223, -964),  # Missing?
  
  # Ring 5 (21 Found, 0 Missing)
  (8378, -10695),   # 
  (-6907, -11810),  # 
  (782, -13817),    # 
  (11591, 7662),    # 
  (1012, -13910),   # 
  (11418, -8017),   # 
  (13976, -329),    # 
  (-10433, -9334),  # 
  (5272, 12991),    # 
  (13622, 3739),    # 
  (1247, 14087),    # 
  (-14077, 2305),   # 
  (-10456, 9854),   # 
  (-6942, 12585),   # 
  (-13133, -6009),  # 
  (-3446, -14069),  # 
  (9074, 11355),    # 
  (-14439, -2039),  # 
  (13983, -4448),   # 
  (-2952, 14592),   # 
  (-13371, 6662),   # 
  
  # Ring 6 (28 Found, 0 Missing)
  (-16577, -2327),  # 
  (9405, -13886),   # 
  (-16095, 5097),   # 
  (2376, -16723),   # 
  (-1401, -16926),  # 
  (15902, 6098),    # 
  (14866, -8507),   # 
  (-14344, -9600),  # 
  (12572, -11889),  # 
  (-17298, 1421),   # 
  (8752, 15020),    # 
  (-16221, -6324),  # 
  (17366, -1338),   # 
  (1298, 17417),    # 
  (-15141, 8711),   # 
  (-9538, 14669),   # 
  (5271, 16761),    # 
  (12064, 12774),   # 
  (-5192, -16791),  # 
  (-12055, -12796), # 
  (-2485, 17433),   # 
  (17445, 2554),    # 
  (-13047, 12040),  # 
  (-9037, -15330),  # 
  (-6468, 16642),   # 
  (14772, 10042),   # 
  (6520, -16644),   # 
  (16959, -5684),   # 

  # Ring 7 (36 Total,34 Found, 2 Missing but accounted for?)
  (986, -19723),   # 
  (-19360, -4139), # 
  (-18327, -7543), # 
  (18914, -5948),  # 
  (4206, -19380),  # 
  (-9277, -17550), # 
  (-14725, -13353),# 
  (-16874, -10636),# 
  (18033, -8527),  # 
  (15799, -12181), # 
  (-19792, 2615),  # 
  (10753, -16847), # 
  (-2617, -19815), # 
  (13447, -14849), # 
  (14365, 13984),  # 
  (-17793, 9506),  # 
  (12377, 16033),  # 
  (-15969, 12469), # 
  (-10846, 17117), # 
  (16744, 11494),  # 
  (-13608, 15106), # 
  (19887, 4516),   # 
  (-5617, -19608), # 
  (2728, 20307),   # 
  (7964, -18907),  # 
  (-7815, 19027),  # 
  (-4343, 20111),  # 
  (19118, 7962),   # 
  (-20755, -749),  # 
  (-914, 20803),   # 
  (6413, 19938),   # 
  (9755, 18559),   # 
  (-12818, -16599),# 
  (21218, 1002),   # 
  # Here are GPT' (or maths guess)
  #(20333, -2449) # There appears to be chunk Glitches here as well. Edit or chunk trail?
  #(-19497, 6267) # There appears to be chunk Glitches here as well. Edit or chunk trail?
  

  # Ring 8 (0 Found, 9 Missing)
  (21854, 8059),  #
  (13084, 19236), #
  (-887,23789),   #
  (-16301,17091), #
  (-22428, 6380), #
  (-21551,-7836), #
  (-7162,-22444), #
  (16494,-17100), #
  (22740,-4364),  #
]

# Missing / greifed Stronghold Locations Marked in red
missing_locations = [

  # Ring 4
   (11223, -964), # Looked quite a bit cant find is this the one? YES this one
   
  # Ring 7
  (20333, -2449), # There appears to be chunk Glitches here as well. Edit or chunk trail? signs?m no "south one???"warw
  (-19497, 6267), # There appears to be chunk Glitches here as well. Edit or chunk trail? Not the "First One with Signs"
     
]

rings = [
    (1280, 2816, "Ring 1", 3), (4352, 5888, "Ring 2", 6), (7424, 8960, "Ring 3", 10),
    (10496, 12032, "Ring 4", 15), (13568, 15104, "Ring 5", 21), (16640, 18176, "Ring 6", 28),
    (19712, 21248, "Ring 7", 36), (22784, 24320, "Ring 8", 9)
]

# Helper function to sort points
def sort_points(points):
    return sorted(points, key=lambda p: (
        math.sqrt(p[0]**2 + p[1]**2), math.atan2(-p[1], p[0]) % (2 * math.pi)
    ))

sorted_unconfirmed = sort_points(unconfirmed_locations)
sorted_confirmed = sort_points(confirmed_locations)
sorted_missing = sort_points(missing_locations)

# Helper function to add points to the plot
def add_points_to_plot(fig, points, start_idx, color, symbol):
    for idx, (x, z) in enumerate(points, start=start_idx):
        fig.add_trace(go.Scatter(
            x=[x], y=[-z],
            mode='markers+text',
            marker=dict(color=color, size=8, symbol=symbol),
            name=f"{idx}: ({x}, {z})",
            text=str(idx),
            textposition="top center"
        ))

# Create Plot
fig = go.Figure()
add_points_to_plot(fig, sorted_unconfirmed, 1, 'orange', 'x')
add_points_to_plot(fig, sorted_confirmed, len(sorted_unconfirmed) + 1, 'green', 'circle')
add_points_to_plot(fig, sorted_missing, len(sorted_unconfirmed) + len(sorted_confirmed) + 1, 'red', 'triangle-down')

# Add ring sections and boundaries
def add_rings_to_plot(fig, rings):
    for inner, outer, label, num_sections in rings:
        angle_step = 360 / num_sections
        for i in range(num_sections):
            angle = i * angle_step
            inner_x, inner_z = inner * math.cos(math.radians(angle)), inner * math.sin(math.radians(angle))
            outer_x, outer_z = outer * math.cos(math.radians(angle)), outer * math.sin(math.radians(angle))
            fig.add_trace(go.Scatter(
                x=[inner_x, outer_x], y=[-inner_z, -outer_z],
                mode='lines',
                line=dict(color='purple', width=2),
                showlegend=False
            ))
        fig.add_shape(
            type="circle", x0=-inner, y0=-inner, x1=inner, y1=inner,
            line=dict(color="blue", dash="dot")
        )
        fig.add_shape(
            type="circle", x0=-outer, y0=-outer, x1=outer, y1=outer,
            line=dict(color="blue", dash="solid")
        )

add_rings_to_plot(fig, rings)

# Layout configuration
fig.update_layout(
    title="Interactive Cartesian Graph with Strongholds and Rings",
    xaxis_title="X Coordinate (Horizontal: West/East)",
    yaxis_title="Z Coordinate (Vertical: South/North)",
    xaxis=dict(zeroline=True, showline=True, mirror=True, range=[-25000, 25000]),
    yaxis=dict(zeroline=True, showline=True, mirror=True, range=[-25000, 25000],
               tickvals=[-20000, -10000, 0, 10000, 20000],
               ticktext=["-20000", "-10000", "0", "10000", "20000"]),
    showlegend=True,
    width=1700,
    height=1200
)

# Show the interactive chart
fig.show()
