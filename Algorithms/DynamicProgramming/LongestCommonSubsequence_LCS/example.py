from lcs import LCS

x = "AGGTAB"
y = "GXTXAYB"
lcs = LCS(x, y)

print(f"LCS Length: {lcs.compute_lcs()}")
print(f"LCS Sequence: {lcs.get_lcs()}")
