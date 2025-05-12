from datetime import datetime

def valid_date(date: str) -> bool:
    current_date = datetime.now()
    current_str = current_date.strftime("%Y-%m")

    if len(date) == 16 or len(date) == 10:
        for i in range(len(date)):
            if i == 4 or i == 7:
                if date[i] != "-":
                    return False
                else:
                    continue

            elif i == 10:
                if date[i] != " ":
                    return False
                else:
                    continue

            elif i == 13:
                if date[i] != ":":
                    return False
                else:
                    continue

            else:
                try:
                    int(date[i])
                except ValueError:
                    return False
                else:
                    continue

        return True

    else:
        return False

#---------------------------------------------------------------------------

