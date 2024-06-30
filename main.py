def levenshtein_distance(s1, s2):
    # Tạo ma trận với kích thước (len(s1)+1) x (len(s2)+1)
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo hàng đầu tiên và cột đầu tiên của ma trận
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Tính toán các giá trị trong ma trận dựa trên các thao tác chỉnh sửa
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i]
                                   [j - 1], dp[i - 1][j - 1])

    # Giá trị ở ô cuối cùng của ma trận là khoảng cách Levenshtein giữa s1 và s2
    return dp[m][n]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f . readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(file_path='vocab.txt')

import streamlit as st

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):
        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word:', correct_word)

    col1, col2 = st.columns(2)
    col1.write('Vocabulary:')
    col1.write(vocabs)

    col2.write('Distances:')
    col2.write(sorted_distances)


if __name__ == "__main__":
    main()