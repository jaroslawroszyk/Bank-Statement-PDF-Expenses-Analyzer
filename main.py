import tabula
import json
import math
import sys

def save_to_json(json_data):
    result = {"data": json_data}
    json_out = json.dumps(result, ensure_ascii=False, indent=4)
    with open("output.json", "w") as jsonFile:
        jsonFile.write(json_out)
        jsonFile.close()

def sum_values_json(json_data):
    sum_values = sum(float(item["Kwota"].replace(',', '.').replace(' ', '')) for item in json_data)
    sumRounder = format(sum_values, ".2f")
    return sumRounder

def extract_table_data(pdf_file):
    try:
        tables = tabula.read_pdf(pdf_file, pages='all')
        json_data = []

        for table in tables:
            if "Kwota" in table.columns:
                amount_column = table["Kwota"]
                for value in amount_column:
                    if isinstance(value, float) and math.isnan(value):
                        continue
                    json_data.append({"Kwota" : value})
        save_to_json(json_data)
        sum = sum_values_json(json_data)
        print(sum)

    except Exception as e:
        print(f"Błąd podczas ekstrakcji danych: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Podaj nazwę pliku PDF jako argument.")
    else:
        pdf_file = sys.argv[1]
        extract_table_data(pdf_file)