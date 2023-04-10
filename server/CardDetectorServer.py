import socket
import time
import os
import CardDetector
import Cards
import VideoStream

rank_map = {
    "Ace": "a",
    "One": "1",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
    "Six": "6",
    "Seven": "7",
    "Eight": "8",
    "Nine": "9",
    "Ten": "10",
    "Jack": "j",
    "Queen": "a",
    "King": "k",
    "Unknown": ""
}
suit_map = {
    "Hearts": "h",
    "Spades": "s",
    "Diamonds": "d",
    "Clubs": "c",
    "Unknown": ""
}


IM_WIDTH = 1280
IM_HEIGHT = 720
FRAME_RATE = 10
PATH = os.path.dirname(os.path.abspath(__file__))

HOST = "127.0.0.1"
PORT = 14444
videostream = VideoStream.VideoStream((IM_WIDTH, IM_HEIGHT), FRAME_RATE, 2, 0).start()
time.sleep(1)

train_ranks = Cards.load_ranks(PATH + '/Card_Imgs/')
train_suits = Cards.load_suits(PATH + '/Card_Imgs/')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = CardDetector.detect_cards(videostream, train_ranks, train_suits)
                send_val = []
                for i in data:
                    send_val.append(rank_map[i[1]]+suit_map[i[0]])
                for _ in range(5-len(send_val)):
                    send_val.append("")
                s_data = " ".join([x if len(x)==2 else "c" for x in send_val]).encode(encoding="utf-8")
                print(s_data)
                conn.sendall(s_data)
                time.sleep(0.5)
# while True:
#     data = CardDetector.detect_cards(videostream, train_ranks, train_suits)
#     send_val = []
#     for i in data:
#         send_val.append(suit_map[i[0]]+rank_map[i[1]])
#     print([x if len(x)==2 else "c" for x in send_val])
#     time.sleep(0.5)
