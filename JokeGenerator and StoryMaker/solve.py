dict=[{'name':"Manjeet",'salary':25000},{'name':"Sandeep",'salary':45000},{'name':"Pankaj",'salary':15000}]

def max_salary_emp(dict):
    min=0
    res={}
    for item in dict:
        if(item['salary']>min):
            min=item['salary']
            res=item

    return res


print(max_salary_emp(dict))