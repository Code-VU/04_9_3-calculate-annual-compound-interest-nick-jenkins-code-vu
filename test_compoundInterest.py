def calculateCompoundInterest(p,r,t):
     a = p(1+(r/100))^t
     print("compound interest: "+ str(round(a - p,2)))


def collect_inputs_and_convert_to_float():
    client_p = float(input("principle (amount): "))
    client_t =      float(input("Time:               "))
    client_r =      float(input("Rate:               "))
    return client_p, client_t, client_r

def calculateCompoundInterest():
    client_p_1, client_t_1, client_r_1 = collect_inputs_and_convert_to_float()
    calculateCompoundInterest(client_p_1, client_r_1, client_t_1)
    print("---")
    client_p_2, client_t_2, client_r_2 = collect_inputs_and_convert_to_float()
    calculateCompoundInterest(client_p_2, client_r_2, client_t_2)
    print("---")
    client_p_3, client_t_3, client_r_3 = collect_inputs_and_convert_to_float()
    calculateCompoundInterest(client_p_3, client_r_3, client_t_3)

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":

    calculateCompoundInterest()
