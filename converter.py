import json
import base64

useful_fields = [
    "year", "month", "sale_units", "sale_amount"
]
delimiter = ","


def json_to_csv(event, context):
    print(event['records'])
    succeed_cnt = 0
    skip_cnt = 0
    final_output = []
    for record in event['records']:
        output = []
        id = record["recordId"]
        current = json.loads(base64.b64decode(record["data"]))
        print(current)
        for batch in current:
            current_output = []
            skip = False
            for field in useful_fields:
                if field in batch:
                    current_output.append(str(batch[field]))
                else:
                    skip = True
                    break
            if skip:
                skip_cnt += 1
                continue
            succeed_cnt += 1
            output.append(delimiter.join(current_output))
        final_output.append(
            {"recordId": id,
             "result": "Ok",
             "data": base64.b64encode('\n'.join(output).encode("utf-8")).decode("utf-8")
             }
        )
    print('Processing completed.  Successful records {}, Skipped records {}.'.format(succeed_cnt, skip_cnt))
    print(final_output)
    return {"records": final_output}


if __name__ == "__main__":
    with open("data/small.json") as r:
        events = r.read()
        print(json_to_csv({"records": events}, None))

