import pywavefront
import numpy as np

# Load the SMPL-X OBJ file
obj_file = 'results\econ\obj\Dane_0_smpl_00.obj'
scene = pywavefront.Wavefront(obj_file)

# Extract the vertices and faces from the OBJ file
vertices = np.array(scene.vertices)
faces = np.array(scene.mesh_list[0].faces)

# Scale the vertices to centimeters
vertices *= 100

# Compute the height of the model
height = np.max(vertices[:, 1]) - np.min(vertices[:, 1])
print(f'Height: {height:.2f} cm')

# Compute the waist circumference of the model
waist_vertices = vertices[(vertices[:, 0] > -2) & (vertices[:, 0] < 2) & (vertices[:, 1] < np.median(vertices[:, 1]))]
waist_circumference = 2 * np.pi * np.mean(np.linalg.norm(waist_vertices[:, [0, 2]], axis=1))
print(f'Waist circumference: {waist_circumference:.2f} cm')

# Compute the chest circumference of the model
chest_vertices = vertices[(vertices[:, 0] > -5) & (vertices[:, 0] < 5) & (vertices[:, 1] > np.median(vertices[:, 1]))]
chest_circumference = 2 * np.pi * np.mean(np.linalg.norm(chest_vertices[:, [0, 2]], axis=1))
print(f'Chest circumference: {chest_circumference:.2f} cm')


# Compute the neck length
neck_vertices = vertices[(vertices[:, 0] > -1) & (vertices[:, 0] < 1) & (vertices[:, 1] > np.median(vertices[:, 1]))]
neck_length = np.linalg.norm(neck_vertices[0] - neck_vertices[-1])
print(f'Neck length: {neck_length:.2f} cm')