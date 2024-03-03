from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain

class StreamingConversationalRetrievalChain(ConversationalRetrievalChain, StreamableChain):
    pass