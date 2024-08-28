import pygame
class GravityEngine:
	def __init__(self, force):
		self.force = force

	def calculate_gravitational_force(self, mass1, mass2, distance):
		return (self.force * mass1 * mass2) / (distance ** 2)


class Ball:
	def __init__(self, mass):
		self.mass = mass

	def apply_gravitational_force(self, force, distance):
		gravity_force = force.calculate_gravitational_force(self.mass, force.mass, distance)
		return gravity_force
