package_pencils = 5.80
package_markers = 7.20
cleaner = 1.20
package_pencils_full = int(input())
package_markers_full = int(input())
liters_of_cleaner = int(input())

price_for_package_pencils = package_pencils * package_pencils_full
price_for_package_markers = package_markers * package_markers_full
price_for_cleaner = cleaner * liters_of_cleaner
discount = float(input()) / 100
price_for_all_materials = price_for_cleaner + price_for_package_markers + price_for_package_pencils
price_with_discount = price_for_all_materials - (price_for_all_materials * discount)
print(price_with_discount)

