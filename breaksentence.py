# Open the input file for reading
with open('TTSData.txt', 'r') as input_file:
    # Read the contents of the file
    data = input_file.read()
    
    # Split the data into sentences based on the period followed by a space ('. ')
    sentences = data.split('. ')
    
    # Open the output file for writing
    with open('output.txt', 'w') as output_file:
        # Iterate over each sentence
        for sentence in sentences:
            # Write the sentence to the output file with a period and a newline character
            output_file.write(sentence + '.\n')
