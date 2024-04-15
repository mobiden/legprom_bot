from settings import create_logs, COMP_FEAT_LIST


def get_fabric(feature_list: list) -> str:
    create_logs('get_fabric starting', printing=True)
    answer = ''
    found_fabric = []

    print(f'заказ {feature_list}')
    for enum, c_feat in enumerate(COMP_FEAT_LIST):
        complete = True

        for process in feature_list:

            if int(process) not in c_feat:
                complete = False
                break
        if complete:
            found_fabric.append(enum)


    if len(found_fabric) == 0:
        answer = str(f'фабрики под заказ не найдено')
    else:
        answer = f'найдено {len(found_fabric)} фабрик. '
        answer += f'Первые десять: {" ".join(str(i) for i in found_fabric[:10])}'
    #create_logs(f'answer: {answer}', printing=True)
    return answer

