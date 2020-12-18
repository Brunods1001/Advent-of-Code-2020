"""
Password philosophy

How many passwords are valid according to their policies?
"""

input = open("input.txt", "r") do f
	read(f, String)
end

vec = split(input, "\n")
vec = vec[vec .!= ""]
num_passes = 0
for (i, pswdi) in enumerate(vec)
	xmin, xmax, letter, pswd = split(pswdi, r"[?:\s-]+")
	xmin, xmax = parse(Int, xmin), parse(Int, xmax)
	letter_count = count(x -> x == letter[1], pswd)
	passes = xmin <= letter_count && letter_count <= xmax
	global num_passes += passes
end

println("Number of valid passwords: ", num_passes)

