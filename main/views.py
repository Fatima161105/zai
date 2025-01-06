from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Home - Catalog',
        'main': [
    {'image': 'deps/images/p1.png',
    'name':'Носки женские с принтами',
    'discription':'5 ПАР коротких женских носков . Модные , идеально сидят на ногах , подойдут ко всем образам. Яркие и оригинальные. Короткие носки отлично смотрятся на ноге, хорошо тянутся, сохраняя при этом свою форму. Они имеют удобную резинку, которая не сдавливает, а также усиленный носок и пятку, что позволяет избежать натирания. Стильные носки разных цветов станут отличным дополнением к любому образу. носки идеально подходят к обуви, кроссовкам, мокасинам, женским джинсам. Спешите порадовать своих близких и подарить классные носочки. Цветные носки подходят для прогулок, занятий спортом и активного отдыха. школьные, на прогулку, дома . носки средней длины пригодятся везде. Комплект носков подойдет в качестве подарка коллеге-женщине.. Набор женских носков уместен на 8 марта. Хороший недорогой вариант классного подарка для дочери - носки с принтом для женщин.',
    'price': 559 },

    {'image': 'deps/images/p2.png',
    'name':'Детские брюки палаццо',
    'discription':'Ищете комфортные брюки для своей маленькой модницы? Наши брюки палаццо для девочек станут идеальным выбором! Изготовленные из мягких, дышащих тканей, эти широкие брюки идеально подходят для активных игр и повседневных прогулок. Свободный крой не стесняет движений, а яркие расцветки и модные принты помогут создать неповторимый образ. Эти стильные брюки станут любимой вещью в гардеробе вашей девочки! Идеальны как повседневные брюки и летние брюки.',
    'price': 598 },
    
    {'image': 'deps/images/p3.png',
    'name':'Детские брюки палаццо',
    'discription':'Подарите своему малышу тепло и уют с нашим очаровательным детским кигуруми панда! Этот мягкий комбинезон изготовлен из нежного и приятного на ощупь флиса, который согреет в любое время года. Кигуруми для малышей в стиле панды – это идеальный выбор для сна и игр, а милый дизайн обязательно понравится и детям, и взрослым. Это больше чем просто пижама панда – это уют и радость!',
    'price': 1233 },

    {'image': 'deps/images/p7.png',
    'name':'Носки женские махровые высокие 5 пар',
    'discription':"Носки махровые высокие от бренда ZA'I представляют собой идеальный выбор для тех, кто ценит комфорт и стиль. Каждая пара из упаковки содержит 5 штук, что делает их отличным выбором для повседневного использования или как подарок. Состав из 93% полиэстера и 7% эластана обеспечивает идеальное сочетание удобства и прочности, позволяя носкам сохранять свою форму и цвет после многократного использования. Декоративные элементы в виде вышивки добавляют уникальный стиль и изысканность, делая эти носки не только практичными, но и модными аксессуарами. Высокая махровость обеспечивает тепло и комфорт, а легкость материала позволяет носкам легко сочетаться с любыми видами обуви.",
    'price': 960 },

    {'image': 'deps/images/p6.png',
    'name':'Рубашка праздничная с длинными рукавами',
    'discription':"Эта нарядная рубашка с длинным рукавом станет незаменимой вещью в вашем гардеробе! Она прекрасно подходит для торжественных мероприятий, корпоративов, деловых встреч, а также для повседневной носки, если необходимо создать более официальный образ. Эта женская рубашка изготовлена из качественных материалов, что гарантирует ее долговечность и комфорт. Идеально подойдет как женская офисная рубашка и как нарядная рубашка для особых случаев.",
    'price': 1340 },

    {'image': 'deps/images/p4.png',
    'name':'Носки детские с принтами',
    'discription':"Подростковые носки средней длины 5 ПАР с Куроми. Носочки подойдут детям 9-12 лет . Такие носки подойдут для повседневной носки, спортивных занятий , кружков, школы, детского сада. Высокое содержание хлопка является преимуществом, носки очень мягкие и удобные, не давят. В наборе идет 5 пар, носки прослужат долго. Подойдут для мальчиков и девочек.",
    'price': 657 },

    {'image': 'deps/images/p5.png',
    'name':'Носки детские с принтами',
    'discription':"Стильные женские короткие носки 5 ПАР. Модные , идеально сидят на ногах , подойдут ко всем образам.Яркие и оригинальные.Короткие носки отлично смотрятся на ноге, хорошо тянутся, сохраняя при этом свою форму. Они имеют удобную резинку, которая не сдавливает, а также усиленный носок и пятку, что позволяет избежать натирания. Стильные носки разных цветов станут отличным дополнением к любому образу. носки идеально подходят к обуви, кроссовкам, мокасинам, женским джинсам. Спешите порадовать своих близких и подарить классные носочки. Цветные носки подходят для прогулок, занятий спортом и активного отдыха. школьные, на прогулку, дома . носки средней длины пригодятся везде. Комплект носков подойдет в качестве подарка коллеге-женщине. Им не стыдно преподнести подарок на день рождения другу, маме, любимой жене, любимой подруге, бабушке, дедушке, сестре. Набор женских носков уместен на 8 марта. Хороший недорогой вариант классного подарка для дочери - носки с принтом для женщин.",
    'price': 500 },

    {'image': 'deps/images/p9.png',
    'name':'Носки детские Nike',
    'discription':"Детские хлопковые носки короткие Найк.Белоснежные носочки подойдут детям 1-12 лет (нужно выбрать правильный размер). Такие носки подойдут для повседневной носки, спортивных занятий , кружков, школы, детского сада. Высокое содержание хлопка является преимуществом, носки очень мягкие и удобные, не давят. В наборе идет 5 пар, носки прослужат долго. Подойдут для мальчиков и девочек.",
    'price': 647 },

    {'image': 'deps/images/p8.png',
    'name':'Рубашка школьная для девочки',
    'discription':"Рубашка школьная для девочки представляет собой комфортное и стильное решение для каждодневного ношения в школе. Изготовленная из мягкого и эластичного стрейч-хлопка, эта рубашка обеспечивает идеальное сочетание удобства и долговечности. Она оснащена украшающими подвесками на кармане(могут прийти разных моделей) добавляющими особый шарм и индивидуальность. Стильная и практичная, эта рубашка подходит для активного школьного дня, обеспечивая свободное движение и длительный комфорт.Вырез сзади с завязкой обеспечиает комфортное движение, а также придает уникальность данной модели",
    'price': 1068 },
]
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content':"О нас"
    }
    return  render(request, 'main/about.html', context) 

