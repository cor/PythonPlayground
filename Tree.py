import sys

tree_width = 25

if len(sys.argv) is 2:
	tree_width = int(sys.argv[1])
	if tree_width % 2 == 0:
		tree_width = 25

def print_tree(size):
	# Get the string for every line of the tree	
	def get_component(component_number):
		# Return None on every even number
		if component_number % 2 == 0:
			return None
		else:
			# Line is odd, print line
			side_width = (size - component_number) / 2
			return "-" * side_width + "#" * component_number + "-" * side_width

	# Loop through the lines and print the line
	for i in range(tree_width + 1):
		if get_component(i) is not None:
			print get_component(i)
	# Print the base
	print get_component(1);

print_tree(tree_width)
