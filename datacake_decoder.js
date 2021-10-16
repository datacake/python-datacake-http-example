function Decoder(request) {

    // hardcoded serial
    var serial = "9c26490c-8cb0-4ab0-a27f-989ffc1f4339";

    /* extract Serial from Payload / request.body (if included)
    you can set individual serial numbers on your datacake devices
    routing is done based on this serial
    you can use same Webhook URL for multiple devices */

    // serial = payload.serial

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
