def fds(jl):
    for o in range(1,len(jl)):
        for j in range(0, len(jl)-o):
            if jl[j] > jl[j+1]:
                jl[j],jl[j+1] = jl[j+1],jl[j]
    return jl

jk = [4,5,3,6,7,8,1,2,0]
print(fds(jk))



