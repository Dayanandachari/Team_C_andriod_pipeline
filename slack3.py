import requests
import sys
import getopt


# send slack message using slack API

def send_slack_message(message):
    payload = '{"text": "%s"}' % message
    webhook_url = os.environ.get('slack_webhook_url')
    response = requests.post(webhook_url,
                             data=payload)
    
    print(response.text)


def main(argv):
    message = ''

    try:
        opts, args = getopt.getopt(argv, "hm:a:", ["message="])

    except getopt.GetoptError:
        print('slack3.py -m <message>')
        sys.exit(2)

    if len(opts) == 0:
        message = "Hello world"

    for opt, arg in opts:
        if opt == '-h':
            print('slack3.py -m <message>')
            sys.exit()
        elif opt in ("-m", " --<message>"):
            message = arg

    send_slack_message(message)


if __name__ == "__main__":
    # print(sys.argv)
    # print(sys.argv[0])
    # print(sys.argv[1:3])
    # print(sys.argv[1:])
    main(sys.argv[1:])
