import xml.etree.ElementTree as et
import xml.etree.ElementTree as et
import collections

output_buffer = []
output = None

def xmlconverstion(input_file, output_file, delimiter=",",  noheader=False,
			limit=-1, buffer_size=10000, quotes=True):
	# open the xml file for iteration
	tree = et.parse(input_file)
	root = tree.getroot()

	elements = []

	for child in root:
	    elements.append(child.tag)

	new_elements = []


	new_elements = [item for item, count in collections.Counter(elements).items() if count > 2]
	# print new_elements[0]
	tag = new_elements[0]
	context = et.iterparse(input_file, events=("start", "end"))
	global output_buffer
	global output

	# output file handle
	try:
		output = open(output_file, "w")
	except:
		print("Failed to open the output file")
		raise

	# get to the root
	event, root = context.next()

	items = []
	header_line = []
	field_name = ''
	processed_fields = []

	tagged = False
	started = False
	n = 0


	# iterate through the xml
	for event, elem in context:

		should_write = elem.tag != tag and started and elem.tag

		should_tag = not tagged and should_write and not noheader

		if event == 'start':
			if elem.tag==tag:
				processed_fields=[]
			if elem.tag == tag and not started:
				started = True
			elif should_tag:
				# if elem is nested inside a "parent", field name becomes parent_elem
				field_name = '_'.join((field_name, elem.tag)) if field_name else elem.tag

		else:
			if should_write and elem.tag not in processed_fields:
				processed_fields.append(elem.tag)
				if should_tag:
					header_line.append(field_name)  # add field name to csv header
					# remove current tag from the tag name chain
					field_name = field_name.rpartition('_' + elem.tag)[0]
				items.append('' if elem.text is None else elem.text.strip().replace('"', r'""'))

			# end of traversing the record tag
			elif elem.tag == tag and len(items) > 0:
				# csv header (element tag names)
				if header_line and not tagged:
					output.write(delimiter.join(header_line) + '\n')
				tagged = True

				# send the csv to buffer
				if quotes:
					output_buffer.append(r'"' + (r'"' + delimiter + r'"').join(items) + r'"')
				else:
					output_buffer.append((delimiter).join(items))
				items = []
				n += 1

				if n == limit:
					break


				if len(output_buffer) > buffer_size:
					write_buffer()

			elem.clear()

	write_buffer()
	output.close()

	return n


def write_buffer():
    global output_buffer
    global output

    output.write('\n'.join(output_buffer) + '\n')
    output_buffer = []

input_file = raw_input('Input file name: ')
output_file = raw_input('Output file name: ')

delimiter = raw_input('Delimiter: ')

n = xmlconverstion(input_file, output_file, delimiter)
print "Complete"
