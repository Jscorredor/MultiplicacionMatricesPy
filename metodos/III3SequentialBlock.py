def main():
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    try:
        with open(input_file_path, 'r') as reader, open(output_file_path, 'w') as writer:
            for line in reader:
                # Procesar la línea (por ejemplo, convertir a mayúsculas)
                processed_line = line.upper()
                writer.write(processed_line)

    except IOError as e:
        print(e)

if __name__ == "__main__":
    main()