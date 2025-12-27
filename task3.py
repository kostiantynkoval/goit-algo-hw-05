import timeit
from n_Boyer_Moore_subst import boyer_moore_search
from m_KMP_subst_search import kmp_search
from o_Rabin_Karp_subst import rabin_karp_search

if __name__ == '__main__':
    with open('article1.txt', 'r') as article1:
        article1_text = article1.read()
    with open('article2.txt', 'r') as article2:
        article2_text = article2.read()

    article1_text_pattern = "Експоненціальний пошук використовується для пошуку елементів шляхом переходу в експоненціальні позиції"

    boyer_moore_search_article1_time = timeit.timeit(lambda: boyer_moore_search(article1_text, article1_text_pattern), number=1000)
    kmp_search_article1_time = timeit.timeit(lambda: kmp_search(article1_text, article1_text_pattern), number=1000)
    rabin_karp_search_article1_time = timeit.timeit(lambda: rabin_karp_search(article1_text, article1_text_pattern), number=1000)

    article2_text_pattern = "У таблиці 2 наведено результати серії експериментів, проведених для порівняння кількості використаної пам’яті"

    boyer_moore_search_article2_time = timeit.timeit(lambda: boyer_moore_search(article2_text, article2_text_pattern), number=1000)
    kmp_search_article2_time = timeit.timeit(lambda: kmp_search(article2_text, article2_text_pattern), number=1000)
    rabin_karp_search_article2_time = timeit.timeit(lambda: rabin_karp_search(article2_text, article2_text_pattern), number=1000)

    main_string = ''.join(['a' for _ in range(100000)])
    main_string = 'b' + main_string
    pattern = 'baaaaaaaaaaaaaaa'

    boyer_moore_search_easy = timeit.timeit(lambda: boyer_moore_search(main_string, pattern), number=100000)
    kmp_search_easy = timeit.timeit(lambda: kmp_search(main_string, pattern), number=100000)
    rabin_karp_search_easy = timeit.timeit(lambda: rabin_karp_search(main_string, pattern), number=100000)

    boyer_moore_search_time = boyer_moore_search_article1_time + boyer_moore_search_article2_time + boyer_moore_search_easy
    kmp_search_time = kmp_search_article1_time + kmp_search_article2_time + kmp_search_easy
    rabin_karp_search_time = rabin_karp_search_article1_time + rabin_karp_search_article2_time + rabin_karp_search_easy

    print(f"Boyer-Moore article 1: {boyer_moore_search_article1_time}")                 # Time: 0.0426105210208334
    print(f"KMP article 1: {kmp_search_article1_time}")                                 # Time: 0.3576874109567143
    print(f"Rabin-Karp (polynomial) article 1: {rabin_karp_search_article1_time}")      # Time: 0.9084060079767369

    print(f"Boyer-Moore article 2: {boyer_moore_search_article2_time}")                 # Time: 0.0726219950011
    print(f"KMP article 2: {kmp_search_article2_time}")                                 # Time: 0.6296347859897651
    print(f"Rabin-Karp (polynomial) article 2: {rabin_karp_search_article2_time}")      # Time: 1.591428391984664

    print(f"Boyer-Moore Total easy: {boyer_moore_search_easy}")                         # Time: 0.09417712199501693
    print(f"KMP Total easy: {kmp_search_easy}")                                         # Time: 0.10892543598311022
    print(f"Rabin-Karp (polynomial) Total easy: {rabin_karp_search_easy}")              # Time: 0.3564930720021948

    print(f"Boyer-Moore Total: {boyer_moore_search_time}")                              # Time: 0.20940963801695034
    print(f"KMP Total: {kmp_search_time}")                                              # Time: 1.0962476329295896
    print(f"Rabin-Karp (polynomial) Total: {rabin_karp_search_time}")                   # Time: 2.8563274719635956

    # It is clearly seen that Boyer-Moore algorithm is the fastest among the three.
    # The worst algorithm is Rabin-Karp (polynomial).