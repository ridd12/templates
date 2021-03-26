from hashlib import sha256

def hasher(*args):
    hashing_text=""
    for i in args:
        hashing_text+=str(i)
    div=sha256()
    div.update(hashing_text.encode('utf-8'))
    return div.hexdigest()

class Block():
    def __init__(self,id=0,number=0,data=None):
        self.id=id
        self.number=number
        self.nonce=0
        self.data=data
        self.previous_hash="0"*64
    def hash(self):
        return hasher(self.number,self.nonce,self.data,self.previous_hash)
    def __str__(self):
        return str("Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" %(
            self.number,
            self.hash(),
            self.previous_hash,
            self.data,
            self.nonce
            )
        )

class Blockchain():
    def __init__(self):
        self.dd=[]
    def add_block(self,block):
        self.dd.append(block)
    def remove_block(self,block):
        self.dd.pop(block)
    def mine_block(self,block):
        difficulty=3
        try:block.previous_hash=self.dd[-1].hash()
        except IndexError:pass

        while True:
            if block.hash()[:difficulty]=="0"*difficulty:
                break
            else:block.nonce+=1
        self.add_block(block)

def main():
    blockchain = Blockchain()
    datas=["moe","lister","wants","titty attack"]
    number=0
    # blockchain.mine_block(Block(3,"df"))
    # print(dd)

    for data in datas:
        number+=1
        blockchain.mine_block(Block(number,data))
    # print(datas)
    for block in blockchain.dd:
        print(block)
if __name__=='__main__':
    main()
