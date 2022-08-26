import logging

import grpc
import chat_pb2
import chat_pb2_grpc

import threading


def chat_join(stub1):
    for strea in stub1.join(chat_pb2.Message(user='', text='')):
        print("stream >> " + strea.user + ":  " + strea.text + "\n")


if __name__ == '__main__':
    logging.basicConfig()
    # grpc의 불안정한 채널인 위에서 오픈한 50051 포트로 연결합니다.
    # with grpc.insecure_channel('localhost:50051') as channel:
    channel = grpc.insecure_channel('localhost:50051')

    # stub을 생성해줍니다.
    stub = chat_pb2_grpc.ChatStub(channel)

    th1 = threading.Thread(target=chat_join, args=[stub], daemon=True)
    th1.start()

    while True:
        msg = input("message >> ")
        # 요청을 보내고 결과를 받는데, 서버에서 지정한 메서드에 요청시 사용할 proto 메시지 형식으로 요청을 전송합니다.
        try:
            response = stub.send(chat_pb2.Message(user='client3', text=msg))
        except Exception as e:
            print("exit")
