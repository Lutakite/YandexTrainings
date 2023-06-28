def main(N:'int>=0'):
    decompositions = []
    cubes = [i*i*i for i in range(int(N**(1/3)), 0, -1)]
    #print(cubes)
    r = to_sum_of_cubes(N, cubes, decompositions)
    print(len(decompositions[0]))
       
def to_sum_of_cubes(N:'int>=0', cubes:list, decompositions:list):
    #print("N="+str(N))
    #print(cubes)
    #print(decompositions)
    if N in (0, 1):
        #print("here")
        decompositions.append([N])
        return
    if not cubes:
        return
    n = N
    decomposition = []
    for idx in range(len(cubes)):
        while n >= cubes[idx]:
            decomposition.append(cubes[idx])
            n -= cubes[idx]
    
    #print(decomposition)
    decompositions.append(decomposition)
    to_sum_of_cubes(N, cubes[1:], decompositions)
    decompositions.sort(key=lambda x: len(x))
    decompositions = [decompositions[0]]

if __name__ == '__main__':
    n = int(input())
    main(n)