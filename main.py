import requests


# def write to csv file domain_name and status
def write_to_csv(domain_name, status):
    with open('domains.csv', 'a') as f:
        f.write(f'{domain_name};{status}\n')
    

# def clear csv file
def clear_csv():
    with open('domains.csv', 'w') as f:
        f.write('domain_name;available_status\n')

# def open ahrefs.csv and return list of value from first column "Domain"
def get_domains():
    with open('ahrefs.csv', 'r') as f:
        list2 = [row.split()[0].replace('"','') for row in f]
    return list2


def main(api_key, domain_name):
    params = {
        "key": api_key,
        "command": "search",
        "domain0": domain_name,
        "show_price": "1",
        "currency": "USD",
    }
    base_url = "https://api.dynadot.com/api3.json?"
    response = requests.get(base_url, params=params)
    return response.json()


if __name__ == "__main__":
    clear_csv()
    list_of_domains = get_domains()
    api_key = "#################" #dynadot api key

    for domain_name in list_of_domains:
        json_data = main(api_key, domain_name)

        try:
            available_status = json_data["SearchResponse"]["SearchResults"][0]["Available"]

        except Exception as e:
            available_status = "Error"
        
        
        print(domain_name, available_status)
        write_to_csv(domain_name, available_status)



