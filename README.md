# Work process

## Disclaimer

- I learned pytest yesterday evening
- I never had the occasion to learn tests professionally in python before (only during 6 months in 2019 with jest in nodeJs)
- I disabled Github copilot for this challenge and did not use Chat GPT

## Challenge

```
1) Write a function that takes as input (sentence: String, n: Number)
and returns a list of size `n` where each element contains a word and and the frequency of that word in `sentence`
This list should be sorted by decreasing frequency and alphabetical order in case of tie.

Example:
Input: ("bar baz foo foo zblah zblah zblah baz toto bar", 3)
Output:
[
   ("zblah", 3),
   ("bar", 2),
   ("baz", 2),
]

2) Write tests for the function you just wrote
```

## prepare environment

```bash
conda create -n foodles-demo python=3.11
conda activate foodles-demo
pip install -r requirements.txt
```

## Run the code

```bash
pytest
```
