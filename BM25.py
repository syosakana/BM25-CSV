from gensim.summarization.bm25 import BM25
from janome.tokenizer import Tokenizer
import pandas as pd

class best_match:
    def __init__(self):
        self.t = Tokenizer()

    #前処理
    def pre_process(self, docs):
        self.docs = docs
        corpus = [self.wakachi(doc) for doc in self.docs]
        self.bm25_ = BM25(corpus)
    
    #クエリとの順位付け
    def ranking(self, query, ):
        wakachi_query = self.wakachi(query)
        self.scores = self.bm25_.get_scores(wakachi_query, )

    #分かち書き
    def wakachi(self, doc):
        return list(self.t.tokenize(doc, wakati = True))

    #上位n件を抽出
    def select_docs(self, num):
        docs_dict = dict(zip(self.scores, self.docs))
        docs_dict = dict(sorted(docs_dict.items(), reverse = True))
        print("\n・検索結果")
        i = 0
        csv_file_bmrt = "低学年の子供を抱えているか家庭.csv"
        for key, value in docs_dict.items():
            print(round(key, 3), value)
            df_search = round(key, 3), value
            pd.DataFrame(df_search).to_csv(csv_file_bmrt, mode="a", header=False)
            i += 1
            if i == num: break


list_review = []
with open('/home/kanata/chatgpt/review/reviews_tokugawa540.csv') as f:    #csvを行ごとに読み込む
    reader = csv.reader(f) 
    for i in reader:
        print(i[0])
        filter_noun = filter(str.isalnum,i[0])
        cleaned_string = "".join(filter_noun)
        list_review.append(cleaned_string)

print("list_review")
print(list_review)

if __name__ == "__main__":
    query = "低学年の子供を抱えている家庭"
    while True:
        try:
            num = int(input("検索数を自然数で入力してください:"))
            if num <= 0:
                print("0より大きな数字を入力してください。")
            elif num < len(list_review):
                break
            else:
                print("文書数より多い数字が入力されています。")
        except Exception:
            print("数字以外のテキストが入力されています。")

#実行結果
print("クエリ:", query)
inst_BM = best_match()
inst_BM.pre_process(list_review)
inst_BM.ranking(query)
inst_BM.select_docs(num)
