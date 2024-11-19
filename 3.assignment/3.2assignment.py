import math

# -- Exercise 1 ---
class Cube():
    """ A cube with the side length of a. """
    def __init__(self, a):
        self.length = a

    def volume(self):
        """ Returns the volume of the cube. """
        return self.length**3
    
    def surface_area(self):
        """ Returns the surface area of the cube. """
        return 6 * self.length**2

    def space_diagonal(self):
        """ Returns the space diagonal of the cube. """
        return math.sqrt(3) * self.length
    
    def rescale(self, scale:float):
        """ Rescales the cube by the factor of the scale. """
        self.length *= scale

# --- Exersice 2 ---
class Vector3D():
    """ A 3 dimentional vector. """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """ Returns a string containing information about the vector. """
        return (f"Points x:{self.x}, y:{self.y}, z:{self.z} " +
                f"Length: {self.length()}")

    def length(self):
        """ Returns the length of the vector. """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def distance(self, other):
        """ Returns the distance to another vector (other)."""
        return math.sqrt((other.x - self.x) ** 2 +
                         (other.y - self.y) ** 2 +
                         (other.z - self.z) ** 2)

if __name__ == "__main__":
    # Testing implementation of exercise 1
    print("--- Exercise 1 ---")

    # Define a cube with size 10 and test the class functions
    cube = Cube(10)
    print(f"Cube side length: {cube.length}")
    print(f"Cube volume: {cube.volume()}")
    print(f"Cube surface area: {cube.surface_area()}")
    print(f"Cube space diagonal: {cube.space_diagonal()}")

    # Rescale the cube and test the class functions again
    scale = 0.5
    cube.rescale(scale)
    print(f"\nCube side length when scaled by {scale}: {cube.length}")
    print(f"Cube volume: {cube.volume()}")
    print(f"Cube surface area: {cube.surface_area()}")
    print(f"Cube space diagonal: {cube.space_diagonal()}")

    # Testing implementation of exercise 2
    print("\n--- Exercise 2 ---")
    vector1 = Vector3D(3, 5, 2)
    vector2 = Vector3D(4, 4, 6)

    # Print their length and distance between the vectors
    print(f"First  vector length: {vector1.length()}")
    print(f"Second vector length: {vector2.length()}")
    print(f"Distance between vectors: {vector1.distance(vector2)}\n")

    # Test the __str__ method
    print(f"Info about first  vector:\n{vector1}\n")
    print(f"Info about second vector:\n{vector2}")