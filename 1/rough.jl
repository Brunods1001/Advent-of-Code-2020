"""
find the two entries that sum to 2020 and then multiply those two numbers together.
"""

input = open("input", "r") do f
	read(f, String)
end

vec = split(input, "\n")
vec = tryparse.(Float64, vec)
vec = filter(x -> x != nothing, vec)

num = 2020

function findnums(vec)
	for (i, v1) in enumerate(vec[1:end - 2])
		if v1 > num
			continue
		end
		for (j, v2) in enumerate(vec[i + 1:end - 1])
			if v1 + v2 > num
				continue
			end
			for (k, v3) in enumerate(vec[j + 1:end])
				vsum = v1 + v2 + v3
				if vsum == num
					println(v1, " + ", v2, " + ", v3, " = ", vsum)
					println("Found nums ", v1, " ", v2, " ", v3)
					println("Their multiple is ", v1 * v2 * v3)
					return (v1, v2, v3)
				end
			end
		end
	end
	println("Failed to find nums")
	nothing
end

findnums(vec)
