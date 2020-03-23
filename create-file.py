import sys

def main():
	file = open(sys.argv[1], 'w')
	counter = 0
	size = sys.argv[2]
	character = sys.argv[3]
	input_string =  writeChunk(character, int(size)/512)
	file.write(input_string)
	file.close()

def writeChunk(character, num_chunks):
	chunk_counter = 0
	arr = ""
	while chunk_counter < num_chunks:
		i = 0
		if i < 6:
			if chunk_counter < 10:
				arr += "00000"+str(chunk_counter)
			elif chunk_counter < 100:
				arr += "0000"+str(chunk_counter)
			elif chunk_counter < 1000:
				arr += "000"+str(chunk_counter)
			elif chunk_counter < 10000:
				arr += "00"+str(chunk_counter)
			elif chunk_counter < 100000:
				arr += "0"+str(chunk_counter)
			else:
				arr += str(chunk_counter)
			i += 6
		if i >= 6:
			while i < 512:
				arr += character
				i += 1
				print(i)
			chunk_counter += 1
				
	return arr

if __name__ == '__main__':
	main()