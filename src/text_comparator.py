# класс, который сравнивает два текста и возвращает расстояние
class TextComparator:
    def __init__(self):
        # Словарь визуально похожих символов
      self.similar_chars = {
          '0': 'o',
          'o': '0',
          'O': '0',
          '1': 'l',
          'l': '1',
          'I': '1',
          'c': 'с',
          'с': 'c',
          'e': 'е',
          'е': 'e',
          'a': 'а',
          'а': 'a',
          'T': 'Т',
          't': 'т',
          'H': 'Н',
          'n': 'п',
          'p': 'р',
          'B': 'В',
          'B': 'в',
          'в': 'B',
          'в': 'В'
      }

    def compareChars(self, text1, text2):
      # Проверка длины строк
      if len(text1) != len(text2):
        return False
        
      # Проверка каждого символа по отдельности
      for char1, char2 in zip(text1, text2):
        if char1 != char2 and self.similar_chars.get(char1, char1) != char2 and self.similar_chars.get(char2, char2) != char1:
          return False
            
      return True
    
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
                if not self.compareChars(textA[j - 1], textB[i - 1]):
                    mas[i][j] = min(mas[i][j - 1] + 1, mas[i - 1][j] + 1, mas[i - 1][j - 1] + 1)
                else:
                    mas[i][j] = min(mas[i][j - 1] + 1, mas[i - 1][j] + 1, mas[i - 1][j - 1] + 0)
      return mas[n][m]