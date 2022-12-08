with open("input.txt", "r") as file:
    guide = [l.split(" ") for l in file.read().splitlines()]
r_p_s, r_p_s_o, s = {"A":{"X":3,"Y":6,"Z":0},"B":{"X":0,"Y":3,"Z":6},"C":{"X":6,"Y":0,"Z":3}}, {"A":{"X":"Z","Y":"X","Z":"Y"},"B":{"X":"X","Y":"Y","Z":"Z"},"C":{"X":"Y","Y":"Z","Z":"X"}} , {"X":1,"Y":2,"Z":3}
print(f"Part 1 {sum([r_p_s[a][b] + s[b] for a, b in guide])}")
print(f"Part 2 {sum([r_p_s[a][r_p_s_o[a][b]] + s[r_p_s_o[a][b]] for a, b in guide])}")
