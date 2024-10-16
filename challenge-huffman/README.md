# Challenge Huffman Encoding

[Challenge Link](https://codingchallenges.fyi/challenges/challenge-huffman/)

Using the program

```sh
# Encode
python main.py encode -i les-miserables.txt -o encoded.txt

# Deocde
python main.py decode -i encoded.txt -o decoded.txt

# Profile the encoder
python -m cProfile -o profile_output.prof main.py encode -i les-miserables.txt -o encoded.txt
# Use snakeviz for visualization
snakeviz profile_output.prof
```

Execution 1:

1. Bug: The encoded file is `4x` bigger than the original file 🤦.
   Reason: Instead of wriing bits, I wrote the the string `'0'` and `'1'` to the 
   encoded file. 
2. Profiling showed that building the freq table took `37%` of the time. It is 
   multiple order higher than even reading the file from the disk.

Execution 2:

1. Fixed the bug. Wrote bits ie binary data to the file.
   Orig size: `3.2M` . Encoded data: `1.8M`
2. Profile is still the same. Of course, it will not change since we have not 
    modified the logic to build freq table.
3. I am working on a mac. The original file and decoded data have different sizes,
    although the text content is same. `nvim -d orig decoded` shows not diff. But
    `vimdiff orig decoded` shows a diff at each line!
    Strangely, there is 1 byte missing from each line.
