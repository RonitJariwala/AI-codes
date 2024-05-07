def objective(x,target):
    return (x**2)-target
    
def hillClimb(target):
    precision=0.1
    current_sol=0.0
    while True:
        current_objective=objective(current_sol,target)
        if abs(current_objective)<abs(precision):
            break
        if current_objective < 0:
            current_sol += 0.1
        elif current_objective > 0:
            current_sol -= 0.1
    return current_sol
    
target=int(input('Enter the value:'))
sol=hillClimb(target)
print(f"The square root of {target} is {sol:.5f}")            