def maximum_speciality(patients,speciality):
    pcount=ocount=ecount=0
    for i in range(1,len(patients)):
        if patients[i] == 'P':
            pcount = pcount+1
        elif patients[i] == 'O':
            ocount = ocount+1
        elif patients[i] == 'E':
            ecount = ecount+1
        i = i+2
    
    if(pcount>ocount and pcount>ecount):
        return speciality.get('P')
    elif(ocount>ecount):
        return speciality.get('O')
    else:
        return speciality.get('E')

patients = list(input("Enter Details:"))
speciality = {"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
print(maximum_speciality(patients,speciality))
