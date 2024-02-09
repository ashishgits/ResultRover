import tabula

tabula.convert_into("./uploads/data.pdf", "result.csv", output_format="csv", pages='all',lattice=True)