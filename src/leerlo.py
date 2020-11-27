if __name__ == '__main__':
    import csv

    results = []
    with open('ejemplo.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            print(row)
        print(results)

    # with open('ejemplo.csv', newline='') as File:
    #     with open('ejemplo2.csv', 'w') as myFile:
    #         reader = csv.reader(File)
    #         writer = csv.writer(myFile)
    #         writer.writerows(reader)

        # print("Writing complete")
    #myFile = open('ejemplo2.csv', 'w')


    # import csv
    #

