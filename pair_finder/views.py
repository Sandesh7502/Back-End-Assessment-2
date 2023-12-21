from django.shortcuts import render
from django.http import JsonResponse

def find_pair_with_sum_view(request):
    nums = [5, 2, 6, 8, 1, 9]
    target = 12

    seen = set()
    pairs = []

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    if pairs:
        return JsonResponse({'pairs_found': pairs})
    else:
        return JsonResponse({'message': 'No pair found with the given sum.'})
