"""You are given a number ‘n’. You have to tell whether a number is great or not.
A great number is a number whose sum of digits let (m) and product of digits let(j) 
when summed together gives the number back"""

if __name__ == "__main__":
    
    ip_num = int(input())
    ip_list = [int(x) for x in str(ip_num)]
    res_mul = 1
    res_sum = 0
    for i in ip_list:
        res_sum = res_sum + int(i)
    for i in ip_list:
        res_mul = res_mul * int(i)

    if ip_num == (res_mul + res_sum):
        print("Great")
    else:
        print("no")
