from intro_oo import Row, Report


report = Report(2)

report.add_row(Row("natasha", "smith", "WA"))
report.add_row(Row("devin", "lei", "WA"))
report.add_row(Row("bob", "li", "CA"))

assert report.get_number_of_pages() == 2
assert report.size() == 3

assert report.get_paged_rows("-fname", 2) == [report.rows[-1]]

report.remove_row(report.rows[-1].row_id)
assert report.size() == 2
