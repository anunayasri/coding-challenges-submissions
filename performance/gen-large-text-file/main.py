import random
import argparse


def generate_unicode_text_file(file_path, target_size_mb=1):
    # Define the valid Unicode range (U+0020 to U+FFFF excluding surrogates)
    valid_unicode_chars = [
        chr(i) for i in range(0x0020, 0xD800)
    ] + [
        chr(i) for i in range(0xE000, 0xFFFF)
    ]
    
    # Calculate the target size in bytes (1 GB = 1 * 1024 * 1024 * 1024 bytes)
    target_size_bytes = target_size_mb * 1024 * 1024
    
    # Open the file in write mode with UTF-8 encoding
    with open(file_path, 'w', encoding='utf-8') as file:
        current_size = 0
        chunk_size = 1024 * 1024 * 10  # Write 10 MB chunks at a time to the file
        
        while current_size < target_size_bytes:
            # Generate a chunk of random Unicode characters using precomputed list
            chunk = ''.join(random.choice(valid_unicode_chars) for _ in range(chunk_size))
            
            # Write the chunk to the file
            file.write(chunk)
            
            # Update the current size (each character in UTF-8 encoding may take 1-4 bytes)
            current_size += len(chunk.encode('utf-8'))  # Convert to bytes for accurate size count
            
            # Optionally print progress
            print(f"Written: {current_size / (1024 * 1024)} MB", end='\r')

    print("\nFile generation complete.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('size', help='Size in MB', type=int)
    args = parser.parse_args()

# Generate a 1 GB text file with Unicode characters
generate_unicode_text_file(args.filename, args.size)

