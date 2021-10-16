import requests

if __name__ == "__main__":

    # individual datacake webhook url
    datacake_url = "https://api.datacake.co/integrations/api/ae6dd531-4cf6-4966-b5c9-6c43939aae90/"

    # Just some random demo data
    number_of_persons_a = 234
    number_of_persons_b = 345
    additional_payload = "bla bla"
    some_data = 23.456

    # create api call
    r = requests.post(datacake_url, json={
        "number_of_persons_a": number_of_persons_a,
        "number_of_persons_b": number_of_persons_b,
        "additional_payload": additional_payload,
        "some_data": some_data
    })

    print(r)
