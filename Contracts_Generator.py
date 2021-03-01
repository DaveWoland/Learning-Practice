import os

contracts = ['salary_change.txt', 'job_change.txt', 'contract_prolongation.txt']

with open("Test_ukol\\employees.txt", "r+") as employees_file:
    employees_info = eval(employees_file.read())

    contract_input = int(input("Please select the option number of action you want to perform:\n"
                               "0. salary change\n"
                               "1. job change\n"
                               "2. contract prolongation\n"))

    chosen_contract = contracts[contract_input]

    path = os.path.join('Test_ukol', chosen_contract)

    for key in employees_info:
        with open(path, "r+") as contract_file:
            text = contract_file.read()
            for key1 in employees_info[key]:
                text = text.replace(f"{{{key1}}}", str(employees_info[key][key1]))

            print(f"Creating contract for {key} ...")
            with open(f"Test_ukol\\{key}_{chosen_contract}", "w") as new_contract:
                new_contract.write(text)

print("Contracts have been generated")

"""
Empolyees info doc and templates docs would be stored in some folder(s) - need to reflect path to such folders.
New contracts should be generated also to specified (existing) folder.

EMPLOYEES_INFO:
                {'X12345' : {'ID': 'X12345', 'full_name': 'Jack Frank',
                    'birthdate': '1.1.1970' , 'job_title' : 'welder',
                    'position_from':'1.5.2015', 'contract_start':'1.2.2013',
                    'contract_end':'31.12.2020', 'salary': 123456},
                'X54321' : {'ID': 'X54321', 'full_name': 'Bob Doe',
                    'birthdate': '8.8.1971' , 'job_title' : 'machinist',
                    'position_from':'1.8.2016', 'contract_start':'1.8.2014',
                    'contract_end':'31.12.2021', 'salary': 23451}}

SALARY_CHANGE:
                Company & CO
                Main Street, 5
                Newyorkshire
                Somewhere

                            SALARY CHANGE


                Employee {full_name}, (ID: {ID}) born on {birthdate},
                has agreed to accept change of the salary amounting to
                {salary} dollars.

                The new salary shall be paid with the next payroll.

                Signature
                ______________
                {full_name}

JOB_CHANGE:
                Company & CO
                Main Street, 5
                Newyorkshire
                Somewhere

                         JOB CHANGE


                Employee {full_name}, (ID: {ID}) born on {birthdate},
                hereby agrees to change the job title to {job_title}.

                This change is valid as of {position_from}

                Signature

                ______________
                {full_name}

CONTRACT_PROLONGATION:
                Company & CO
                Main Street, 5
                Newyorkshire
                Somewhere

                            CONTRACT PROLONGATION


                Employee {full_name}, (ID: {ID}) born on {birthdate},
                hereby agrees to change the employment contract
                termination to {contract_end}.

                This change is performed with immediate validity.

                Signature

                ______________
                {full_name}
"""