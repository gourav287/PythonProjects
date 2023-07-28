import pandas as pd
import requests

def get_json_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    json_url = "https://jsonplaceholder.typicode.com/users"
    json_data = get_json_data(json_url)

    if json_data:
        # DataFrame for "employee" containing id, name, and username
        employee_df = pd.DataFrame(json_data, columns=['id', 'name', 'username', 'email', 'phone', 'website'])
        print("Employee DataFrame:")
        print(employee_df)

        # Extract "address" fields and create a new DataFrame
        address_df = pd.DataFrame([{"id": item["id"], **item["address"]} for item in json_data])
        address_df = address_df[["id", "street", "suite", "city", "zipcode"]]
        print("\nAddress DataFrame:")
        print(address_df)

        # Extract "geo" fields and create a new DataFrame
        geo_df = pd.DataFrame([{"id": item["id"], **item["address"]["geo"]} for item in json_data])
        print("\nGeo DataFrame:")
        print(geo_df)

        # Extract "company" fields and create a new DataFrame
        company_df = pd.DataFrame([{"id": item["id"], **item["company"]} for item in json_data])
        print("\nCompany DataFrame:")
        print(company_df)