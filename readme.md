# Python 2 Datacake

# Introduction

- It's super easy to send Data from Python to Datacake. Here's an example.

# Python Script

- In the following snippet you see a short Python code that is using the Python Requests Package to perfom an HTTP Post Request with encapsulated JSON Data.

```python
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
```

# Datacake Decoder

- We are sending Data to Datacake using an individual webhook url.
- On the device we need to provide a short decoder that decodes the incoming data using a short javascript snippet.
- Paste the following snippet into the Datacake Decoder Section for HTTP Payload Decoder.

```javascript
function Decoder(request) {

    // hardcoded serial
    var serial = "9c26490c-8cb0-4ab0-a27f-989ffc1f4339";

    // extract payload from request.body and parse as json
    var payload = JSON.parse(request.body)

    // extract data
    var number_of_persons_a = payload.number_of_persons_a;
    var number_of_persons_b = payload.number_of_persons_b;
    var additional_payload = payload.additional_payload;
    var some_data = payload.some_data;

    // forward to datacake
    return [
        {
            device: serial, // payload decoder runs on product so we need to tell which device we want to route the data to
            field: "NUMBER_OF_PERSONS_A", // the field identifier from database
            value: number_of_persons_a // the actual data extracted from request.body
        },
        {
            device: serial,
            field: "NUMBER_OF_PERSONS_B",
            value: number_of_persons_b
        },
        {
            device: serial,
            field: "ADDITIONAL_PAYLOAD",
            value: additional_payload
        },
        {
            device: serial,
            field: "SOME_DATA",
            value: some_data
        },
    ];
}
```
