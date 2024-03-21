def solution(citations):
    citations_sorted = sorted(citations, reverse=True)
    h_idx = 0

    for i in range(len(citations_sorted)):
        h_idx = max(h_idx, min(i+1, citations_sorted[i]))

    return h_idx

