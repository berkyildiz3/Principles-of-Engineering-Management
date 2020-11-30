import numpy as np
from sys import maxsize
import time


vertex = []
N = 6
def dynamicPr(input, start):
	studyTime1 = 35;
	studyTime2 = 45;
	studyTime3 = 20;
	studyTime4 = 50;
	studyTime5 = 65;
	totalStudyTime = studyTime1 + studyTime2 + studyTime3 + studyTime4 + studyTime5;

	for i in range(N):
		if i != start:
			vertex.append(i)
	minimumDist = maxsize
	while True:
		dist = 0
		j = start
		for i in range(len(vertex)):
			dist += input[j][vertex[i]]
			j = vertex[i]
		dist += input[j][start]
		minimumDist = min(minimumDist, dist)
		if not next_permut(vertex):
			break
	return minimumDist + totalStudyTime
def next_permut(L):
	a = len(L)
	i = a - 2
	while i >= 0 and L[i] >= L[i + 1]:
		i -= 1
	if i == -1:
		return False
	j = i + 1
	while j < a and L[j] > L[i]:
		j += 1
	j -= 1
	L[i], L[j] = L[j], L[i]
	right = a - 1
	left = i + 1
	while left < right:
		L[left], L[right] = L[right], L[left]
		right = right - 1
		left = left + 1
	return True

start = 0
input = [[0, 23, 15, 42, 30, 51],
		[23, 0, 34, 28, 35, 45],
		[15, 34, 0, 48, 62, 27],
		[42, 28, 48, 0, 21, 19],
		[30, 35, 62, 21, 0, 36],
		[51, 45, 27, 19, 36, 0]]
startTime = time.time()
print("Output is ", dynamicPr(input, start))
endTime = time.time()
print("Running time: ", endTime - startTime, " second(s).")


