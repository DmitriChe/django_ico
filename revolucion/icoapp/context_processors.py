from random import randint


def get_wiseness(request):
    wiseness_list = [
        'Бл҃же́ни ни́щїи дꙋ́хомъ: ꙗ҆́кѡ тѣ́хъ є҆́сть црⷭ҇твїе нбⷭ҇ное.',
        'Бл҃же́ни пла́чꙋщїи: ꙗ҆́кѡ ті́и ѹ҆тѣ́шатсѧ.',
        'Бл҃же́ни кро́тцыи: ꙗ҆́кѡ ті́и наслѣ́дѧтъ ꙁе́млю.',
        'Бл҃же́ни а҆́лчꙋщїи и҆ жа́ждꙋщїи пра́вды: ꙗ҆́кѡ ті́и насы́тѧтсѧ.',
        'Бл҃же́ни млⷭ҇тивїи: ꙗ҆́кѡ ті́и поми́ловани бꙋ́дꙋтъ.',
        'Бл҃же́ни чтⷭ҇їи срⷣцемъ: ꙗ҆́кѡ ті́и бг҃а ѹ҆́ꙁрѧтъ.',
        'Бл҃же́ни миротво́рцы: ꙗ҆́кѡ ті́и сн҃ове бж҃їи нарекꙋ́тсѧ.',
        'Бл҃же́ни и҆ꙁгна́ни пра́вды ра́ди: ꙗ҆́кѡ тѣ́хъ є҆́сть црⷭ҇твїе нбⷭ҇ное.',
        'Бл҃же́ни є҆стѐ, є҆гда̀ поно́сѧтъ ва́мъ, и҆ и҆жденꙋ́тъ, и҆ рекꙋ́тъ всѧ́къ ѕо́лъ глаго́лъ на вы̀ лжꙋ́ще, менє̀ ра́ди: ра́дꙋйтесѧ и҆ весели́тесѧ, ꙗ҆́кѡ мꙁда̀ ва́ша мно́га на нб҃сѣ́хъ: та́кѡ бо и҆ꙁгна́ша прⷪ҇ро́ки, и҆̀же (бѣ́ша) пре́жде ва́съ.',
    ]

    wiseness = wiseness_list[randint(0, len(wiseness_list) - 1)]

    return {"wiseness": wiseness}
