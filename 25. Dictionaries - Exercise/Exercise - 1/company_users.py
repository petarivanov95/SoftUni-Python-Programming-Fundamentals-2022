companies = {}

while True:
    user_input = input()
    if user_input == "End":
        break
    company_name, company_id = user_input.split(" -> ")
    if company_name not in companies:
        companies[company_name] = [company_id]
    else:
        if company_id in companies[company_name]:
            pass
        else:
            companies[company_name].append(company_id)

for company, id in companies.items():
    print(company)
    for user in companies[company]:
        print(f"-- {user}")
