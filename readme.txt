GitHub Repositorylarni O‘chirish Qo‘llanmasi

Bu qo‘llanma GitHub-dagi repositorylarni avtomatik ravishda o‘chirish uchun ikkita Python skriptidan foydalanishni tushuntiradi:

1. delete_numeric_repos.py – faqat nomida raqam bo‘lgan repositorylarni o‘chiradi.
2. delete_all_repos.py – barcha repositorylarni o‘chiradi.

1. GitHub Token Yaratish

   - GitHub’ga kiring: https://github.com
   - Settings → Developer settings → Personal access tokens (classic) ga kiring
   - "Generate new token (classic)" tugmasini bosing
   - Quyidagi ruxsatlarni belgilang:
     - repo – Repositorylarga to‘liq kirish
     - delete_repo – Repositorylarni o‘chirish
   - Tokenni nusxalab oling (uni keyin ko‘ra olmaysiz!)

2. delete_numeric_repos.py faylini ishga tushirish nomida raqam bo‘lgan repositorylarni o‘chiradi.

3. delete_all_repos.py faylini ishga tushirish barcha repositorylarni o‘chiradi.

Bu kodlarni ishlatishda ehtiyot bo‘ling, ayniqsa barcha repositorylarni o‘chiradigan skriptni ishlatishdan oldin diqqat bilan tekshiring.