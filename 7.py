inp = open('7.in', 'r').read()

inpC = [int(x) for x in inp.split(',')]

i = 0

from itertools import permutations

phaseSettings= list(range(5,10))

perms = list(permutations(phaseSettings))




def process(inp, code, arg1, arg2, arg3,lastOutput):
    #print('process: ',i, inp[i:i+20])
    pntr = None
    length = 0
    if code == 1:
        inp[arg3] = arg1 + arg2
        length = 3
    elif code == 2:
        inp[arg3] = arg1 * arg2
        length = 3

    elif code == 3:
        print('INPUT: ',arg2)
        inp[arg1] = arg2
        length = 1
    
    elif code == 4: 
        print('output: ', inp[arg1])
        lastOutput = inp[arg1]
        length = 1
    elif code == 5:
        if arg1 != 0:
            pntr = arg2
        else:
            length = 2
    elif code == 6:
        if arg1 == 0:
            pntr = arg2
        else: length  = 2
    elif code == 7:
        if arg1 < arg2:
            inp[arg3] = 1
        else:
            inp[arg3] = 0
        length = 3
    else:
        if arg1 == arg2:
            inp[arg3] = 1
        else:
            inp[arg3] = 0
        length = 3
        
    return length, pntr, lastOutput

params = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3}
bestSeq = 0
bestSignal = 0
counts = 0

for sequence in perms:
    states = [inpC.copy() for x in range(5)]
    indices = [0 for x in range(5)]
    started = [1 for x in range(5)]
    counts +=1
    seq = list(sequence)
    lastOutput = 0
    lastEOutput = 0
    dones = 0
    ampIndex = 0
    
    while(dones <5):
        
        i = indices[ampIndex]
        inp = states[ampIndex]
        start = started[ampIndex]
        outputted = False
        while(i<len(inp)):
            #print(i)
            length = 0
            if inp[i] == 99: 
                print('exit')
                dones +=1
                pntr = len(inp)
            if inp[i] < 9:
                if inp[i] == 0:
                    print('skip')
                elif inp[i] <3:
                    length, pntr,_ = process(inp, inp[i], inp[inp[i+1]], inp[inp[i+2]], inp[i+3], lastOutput)
                elif inp[i] == 3:
                    print('ampindex', ampIndex)
                    if start==1:
                        length, pntr ,_= process(inp, inp[i], inp[i+1], seq[ampIndex], None, lastOutput)
                        started[ampIndex] = 2
                        start = 2
                    elif start == 2:
                        length, pntr,_ = process(inp, inp[i], inp[i+1], lastOutput, None,lastOutput)
                        start = 3
                    else:
                        length, pntr, _ = process(inp, inp[i], inp[i+1], lastOutput, None,lastOutput)
                elif inp[i]<5: # 4
                    length, pntr, lastOutput  = process(inp, inp[i], inp[i+1], None, None,lastOutput)
                    outputted = True
                elif inp[i] <7: # 5,6
                    length, pntr ,_ = process(inp, inp[i], inp[i+1], inp[i+2], None,lastOutput)
                else:
                    length, pntr,_  = process(inp, inp[i], inp[inp[i+1]], inp[inp[i+2]], inp[i+3],lastOutput)
            elif inp[i]!=99:
                # print(i, 'code: ',inp[i])
                # print(inp[i:i+20])
                code = int(str(inp[i])[-2:])
                modes = [int(x) for x in str(inp[i])[::-1][2:]] + [0]*(params[code]-len(str(inp[i]))+2)
                args = []
                # print(code, modes)
                for k, m in enumerate(modes):
                    if m == 1:
                        args.append(inp[i+k+1])
                    else: 
                        args.append(inp[inp[i+k+1]])
                # print(args)
                if code<3:
                    length, pntr,_ = process(inp, code, args[0], args[1], inp[i+3],lastOutput )
                elif code == 3:
                    if start==1:
                        length, pntr,_ = process(inp, code,args[0], seq[ampIndex], None,lastOutput)
                        start = 2
                        started[ampIndex] = 2
                    else:
                        length, pntr,_ = process(inp, code, args[0], lastOutput, None,lastOutput)
                elif code <5: # 4 
                    length, pntr,_ = process(inp, code, args[0], None, None,lastOutput)
                    outputted = True
                elif code<7:
                    length, pntr,_  = process(inp, code, args[0], args[1], None,lastOutput)
                else:
                    length, pntr,_ = process(inp, code, args[0], args[1], inp[i+3],lastOutput )
                # print('done: ', inp[:20])
            if pntr:
                i = pntr
            else:
                i +=length +1
            if ampIndex==4: lastEOutput = lastOutput
            if outputted:
                break
        indices[ampIndex] = i
        states[ampIndex] = inp
        ampIndex +=1
        ampIndex %= 5
    if lastEOutput > bestSignal:
        bestSignal = lastEOutput
print('best', bestSignal)
print(counts)
print(lastEOutput)