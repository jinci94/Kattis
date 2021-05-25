# snappereasy + snapperhard:

def easy():
    T = int(input())
    for t in range(T):
        N, K = [int(x) for x in input().split()]
        snappers = ['OFF' for i in range(N)]    # all are OFF
        snappers[0] = '-'   # first one is receiving power (but not ON)

        change1 = {'-':'ON+', 'OFF':'-', 'ON+':'-'}   # snapps the finger (only the first)
        
        #change2 = {'-':'ON+', 'OFF':'-', 'ON':'ON+', 'ON+':'ON+'}  # if the one before turns ON+
        #change3 = {'-':'ON', 'OFF':'OFF', 'ON':'ON', 'ON+':'ON'}  # if the one before turns ON
        #change4 = {'-':'ON', 'OFF':'OFF', 'ON':'ON', 'ON+':'ON'}  # if the one before turns OFF
        #change5 = {'-':'ON', 'OFF':'OFF', 'ON':'ON', 'ON+':'ON'}  # if the one before toggles

        change2 = {'-':'ON+', 'OFF':'-', 'ON':'ON+', 'ON+':'-'}  # if the one before turns ON+
        change3 = {'-':'ON', 'OFF':'OFF', 'ON':'ON', 'ON+':'OFF'}  # if the one before turns ON
        change4 = {'-':'ON', 'OFF':'OFF', 'ON':'ON', 'ON+':'OFF'}  # if the one before turns OFF
        change5 = {'-':'ON', 'OFF':'OFF', 'ON':'ON', 'ON+':'OFF'}  # if the one before toggles

        choose_change = {'ON+':change2, 'ON':change3, 'OFF':change4, '-':change5}
        for i in range(K):
            snappers[0] = change1[snappers[0]]
            for j in range(1,N):
                snappers[j] = choose_change[snappers[j-1]][snappers[j]]
        print(f'Case #{t+1}: ON') if snappers[-1] == 'ON+' else print(f'Case #{t+1}: OFF')

def hard():
    T = int(input())
    for t in range(T):
        N, K = [int(x) for x in input().split()]
        switches_needed = 2**N - 1  # all 'ON' -> all 'ones' binary
        # Soo.. one case is K == switches_needed. To get all: divide by 2**N, since we must add 2**N times for every round.
        print(f'Case #{t+1}: ON') if (K-switches_needed)%(switches_needed+1) == 0 else print(f'Case #{t+1}: OFF')