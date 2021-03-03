from chat_downloader import ChatDownloader
import argparse
import csv

def crawl(url, output):
    chat = ChatDownloader().get_chat(url)       # create a generator

    with open(output, 'w', newline='') as csvfile:        
        writer = csv.writer(csvfile)
        writer.writerow(["author", "message", "time_in_seconds", "time_text", "timestamp"])

        for message in chat:
            writer.writerow([message["author"]["name"], message["message"], message["time_in_seconds"], message["time_text"], message["timestamp"]]) 
            print(chat.format(message))             # print the formatted message
        
    print("Finish!")    
        


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='A simple tool used to retrieve YouTube chat from past broadcasts/VODs. No authentication needed!',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('url', help='YouTube video URL')

    parser.add_argument('-output', '-o', default=None,
                        help='name of output file\n(default: %(default)s = print to standard output)')

    args = parser.parse_args()

    if(args.output is not None and args.output.endswith('.csv')):
        crawl(args.url, args.output)

    else:
        print("Please enter correct output name ! ")
        print("Example: -o test.csv")

    