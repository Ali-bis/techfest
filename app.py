from flask import Flask, render_template, request

app = Flask(__name__)

DNA_TO_BINARY = {
    'A': '00',
    'T': '11',
    'C': '01',
    'G': '10'
}

BINARY_TO_DNA = {
    '00': 'A',
    '11': 'T',
    '01': 'C',
    '10': 'G'
}

def dna_to_binary(sequence):
    result = ''
    for nucleotide in sequence.upper():
        if nucleotide not in DNA_TO_BINARY:
            return None
        result += DNA_TO_BINARY[nucleotide]
    return result

def binary_to_dna(sequence):
    if len(sequence) % 2 != 0:
        return None
    
    result = ''
    for i in range(0, len(sequence), 2):
        two_bits = sequence[i:i+2]
        if two_bits not in BINARY_TO_DNA:
            return None
        result += BINARY_TO_DNA[two_bits]
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    input_value = ''
    
    if request.method == 'POST':
        sequence = request.form.get('sequence', '').strip()
        input_value = sequence
        
        if not sequence:
            error = 'Please enter a sequence.'
        else:
            is_dna = all(c.upper() in 'ATCG' for c in sequence)
            is_binary = all(c in '01' for c in sequence)
            
            if is_dna and not is_binary:
                converted = dna_to_binary(sequence)
                if converted:
                    result = f'Binary: {converted}'
                else:
                    error = 'Invalid DNA sequence. Use only A, T, C, or G.'
            elif is_binary and not is_dna:
                if len(sequence) % 2 != 0:
                    error = 'Binary sequence must have an even length.'
                else:
                    converted = binary_to_dna(sequence)
                    if converted:
                        result = f'DNA: {converted}'
                    else:
                        error = 'Invalid binary sequence. Use only 0 and 1.'
            else:
                error = 'Invalid input. Enter either a DNA sequence (A, T, C, G) or a binary sequence (0, 1).'
    
    return render_template('index.html', result=result, error=error, input_value=input_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
