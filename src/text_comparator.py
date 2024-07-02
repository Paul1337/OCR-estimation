# класс, который сравнивает два текста и возвращает расстояние
class TextComparator:
  def compare(self, textA, textB):
    m, n = len(textA), len(textB)
    mas = [0] * (n + 1)
    for i in range(0, n + 1):
        mas[i] = [0] * (m + 1)
        for j in range(0, m + 1):
            if i == 0 and j == 0:
                mas[i][j] = 0
            elif i == 0 and j > 0:
                mas[i][j] = j
            elif i > 0 and j == 0:
                mas[i][j] = i
            elif i > 0 and j > 0:
                if textA[j - 1] != textB[i - 1]:
                    mas[i][j] = min(mas[i][j - 1] + 1, mas[i - 1][j] + 1, mas[i - 1][j - 1] + 1)
                else:
                    mas[i][j] = min(mas[i][j - 1] + 1, mas[i - 1][j] + 1, mas[i - 1][j - 1] + 0)
    return mas[n][m]