"""
find the two entries that sum to 2020 and then multiply those two sumnumbers together.
"""

input = open("input", "r") do f
	read(f, String)
end

vec = split(input, "\n")
vec = tryparse.(Float64, vec)
vec = filter(x -> x != nothing, vec)

sumnum = 2020

nums = 3

"""
Uses recursion.
"""

#function findsumnums(vec, sumnum, nums)
#	vsum = sum(vec[1:nums])
#end

NUMS = 3

function findsumnums(vec, sumnum, nums; candidates = [])
	if nums == 0
		println("Finding sum nums ", nums, "\n", candidates, "\n", sumnum)
		if sumnum == 0
			println("nums found! sumnum is ", sumnum)
			println("They are: ", candidates)
			vsum = sum(candidates)
			println("Their sum is: ", vsum)
			if vsum == sumnum
				println("DONE!")
				return candidates
			end
			return candidates
		end
		return findsumnums(
			vec[2:end], sumnum - vec[1], NUMS;
			candidates = [])
	end
	candidates = findsumnums(
		vec[2:end], sumnum - vec[1], nums - 1;
		candidates = [candidates; vec[1]])
	return candidates
end

findsumnums(vec, sumnum, nums)
