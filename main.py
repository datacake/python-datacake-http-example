import requests

if __name__ == "__main__":

    # individual datacake webhook url
    # Change this to the webhook url of your datacake device/product
    datacake_url = "https://api.datacake.co/integrations/api/ae6dd531-4cf6-4966-b5c9-6c43939aae90/"

    # Serial number
    # Include Serial Number in Payload so Datacake can route information
    # based on serial of device
    serial = "python0001"

    # Just some random demo data
    number_of_persons_a = 234
    number_of_persons_b = 345
    additional_payload = "bla bla"
    some_data = 23.456
    a_boolean = True

    # create api call
    r = requests.post(datacake_url, json={
        "number_of_persons_a": number_of_persons_a,
        "number_of_persons_b": number_of_persons_b,
        "additional_payload": additional_payload,
        "some_data": some_data,
        "a_boolean": a_boolean,
        "serial": serial
    })

    print(r)
