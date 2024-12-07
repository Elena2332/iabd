import happybase                                                                                                # type: ignore
import csv

# Conecxion con HBase
connection = happybase.Connection('ec2-52-201-227-30.compute-1.amazonaws.com', port=9090)
table_choco = connection.table('chocolate')


# Leer el CSV y cargar los datos
with open('./datos_chocolate.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    id = 0
    for row in reader:
        table_choco.put(id, 
                {
                    'datos_vaina:bean_origin': row['bean_origin'],
                    'datos_vaina:bean_type': row['bean_type'],
                    'datos_vaina:broad_bean_origin': row['broad_bean_origin'],
                    'datos_tableta:company_maker': row['company_maker'],
                    'datos_tableta:ref': row['ref'],
                    'datos_tableta:review_date': row['review_date'],
                    'datos_tableta:cocoa_percent': row['cocoa_percent'],
                    'datos_tableta:company_location': row['company_location'],
                    'datos_tableta:rating': row['rating'],
                }
            )
        id += 1
    