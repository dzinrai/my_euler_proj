sum_sqr = 0
srt_sum = 0
for nat in range(1,101):
    sum_sqr = sum_sqr + nat ** 2
for nat in range(1,101):
    srt_sum+=nat
srt_sum = srt_sum ** 2
print(srt_sum - sum_sqr)
